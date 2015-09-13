
cdef extern from "Core.h":
	pass

cdef extern from "GenericPlatform/GenericPlatformMath.h":
	cdef cppclass FGenericPlatformMath:
		@staticmethod
		#int Max(const int A, const int B)
		T Max[T](const T A, const T B)
