
using System.Diagnostics;
using System.IO;

namespace UnrealBuildTool.Rules
{
    public class UnrealPyEmbed_Python : ModuleRules
    {
        public UnrealPyEmbed_Python(TargetInfo Target)
        {
            BuildConfiguration.bPrintDebugInfo = true;

            PrivateDependencyModuleNames.AddRange(
                new string[]
                {
                    "Core",
                    "CoreUObject",
                    "Engine",
                    "UnrealEd",
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

            /** if true we will load Python debug libs */
            const bool PythonDebug = true;

            var PluginPath = Path.GetFullPath("../Plugins/Developer/UnrealPyEmbed");
            var PythonPath = PluginPath + "/Source/Python";
            var PythonLibDirectory = PythonPath + "/Lib";
            var LibName = "python27" + (PythonDebug ? "_d" : "");
            var PythonIncludeSuffix = "Include";

            // Path to Python include files
            var IncludePath = Path.GetFullPath(Path.Combine(PythonPath, PythonIncludeSuffix));
            PrivateIncludePaths.Add(IncludePath);

            Definitions.Add("WITH_PYTHON=1");
            Definitions.Add("Py_ENABLE_SHARED=1");

            if (PythonDebug)
            {
                // We have some C extensions in here, and they have to link properly
                Definitions.Add("Py_DEBUG=1");
                Definitions.Add("_DEBUG=1");
            }

            if (Target.Platform == UnrealTargetPlatform.Win64)
            {
                PublicLibraryPaths.Add(PythonLibDirectory + "/Win64");
                PublicAdditionalLibraries.Add(LibName + ".lib");
                RuntimeDependencies.Add(new RuntimeDependency(LibName + ".dll"));
            }
        }
    }
}
