
#pragma once

#include "ModuleManager.h"

DECLARE_LOG_CATEGORY_EXTERN(LogPython, Log, All);

class IUnrealPyEmbed_PythonModule : public IModuleInterface
{

public:

	static inline IUnrealPyEmbed_PythonModule& Get()
	{
		return FModuleManager::LoadModuleChecked< IUnrealPyEmbed_PythonModule >( "UnrealPyEmbed_Python" );
	}

	static inline bool IsAvailable()
	{
		return FModuleManager::Get().IsModuleLoaded( "UnrealPyEmbed_Python" );
	}
};

