
#pragma once

#include "BaseTextLayoutMarshaller.h"
#include "SlateBasics.h"

/**
 * This is heavily based on SOutputLog.h, if something breaks here,
 * maybe it's fixed there. :)
 */

class  FPythonConsoleTextLayoutMarshaller;

struct FLogMessage
{
	TSharedRef<FString> Message;
	FName Style;

	FLogMessage(const TSharedRef<FString>& NewMessage, FName NewStyle = NAME_None)
		: Message(NewMessage)
		, Style(NewStyle)
	{
	}
};

/** Console input box */
class SConsoleInputBox
	: public SCompoundWidget
{

public:

	SLATE_BEGIN_ARGS(SConsoleInputBox)
		{}

		/** Called when a console command is executed */
		SLATE_EVENT(FSimpleDelegate, OnConsoleCommandExecuted)
	SLATE_END_ARGS()

	SConsoleInputBox()
	{
	};

	/** Construct this widget, called by SNew() Slate macro. */
	void Construct(const FArguments& InArgs);

	/** Returns the editable text box associated with this widget, used to set focus directly. */
	TSharedRef<SEditableTextBox> GetEditableTextBox()
	{
		return InputText.ToSharedRef();
	}

	// Begin SWidget interface
	virtual void Tick(const FGeometry& AllottedGeometry, const double InCurrentTime, const float InDeltaTime) override;
	// End SWidget interface

protected:

	// Begin SWidget interface
	virtual bool SupportsKeyboardFocus() const override { return true; }
	// End Swidget interface

	/** Handles entering in a command */
	void OnTextCommitted(const FText& InText, ETextCommit::Type CommitInfo);

private:

	/** Editable text widget */
	TSharedPtr<SEditableTextBox> InputText;

};

/** Widget showing Python output and containing an input box */
class SPythonConsole
	: public SCompoundWidget, public FOutputDevice
{

public:

	SLATE_BEGIN_ARGS(SPythonConsole)
		: _Messages()
		{}

		/** All message captured before this window has been created */
		SLATE_ARGUMENT(TArray<TSharedPtr<FLogMessage>>, Messages)

	SLATE_END_ARGS()

	/** Destructor, to unregister from notifications */
	~SPythonConsole();

	/** Construct this widget, called by SNew() Slate macro. */
	void Construct(const FArguments& InArgs);

	/**
	 * Creates FLogMessage objects from FOutputDevice callback
	 * @param	V Message text
	 * @param Verbosity Message verbosity
	 * @param Category Message category
	 * @param OutMessages Array to receive created FLogMessage messages
	 *
	 * @return true if any messages have been created, false otherwise
	 */
	 static bool CreateLogMessages(const TCHAR* V, ELogVerbosity::Type Verbosity, const class FName& Category, TArray<TSharedPtr<FLogMessage>>& OutMessages);

protected:

	virtual void Serialize(const TCHAR* V, ELogVerbosity::Type Verbosity, const class FName& Category) override;

	/** Extends the context menu used by the text box */
	void ExtendTextBoxMenu(FMenuBuilder& Builder);

	/** Called when delete all is selected */
	void OnClearLog();

	/** Called when the user scrolls the log window vertically */
	void OnUserScrolled(float ScrollOffset);

	/** Called to determine whether delete all is currently a valid command */
	bool CanClearLog() const;

	/** Called when a console command is entered in the console */
	void OnConsoleCommandExecuted();

	/** Request we immediately force scroll to the bottom of the log */
	void RequestForceScroll();

protected:

	/** Converts the array of messages into something the text box understands */
	TSharedPtr<FPythonConsoleTextLayoutMarshaller> MessagesTextMarshaller;

	/** The editable text showing all log messages */
	TSharedPtr<SMultiLineEditableTextBox> MessagesTextBox;

	/** True if the user has scrolled the window upwards */
	bool bIsUserScrolled;

private:

	static const FName PythonLogCategory;

};


class FPythonConsoleTextLayoutMarshaller : public FBaseTextLayoutMarshaller
{
public:

	static TSharedRef<FPythonConsoleTextLayoutMarshaller> Create(TArray<TSharedPtr<FLogMessage>> InMessages);

	virtual ~FPythonConsoleTextLayoutMarshaller();

	virtual void SetText(const FString& SourceString, FTextLayout& TargetTextLayout) override;
	virtual void GetText(FString& TargetString, const FTextLayout& SourceTextLayout) override;

	bool AppendMessage(const TCHAR* InText, const ELogVerbosity::Type InVerbosity, const FName& InCategory);
	void ClearMessages();
	int32 GetNumMessages() const;

protected:

	FPythonConsoleTextLayoutMarshaller(TArray<TSharedPtr<FLogMessage>> InMessages);

	void AppendMessageToTextLayout(const TSharedPtr<FLogMessage>& InMessage);

	/** All log messages to show in the text box */
	TArray<TSharedPtr<FLogMessage>> Messages;

	FTextLayout* TextLayout;

};
