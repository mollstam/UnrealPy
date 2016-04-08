
#include "UnrealPyEmbed_ConsolePrivatePCH.h"
#include "SPythonConsole.h"
#include "Editor/EditorStyle/Public/EditorStyle.h"
#include "PythonInterpreter.h"
#include "Widgets/Input/SMultilineEditableTextBox.h"

const FName SPythonConsole::PythonLogCategory = FName(TEXT("LogPython"));

BEGIN_SLATE_FUNCTION_BUILD_OPTIMIZATION
void SConsoleInputBox::Construct(const FArguments& InArgs)
{
	ChildSlot
	[
		SAssignNew(InputText, SEditableTextBox)
			.OnTextCommitted(this, &SConsoleInputBox::OnTextCommitted)
			.HintText(NSLOCTEXT("PythonConsole", "TypeInConsoleHint", "Enter Python code"))
	];
}
END_SLATE_FUNCTION_BUILD_OPTIMIZATION

void SConsoleInputBox::Tick(const FGeometry& AllottedGeometry, const double InCurrentTime, const float InDeltaTime)
{
	if (!GIntraFrameDebuggingGameThread && !IsEnabled())
	{
		SetEnabled(true);
	}
	else if (GIntraFrameDebuggingGameThread && IsEnabled())
	{
		SetEnabled(false);
	}
}

void SConsoleInputBox::OnTextCommitted(const FText& InText, ETextCommit::Type CommitInfo)
{
	if (CommitInfo == ETextCommit::OnEnter)
	{
		const FString ExecString = InText.ToString();

		// clear the input area
		InputText->SetText(FText::GetEmpty());

		FPythonInterpreter::Get()->RunString(ExecString);
	}
}

SPythonConsole::~SPythonConsole()
{
	if (GLog != nullptr)
	{
		GLog->RemoveOutputDevice(this);
	}
}

BEGIN_SLATE_FUNCTION_BUILD_OPTIMIZATION
void SPythonConsole::Construct(const FArguments& InArgs)
{
	MessagesTextMarshaller = FPythonConsoleTextLayoutMarshaller::Create(MoveTemp(InArgs._Messages));

	MessagesTextBox = SNew(SMultiLineEditableTextBox)
		.Style(FEditorStyle::Get(), "Log.TextBox")
		.TextStyle(FEditorStyle::Get(), "Log.Normal")
		.ForegroundColor(FLinearColor::Gray)
		.Marshaller(MessagesTextMarshaller)
		.IsReadOnly(true)
		.AlwaysShowScrollbars(true)
		.OnVScrollBarUserScrolled(this, &SPythonConsole::OnUserScrolled)
		.ContextMenuExtender(this, &SPythonConsole::ExtendTextBoxMenu);

	ChildSlot
	[
		SNew(SVerticalBox)
			+SVerticalBox::Slot()
				.FillHeight(1)
			[
				MessagesTextBox.ToSharedRef()
			]
			+SVerticalBox::Slot()
				.AutoHeight()
				.Padding(FMargin(0.0f, 4.0f, 0.0f, 0.0f))
			[
				SNew(SConsoleInputBox)
				.OnConsoleCommandExecuted(this, &SPythonConsole::OnConsoleCommandExecuted)
			]
	];

	GLog->AddOutputDevice(this);

	bIsUserScrolled = false;
	RequestForceScroll();
}
END_SLATE_FUNCTION_BUILD_OPTIMIZATION

bool SPythonConsole::CreateLogMessages(const TCHAR* V, ELogVerbosity::Type Verbosity, const class FName& Category, TArray<TSharedPtr<FLogMessage>>& OutMessages)
{
	// We only log Python output
	if (Category != PythonLogCategory)
	{
		return false;
	}

	if (Verbosity == ELogVerbosity::SetColor)
	{
		return false;
	}

	FName Style = FName(TEXT("Log.Normal"));
	if (Verbosity == ELogVerbosity::Error)
	{
		Style = FName(TEXT("Log.Error"));
	}
	else if (Verbosity == ELogVerbosity::Warning)
	{
		Style = FName(TEXT("Log.Warning"));
	}

	static ELogTimes::Type LogTimestampMode = ELogTimes::None;
	if (UObjectInitialized() && !GExitPurge)
	{
		LogTimestampMode = GetDefault<UEditorStyleSettings>()->LogTimestampMode;
	}

	const int32 OldNumMessages = OutMessages.Num();

	// handle multiline strings by breaking them apart by line
	TArray<FTextRange> LineRanges;
	FString CurrentLogDump = V;
	FTextRange::CalculateLineRangesFromString(CurrentLogDump, LineRanges);

	bool bIsFirstLineInMessage = true;
	for (const FTextRange& LineRange : LineRanges)
	{
		if (!LineRange.IsEmpty())
		{
			FString Line = CurrentLogDump.Mid(LineRange.BeginIndex, LineRange.Len());
			Line = Line.ConvertTabsToSpaces(4);

			// Hard-wrap lines to avoid them being to long
			static const int32 HardWrapLen = 360;
			for (int32 CurrentStartIndex = 0; CurrentStartIndex < Line.Len();)
			{
				int32 HardWrapLineLen = 0;
				if (bIsFirstLineInMessage)
				{
					FString MessagePrefix = FOutputDevice::FormatLogLine(Verbosity, NAME_None, nullptr, LogTimestampMode);

					HardWrapLineLen = FMath::Min(HardWrapLen - MessagePrefix.Len(), Line.Len() - CurrentStartIndex);
					FString HardWrapLine = Line.Mid(CurrentStartIndex, HardWrapLineLen);

					OutMessages.Add(MakeShareable(new FLogMessage(MakeShareable(new FString(MessagePrefix + HardWrapLine)), Style)));
				}
				else
				{
					HardWrapLineLen = FMath::Min(HardWrapLen, Line.Len() - CurrentStartIndex);
					FString HardWrapLine = Line.Mid(CurrentStartIndex, HardWrapLineLen);

					OutMessages.Add(MakeShareable(new FLogMessage(MakeShareable(new FString(MoveTemp(HardWrapLine))), Style)));
				}

				bIsFirstLineInMessage = false;
				CurrentStartIndex += HardWrapLineLen;
			}
		}
	}

	return OldNumMessages != OutMessages.Num();
}

