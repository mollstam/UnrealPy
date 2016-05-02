
from core.modules.ModuleManager cimport IModuleInterface
from AssetRegistry cimport IAssetRegistry

cdef extern from "AssetRegistryModule.h":
	cdef cppclass FAssetRegistryModule(IModuleInterface):
		IAssetRegistry& Get() const