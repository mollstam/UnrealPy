
cimport ue_GenericPlatformMath

cdef class GenericPlatformMath:
	@staticmethod
	def max(a, b):
		ue_GenericPlatformMath.Max(a, b)
