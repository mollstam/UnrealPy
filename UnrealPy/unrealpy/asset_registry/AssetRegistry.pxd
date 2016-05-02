
from libcpp cimport bool

cdef extern from "IAssetRegistry.h":
	cdef cppclass IAssetRegistry:
		bool IsLoadingAssets() const