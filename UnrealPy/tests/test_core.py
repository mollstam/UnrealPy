
import sys
import os

print(os.path.abspath('.'))
print(sys.path)
print('rpath env var:', os.environ.get('DYLD_LIBRARY_PATH'))

from unrealpy.core import uint8


def test_uint8_size():
    """Make sure uint8 is of the expected size."""
    i = uint8(3)
    assert sys.getsizeof(i) == 8
