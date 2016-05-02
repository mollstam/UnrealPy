
from CoreMisc cimport FCommandLine

cdef class CommandLine:
	@staticmethod
	def is_initialized():
		return FCommandLine.IsInitialized()

	@staticmethod
	def get():
		return FCommandLine.Get()

	@staticmethod
	def set(line):
		return FCommandLine.Set(str(line).decode('utf-8'))
