
#pragma once

#include "UnrealPyEmbedSettings.generated.h"

UCLASS(config=Engine, defaultconfig)
class UNREALPYEMBED_PYTHON_API UUnrealPyEmbedSettings : public UObject
{
public:
	GENERATED_BODY()

	UUnrealPyEmbedSettings();

public:

	/** List of Python scripts to run when editor starts */
	UPROPERTY(GlobalConfig, EditAnywhere, Category = Settings, meta=(FilePathFilter = "py"))
	TArray<FFilePath> StartupScripts;
};
