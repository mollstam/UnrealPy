
using UnrealBuildTool;
using System.Diagnostics;
using System.IO;

public class UnrealPy : ModuleRules
{
	public UnrealPy(TargetInfo Target)
	{
		PublicIncludePaths.Add("Editor/UnrealEd/Public");

		PrivateDependencyModuleNames.AddRange(
			new string[] {
				"Core",
				"CoreUObject",
				"Engine",
				"UnrealEd",
			}
		);

        PrivateIncludePaths.Add(@"C:\Python27\include");

        PublicLibraryPaths.Add(@"C:\Python27\libs");
        PublicAdditionalLibraries.Add(@"C:\Python27\libs\python27.lib");
	}
}
