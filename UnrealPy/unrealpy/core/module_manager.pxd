
cdef extern from "Modules/ModuleManager.h":
	cdef cppclass FModuleManager:
		T* load_module[T](FName name, bool was_reloaded=False)
