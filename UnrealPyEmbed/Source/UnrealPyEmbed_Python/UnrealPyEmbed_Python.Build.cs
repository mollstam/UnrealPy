
using System.Diagnostics;
using System.IO;

namespace UnrealBuildTool.Rules
{
    public class UnrealPyEmbed_Python : ModuleRules
    {
        public UnrealPyEmbed_Python(TargetInfo Target)
        {
            //BuildConfiguration.bPrintDebugInfo = true;

            PrivateDependencyModuleNames.AddRange(
                new string[]
                {
                    "Core",
                    "CoreUObject",
                    "EditorStyle",
                    "Engine",
                    "Kismet",
                    "Slate",
                    "SlateCore",
                    "UnrealEd",
                }
            );

            PrivateIncludePaths.AddRange(
                new string[] {
                });

            DynamicallyLoadedModuleNames.AddRange(
                new string[] {
                    "Kismet",
                    "MainFrame",
                });

            PrivateIncludePathModuleNames.AddRange(
                new string[]
                {
                    "MainFrame",
                });

            // if true we will load Python debug build
            bool PythonDebug = false;

            var PythonPath = Path.Combine("..", "Plugins", "Developer", "UnrealPyEmbed", "Source", "Python");
            var PythonLibDirectory = Path.GetFullPath(Path.Combine(PythonPath, "Lib", Target.Platform.ToString()));
            var PythonLibPath = Path.Combine(PythonLibDirectory, GetPythonLibName(Target.Platform, PythonDebug));
            var PythonIncludeSuffix ="Include";

            Log.WriteLine(TraceEventType.Information, "Looking for Python lib at '{0}'", PythonLibPath);
            if (File.Exists(PythonLibPath))
            {
                // Path to Python include files
                var IncludePath = Path.GetFullPath(Path.Combine(PythonPath, PythonIncludeSuffix));
                PrivateIncludePaths.Add(IncludePath);

                Definitions.Add("WITH_PYTHON=1");
                Definitions.Add("Py_NO_ENABLE_SHARED=1");

                if (PythonDebug)
                {
                    // We have some C extensions in here, and they have to link properly
                    Definitions.Add("Py_DEBUG=1");
                }

                // Lib file
                PublicLibraryPaths.Add(PythonLibDirectory);
                PublicAdditionalLibraries.Add(PythonLibPath);

                Log.WriteLine(TraceEventType.Information, "Python Integration enabled: {0}", IncludePath);
            }
            else
            {
                Log.WriteLine(TraceEventType.Information, "Python Integration NOT enabled");
            }
        }

        private System.String GetPythonLibName( UnrealTargetPlatform Platform, bool PythonDebug = false )
        {
            if (Platform == UnrealTargetPlatform.Win32 || Platform == UnrealTargetPlatform.Win64)
            {
                return System.String.Format("python27{0}.lib", PythonDebug ? "_d" : "");
            }
            else
            {
                // todo: debug name of nix lib
                return "libpython2.7.a";
            }
        }

    }
}
