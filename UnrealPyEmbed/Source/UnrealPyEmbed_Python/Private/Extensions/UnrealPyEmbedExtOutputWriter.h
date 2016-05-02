
#pragma once

#if WITH_PYTHON
#include <Python/Python.h>

namespace UnrealPyEmbedExtOutputWriter {
	typedef struct {
		PyObject_HEAD
			int Severity;
	} UnrealPyEmbedOutputWriter;
}
#endif // WITH_PYTHON

class FUnrealPyEmbedExtOutputWriter
{
public:

	/** Initializes the Python extension and automatically hooks into stdout/err streams */
	static void Init();

#if WITH_PYTHON

	static int UnrealPyEmbedOutputWriter_Init(UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter* Self, PyObject* Args, PyObject* Kwds);

	static PyObject* UnrealPyEmbedOutputWriter_Write(UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter* self, PyObject* args);

#endif // WITH_PYTHON

};
