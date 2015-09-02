
cimport ue_GenericPlatformMath

cdef class GenericPlatformMath:
	@staticmethod
	def max(a, b):
		return ue_GenericPlatformMath.FGenericPlatformMath.Max[long](a, b)