void SPythonConsole::Serialize(const TCHAR* V, ELogVerbosity::Type Verbosity, const class FName& Category)
{
	if (MessagesTextMarshaller->AppendMessage(V, Verbosity, Category))
	{
		// don't scroll to bottom if user is scrolling
		if (!bIsUserScrolled)
		{
			MessagesTextBox->ScrollTo(FTextLocation(MessagesTextMarshaller->GetNumMessages() - 1));
		}
	}
}

void SPythonConsole::ExtendTextBoxMenu(FMenuBuilder& Builder)
{
	FUIAction ClearOutputLogAction(
		FExecuteAction::CreateRaw(this, &SPythonConsole::OnClearLog),
		FCanExecuteAction::CreateSP(this, &SPythonConsole::CanClearLog)
		);

	Builder.AddMenuEntry(
		NSLOCTEXT("OutputLog", "ClearLogLabel", "Clear Log"),
		NSLOCTEXT("OutputLog", "ClearLogTooltip", "Clears all log messages"),
		FSlateIcon(),
		ClearOutputLogAction
		);
}

void SPythonConsole::OnClearLog()
{
	MessagesTextBox->GoTo(FTextLocation(0));
	MessagesTextMarshaller->ClearMessages();
	MessagesTextBox->Refresh();
	bIsUserScrolled = false;
}

void SPythonConsole::OnUserScrolled(float ScrollOffset)
{
	bIsUserScrolled = !FMath::IsNearlyEqual(ScrollOffset, 1.0f);
}

bool SPythonConsole::CanClearLog() const
{
	return MessagesTextMarshaller->GetNumMessages() > 0;
}

void SPythonConsole::OnConsoleCommandExecuted()
{
	RequestForceScroll();
}

void SPythonConsole::RequestForceScroll()
{
	if (MessagesTextMarshaller->GetNumMessages() > 0)
	{
		MessagesTextBox->ScrollTo(FTextLocation(MessagesTextMarshaller->GetNumMessages() - 1));
		bIsUserScrolled = false;
	}
}

TSharedRef<FPythonConsoleTextLayoutMarshaller> FPythonConsoleTextLayoutMarshaller::Create(TArray<TSharedPtr<FLogMessage>> InMessages)
{
	return MakeShareable(new FPythonConsoleTextLayoutMarshaller(MoveTemp(InMessages)));
}

FPythonConsoleTextLayoutMarshaller::~FPythonConsoleTextLayoutMarshaller()
{
}

void FPythonConsoleTextLayoutMarshaller::SetText(const FString& SourceString, FTextLayout& TargetTextLayout)
{
	TextLayout = &TargetTextLayout;
	for (const auto& Message : Messages)
	{
		AppendMessageToTextLayout(Message);
	}
}

void FPythonConsoleTextLayoutMarshaller::GetText(FString& TargetString, const FTextLayout& SourceTextLayout)
{
	SourceTextLayout.GetAsText(TargetString);
}

bool FPythonConsoleTextLayoutMarshaller::AppendMessage(const TCHAR* InText, const ELogVerbosity::Type InVerbosity, const FName& InCategory)
{
	TArray<TSharedPtr<FLogMessage>> NewMessages;
	if (SPythonConsole::CreateLogMessages(InText, InVerbosity, InCategory, NewMessages))
	{
		const bool bWasEmpty = Messages.Num() == 0;
		Messages.Append(NewMessages);

		if (TextLayout)
		{
			// If we were previously empty, then we'd have inserted a dummy empty line into the document
			// We need to remove this line now as it would cause the message indices to get out-of-sync with the line numbers, which would break auto-scrolling
			if(bWasEmpty)
			{
				TextLayout->ClearLines();
			}

			for (const auto& Message : NewMessages)
			{
				AppendMessageToTextLayout(Message);
			}
		}
		else
		{
			MakeDirty();
		}

		return true;
	}

	return false;
}

void FPythonConsoleTextLayoutMarshaller::ClearMessages()
{
	Messages.Empty();
	MakeDirty();
}

int32 FPythonConsoleTextLayoutMarshaller::GetNumMessages() const
{
	return Messages.Num();
}

FPythonConsoleTextLayoutMarshaller::FPythonConsoleTextLayoutMarshaller(TArray<TSharedPtr<FLogMessage>> InMessages)
	: Messages(MoveTemp(InMessages))
	, TextLayout(nullptr)
{
}

void FPythonConsoleTextLayoutMarshaller::AppendMessageToTextLayout(const TSharedPtr<FLogMessage>& InMessage)
{
	const FTextBlockStyle& MessageTextStyle = FEditorStyle::Get().GetWidgetStyle<FTextBlockStyle>(InMessage->Style);

	TSharedRef<FString> LineText = InMessage->Message;

	TArray<TSharedRef<IRun>> Runs;
	Runs.Add(FSlateTextRun::Create(FRunInfo(), LineText, MessageTextStyle));

	TextLayout->AddLine(LineText, Runs);
}
