
#include "UnrealPyEmbed_ConsolePrivatePCH.h"
#include "SPythonConsole.h"
#include "Widgets/Docking/SDockTab.h"
#include "Editor/WorkspaceMenuStructure/Public/WorkspaceMenuStructureModule.h"

class FUnrealPyEmbed_ConsoleModule : public IUnrealPyEmbed_ConsoleModule
{

public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
};

IMPLEMENT_MODULE( FUnrealPyEmbed_ConsoleModule, UnrealPyEmbedConsole )

#define LOCTEXT_NAMESPACE "UnrealPyEmbed"

namespace PythonConsoleModule
{
	static const FName PythonConsoleTabName = FName(TEXT("PythonConsole"));
}

/**
 * This entire module is heavily based on the OutputLogModule.
 * If there's ever any problems here from a new engine version,
 * we can probably apply the same fix as over there.
 */

/** This class is to capture all log output even if the log windows is closed */
class FPythonLogHistory : FOutputDevice
{
public:

	FPythonLogHistory()
	{
		GLog->AddOutputDevice(this);
		GLog->SerializeBacklog(this);
	}

	~FPythonLogHistory()
	{
		if (GLog != nullptr)
		{
			GLog->RemoveOutputDevice(this);
		}
	}

	const TArray<TSharedPtr<FLogMessage>>& GetMessages() const
	{
		return Messages;
	}

protected:

	virtual void Serialize(const TCHAR* V, ELogVerbosity::Type Verbosity, const class FName& Category) override
	{
		SPythonConsole::CreateLogMessages(V, Verbosity, Category, Messages);
	}

private:

	TArray<TSharedPtr<FLogMessage>> Messages;
};

static TSharedPtr<FPythonLogHistory> PythonLogHistory;

TSharedRef<SDockTab> SpawnPythonConsole(const FSpawnTabArgs& Args)
{
	return SNew(SDockTab)
		.Icon(FEditorStyle::GetBrush("Log.TabIcon"))
		.TabRole(ETabRole::NomadTab)
		.Label(LOCTEXT("TabTitle", "Python Console"))
		[
			SNew(SPythonConsole).Messages(PythonLogHistory->GetMessages())
		];
}

void FUnrealPyEmbed_ConsoleModule::StartupModule()
{
	FGlobalTabmanager::Get()->RegisterNomadTabSpawner(PythonConsoleModule::PythonConsoleTabName, FOnSpawnTab::CreateStatic(&SpawnPythonConsole))
		.SetDisplayName(LOCTEXT("PythonConsoleTab", "Python Console"))
		.SetTooltipText(LOCTEXT("PythonConsoleTooltipText", "Open the Python Console tab."))
		.SetGroup(WorkspaceMenu::GetMenuStructure().GetDeveloperToolsLogCategory())
		.SetIcon(FSlateIcon(FEditorStyle::GetStyleSetName(), "Log.TabIcon"));

	PythonLogHistory = MakeShareable(new FPythonLogHistory);
}

void FUnrealPyEmbed_ConsoleModule::ShutdownModule()
{
	if (FSlateApplication::IsInitialized())
	{
		FGlobalTabmanager::Get()->UnregisterNomadTabSpawner(PythonConsoleModule::PythonConsoleTabName);
	}
}

#undef LOCTEXT_NAMESPACE
