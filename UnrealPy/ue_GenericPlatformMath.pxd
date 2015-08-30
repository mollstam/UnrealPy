
cdef extern from "Core.h":
	pass

cdef extern from "GenericPlatform/GenericPlatformMath.h":
	struct FGenericPlatformMath:
		int Max(const int, const int)
