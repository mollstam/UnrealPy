
from unreal.core.module_manager import FModuleManager

cdef extern from "IAssetRegistry.h":
	cdef cppclass IAssetRegistry:
		pass

cdef extern from "AssetRegistryModule.h":
	cdef cppclass FAssetRegistryModule:
		@staticmethod
		IAssetRegistry Get()
