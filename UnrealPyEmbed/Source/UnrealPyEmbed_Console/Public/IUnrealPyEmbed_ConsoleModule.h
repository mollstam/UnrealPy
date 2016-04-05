
#pragma once

#include "ModuleManager.h"

class IUnrealPyEmbed_ConsoleModule : public IModuleInterface
{

public:

	static inline IUnrealPyEmbed_ConsoleModule& Get()
	{
		return FModuleManager::LoadModuleChecked< IUnrealPyEmbed_ConsoleModule >( "UnrealPyEmbed_Console" );
	}

	static inline bool IsAvailable()
	{
		return FModuleManager::Get().IsModuleLoaded( "UnrealPyEmbed_Console" );
	}
};

