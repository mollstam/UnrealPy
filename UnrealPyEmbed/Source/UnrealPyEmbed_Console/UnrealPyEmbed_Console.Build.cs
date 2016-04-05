
using System.Diagnostics;
using System.IO;

namespace UnrealBuildTool.Rules
{
    public class UnrealPyEmbed_Console : ModuleRules
    {
        public UnrealPyEmbed_Console(TargetInfo Target)
        {
            BuildConfiguration.bPrintDebugInfo = true;

            PrivateDependencyModuleNames.AddRange(
                new string[]
                {
                    "Core",
                    "CoreUObject",
                    "EditorStyle",
                    "Engine",
                    "Slate",
                    "SlateCore",
                    "UnrealEd",
                    "WorkspaceMenuStructure",
                    "UnrealPyEmbed_Python",
                }
            );

            PrivateIncludePaths.AddRange(
                new string[] {
                });

            DynamicallyLoadedModuleNames.AddRange(
                new string[] {
                });

            PrivateIncludePathModuleNames.AddRange(
                new string[]
                {
                });
        }
    }
}
