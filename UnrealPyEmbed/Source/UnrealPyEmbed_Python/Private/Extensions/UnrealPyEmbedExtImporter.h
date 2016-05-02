
#pragma once

#if WITH_PYTHON
#include <Python/Python.h>

namespace UnrealPyEmbedExtImporter {
	typedef struct {
		PyObject_HEAD
	} UnrealPyEmbedImporter;
}
#endif // WITH_PYTHON

class FUnrealPyEmbedExtImporter
{
public:

	/** Initializes the Python extension and registeres a path hook */
	static void Init();

#if WITH_PYTHON

#endif // WITH_PYTHON

};
