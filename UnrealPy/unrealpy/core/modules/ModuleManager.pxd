
from core.Name cimport FName

cdef extern from "Modules/ModuleInterface.h":
	cdef cppclass IModuleInterface:
		pass

cdef extern from "Modules/ModuleManager.h":
	cdef cppclass FModuleManager:
		@staticmethod
		IModuleInterface& LoadModuleChecked "LoadModuleChecked<IModuleInterface>" (FName)