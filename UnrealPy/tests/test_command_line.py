
def test_import():
	from unrealpy.core.misc.core_misc import CommandLine

def test_not_initialized():
	from unrealpy.core.misc.core_misc import CommandLine
	assert CommandLine.is_initialized() == False

def test_intialize():
	from unrealpy.core.misc.core_misc import CommandLine
	line = '-test -command -line'
	CommandLine.set(line)
	assert CommandLine.is_initialized() == True
	assert CommandLine.get() == line