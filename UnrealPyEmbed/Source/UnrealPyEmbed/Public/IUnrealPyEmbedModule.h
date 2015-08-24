
#pragma once

#include "ModuleManager.h"

class IUnrealPyEmbedModule : public IModuleInterface
{

public:

	static inline IUnrealPyEmbedModule& Get()
	{
		return FModuleManager::LoadModuleChecked< IUnrealPyEmbedModule >( "UnrealPyEmbed" );
	}

	static inline bool IsAvailable()
	{
		return FModuleManager::Get().IsModuleLoaded( "UnrealPyEmbed" );
	}
};

