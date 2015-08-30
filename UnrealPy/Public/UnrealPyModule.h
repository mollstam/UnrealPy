
#pragma once

#include "UnrealEd.h"
#include "ModuleInterface.h"

class FUnrealPyModule : public IModuleInterface
{
public:
	/**
	 * Called right after the plugin DLL has been loaded and the plugin object has been created
	 */
	virtual void StartupModule();

	/**
	 * Called before the plugin is unloaded, right before the plugin object is destroyed.
	 */
	virtual void ShutdownModule();
};
