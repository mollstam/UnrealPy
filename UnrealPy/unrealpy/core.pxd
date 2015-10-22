
# ints

# would be nice to get these from the actual def during UE compilation
# so it matches the current platform, currently taking some generic defaults

ctypedef unsigned char uint8_t
ctypedef unsigned short int uint16
ctypedef unsigned int uint32
ctypedef unsigned long long uint64
ctypedef signed char int8
ctypedef signed short int int16
ctypedef signed int int32
ctypedef signed long long int64
ctypedef char ANSICHAR
#ctypedef wchar_t WIDECHAR
ctypedef uint8_t CHAR8
ctypedef uint16 CHAR16
ctypedef uint32 CHAR32
#ctypedef WIDECHAR TCHAR

cdef uint8_t uint8


# FName

cdef extern from "UObject/NameTypes.h":
	ctypedef int32 NAME_INDEX
	cdef cppclass FName:
		NAME_INDEX ComparisonIndex
		# DisplayIndex may not be declared if UE is compiled with
		# WITH_CASE_PRESERVING_NAME set to falsish, might need to
		# include that condition here too when it fails.
		NAME_INDEX DisplayIndex
		uint32 Number
