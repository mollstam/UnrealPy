
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import pprint, os

global include
include = []

global macros
macros = [
	('PLATFORM_WINDOWS', None),
	('UE_ROCKET', 0),
	('UE_BUILD_DEBUG', 1),
	('WITH_EDITOR', 1),
	('WITH_ENGINE', 1),
	('WITH_UNREAL_DEVELOPER_TOOLS', 1),
	('WITH_PLUGIN_SUPPORT', 0),
	('UE_BUILD_MINIMAL', 0),
	('IS_MONOLITHIC', 0),
	('IS_PROGRAM', 0),
	('WITH_SERVER_CODE', 1),

	('UNICODE', None),
	('_UNICODE', None),

	('WIN32', '1'),
	('_WIN32_WINNT', '0x0600'),
	('WINVER', '0x0600'),

	('CORE_API', 'DLLIMPORT'),
	('COREUOBJECT_API', 'DLLIMPORT'),
]

# --

Core = {
	'include': [
		"",
		"Runtime/Core/Public",
		"Runtime/Core/Public/Internationalization",
		"Runtime/Core/Public/Async",
		"Runtime/Core/Public/Concurrency",
		"Runtime/Core/Public/Containers",
		"Runtime/Core/Public/Delegates",
		"Runtime/Core/Public/GenericPlatform",
		"Runtime/Core/Public/HAL",
		"Runtime/Core/Public/Logging",
		"Runtime/Core/Public/Math",
		"Runtime/Core/Public/Misc",
		"Runtime/Core/Public/Modules",
		"Runtime/Core/Public/Modules/Boilerplate",
		"Runtime/Core/Public/ProfilingDebugging",
		"Runtime/Core/Public/Serialization",
		"Runtime/Core/Public/Serialization/Csv",
		"Runtime/Core/Public/Stats",
		"Runtime/Core/Public/Templates",
		"Runtime/Core/Public/UObject",
	]
}

# --

def add_dependency(m):
	base_path = 'F:\\UnrealEngine\\Engine\\Source\\'
	global include
	for path in Core['include']:
		include.extend([os.path.join(base_path,path)])

# --

add_dependency(Core)

# --

extensions = [
	Extension("Math", ["GenericPlatformMath.pyx"],
		include_dirs = include,
		define_macros = macros,
		language="c++",)
]

# --

setup(
	name = 'GenericPlatformMath',
	ext_modules = cythonize(extensions),
)
