
from unreal.platform cimport math

cdef class GenericPlatformMath:
	@staticmethod
	def max(a, b):
		return math.FGenericPlatformMath.Max[long](a, b)
