
from core.hal.Platform cimport TCHAR
from libcpp cimport bool

cdef extern from "Misc/CoreMisc.h":
	cdef cppclass FCommandLine:
		@staticmethod
		bool IsInitialized()
		@staticmethod
		const TCHAR* Get()
		@staticmethod
		bool Set(const TCHAR*)
