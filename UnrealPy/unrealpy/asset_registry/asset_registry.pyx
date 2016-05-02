
from AssetRegistryModule cimport FAssetRegistryModule
from unrealpy.core.modules.ModuleManager cimport FModuleManager
from unrealpy.core.Name cimport FName

cdef class AssetRegistry:

	cdef FAssetRegistryModule* module

	def __cinit__(self):
		self.module = NULL

	def __init__(self):
		self.module = <FAssetRegistryModule*>&FModuleManager.LoadModuleChecked(FName("AssetRegistry"))

	def is_loading_assets(self):
		return self.module.Get().IsLoadingAssets()
