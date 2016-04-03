
#include "UnrealPyEmbed_PythonPrivatePCH.h"
#include "PythonInterpreter.h"

class FUnrealPyEmbed_PythonModule : public IUnrealPyEmbed_PythonModule
{

public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
};

IMPLEMENT_MODULE( FUnrealPyEmbed_PythonModule, UnrealPyEmbedAPI )

#define LOCTEXT_NAMESPACE "UnrealPyEmbed"

void FUnrealPyEmbed_PythonModule::StartupModule()
{
	FPythonInterpreter::Get()->RunString(FString(TEXT("print('Python loaded')\n")));
}

void FUnrealPyEmbed_PythonModule::ShutdownModule()
{
	FPythonInterpreter::Get()->Destroy();
}

DEFINE_LOG_CATEGORY(LogPython)

#undef LOCTEXT_NAMESPACE
