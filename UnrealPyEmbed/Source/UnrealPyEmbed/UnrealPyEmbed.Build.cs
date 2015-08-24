
using System.Diagnostics;

namespace UnrealBuildTool.Rules
{
	public class UnrealPyEmbed : ModuleRules
	{
		public UnrealPyEmbed(TargetInfo Target)
		{
			PrivateDependencyModuleNames.AddRange(
				new string[]
				{
					"Core",
					"UnrealPyEmbed_Python",
				}
			);

			PrivateIncludePaths.AddRange(
				new string[] {
				});

			DynamicallyLoadedModuleNames.AddRange(
				new string[] {
				});
			}
	}
}
