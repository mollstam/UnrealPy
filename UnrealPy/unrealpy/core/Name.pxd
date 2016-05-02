
cdef extern from "UObject/NameTypes.h":
	cdef cppclass FName:
		FName()
		FName(const char* Name)
