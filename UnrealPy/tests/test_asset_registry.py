
def test_import():
	from unrealpy.asset_registry import AssetRegistryModule

def test_get_module():
	from unrealpy.core.misc.core_misc import CommandLine
	if not CommandLine.is_initialized():
		CommandLine.set('')
	from unrealpy.asset_registry import AssetRegistryModule
	module = AssetRegistryModule.get()
	assert module != None
