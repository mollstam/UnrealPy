
#include "UnrealPyEmbed_PythonPrivatePCH.h"
#include "PythonInterpreter.h"
#include "ISettingsModule.h"
#include "UnrealPyEmbedSettings.h"

class FUnrealPyEmbed_PythonModule : public IUnrealPyEmbed_PythonModule
{

public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;

private:

	void RegisterSettings();

	void UnregisterSettings();

	void LoadStartupScripts();
};

IMPLEMENT_MODULE( FUnrealPyEmbed_PythonModule, UnrealPyEmbedAPI )

#define LOCTEXT_NAMESPACE "UnrealPyEmbed"

void FUnrealPyEmbed_PythonModule::StartupModule()
{
	RegisterSettings();

	// Make the interpreter initialize
	FPythonInterpreter::Get();

	LoadStartupScripts();
}

void FUnrealPyEmbed_PythonModule::ShutdownModule()
{
	FPythonInterpreter::Get()->Destroy();

	if (UObjectInitialized())
	{
		UnregisterSettings();
	}
}

void FUnrealPyEmbed_PythonModule::RegisterSettings()
{
	if (ISettingsModule* SettingsModule = FModuleManager::GetModulePtr<ISettingsModule>("Settings"))
	{
		SettingsModule->RegisterSettings("Project", "Plugins", "UnrealPy",
			LOCTEXT("SettingsName", "UnrealPy"),
			LOCTEXT("SettingsDescription", "Configure the UnrealPy plugin"),
			GetMutableDefault<UUnrealPyEmbedSettings>()
		);
	}
}

void FUnrealPyEmbed_PythonModule::UnregisterSettings()
{
	if (ISettingsModule* SettingsModule = FModuleManager::GetModulePtr<ISettingsModule>("Settings"))
	{
		SettingsModule->UnregisterSettings("Project", "Plugins", "UnrealPy");
	}
}

void FUnrealPyEmbed_PythonModule::LoadStartupScripts()
{
	UUnrealPyEmbedSettings* Settings = Cast<UUnrealPyEmbedSettings>(UUnrealPyEmbedSettings::StaticClass()->GetDefaultObject());

	for (const FFilePath& Path : Settings->StartupScripts)
	{
		FPythonInterpreter::Get()->RunFile(Path.FilePath);
	}
}

DEFINE_LOG_CATEGORY(LogPython)

#undef LOCTEXT_NAMESPACE
