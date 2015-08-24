
#include "UnrealPyEmbedPrivatePCH.h"

class FUnrealPyEmbedModule : public IUnrealPyEmbedModule
{
	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
};

IMPLEMENT_MODULE( FUnrealPyEmbedModule, UnrealPyEmbed )

void FUnrealPyEmbedModule::StartupModule()
{
}


void FUnrealPyEmbedModule::ShutdownModule()
{
}



