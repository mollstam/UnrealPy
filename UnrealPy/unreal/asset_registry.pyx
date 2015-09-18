
from unreal import asset_registry

cdef class AssetRegistry:
	@staticmethod
	def get_assets_by_package_name(package_name):
		asset_registry_module = get_asset_registry_module()
		if not asset_registry_module:
			raise Exception('Unable to load module')
		asset_registry = asset_registry_module.Get()
		assets = []
		asset_registry.GetAssetsByPackageName(package_name, assets)
		return assets

cdef FAssetRegistryModule* get_asset_registry_module():
	cdef FAssetRegistryModule* module
	module = FModuleManager.load_module[FAssetRegistryModule]("AssetRegistry")
	return module
