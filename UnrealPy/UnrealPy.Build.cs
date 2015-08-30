
using UnrealBuildTool;

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
	}
}
