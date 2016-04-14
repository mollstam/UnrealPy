
#include "../UnrealPyEmbed_PythonPrivatePCH.h"
#include "UnrealPyEmbedExtOutputWriter.h"
#if WITH_PYTHON
#include <Python/structmember.h>

namespace UnrealPyEmbedExtOutputWriter
{

	static PyMemberDef UnrealPyEmbedOutputWriter_Members[] = {
		{ "severity", T_INT, offsetof(UnrealPyEmbedOutputWriter, Severity), 0, "Writer severity, 0: stdout  1: stderr" },
		{NULL}
	};

	static PyMethodDef UnrealPyEmbedOutputWriter_Methods[] = {
		{ "write", (PyCFunction)FUnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Write, METH_VARARGS, "Prints whatever input to Unreal Editor log" },
		{NULL}
	};

	static PyTypeObject UnrealPyEmbedOutputWriter_Type = {
		PyObject_HEAD_INIT(NULL)
		0,                         													/*ob_size*/
		"uepy_embed.OutputWriter",    												/*tp_name*/
		sizeof(UnrealPyEmbedOutputWriter), 											/*tp_basicsize*/
		0,                         													/*tp_itemsize*/
		0,                         													/*tp_dealloc*/
		0,                         													/*tp_print*/
		0,                         													/*tp_getattr*/
		0,                         													/*tp_setattr*/
		0,                         													/*tp_compare*/
		0,                         													/*tp_repr*/
		0,                         													/*tp_as_number*/
		0,                         													/*tp_as_sequence*/
		0,                         													/*tp_as_mapping*/
		0,                         													/*tp_hash */
		0,                         													/*tp_call*/
		0,                         													/*tp_str*/
		0,                         													/*tp_getattro*/
		0,                         													/*tp_setattro*/
		0,                         													/*tp_as_buffer*/
		Py_TPFLAGS_DEFAULT,        													/*tp_flags*/
		"Class for redirecting Python "												/* tp_doc */
		"stdout/err to UE logging",
		0,																			/* tp_traverse */
		0,																			/* tp_clear */
		0,																			/* tp_richcompare */
		0,																			/* tp_weaklistoffset */
		0,																			/* tp_iter */
		0,																			/* tp_iternext */
		UnrealPyEmbedOutputWriter_Methods,											/* tp_methods */
		UnrealPyEmbedOutputWriter_Members,          								/* tp_members */
		0,																			/* tp_getset */
		0,																			/* tp_base */
		0,																			/* tp_dict */
		0,																			/* tp_descr_get */
		0,																			/* tp_descr_set */
		0,																			/* tp_dictoffset */
		(initproc)FUnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Init,	/* tp_init */
		0,																			/* tp_alloc */
		FUnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_New				/* tp_new */
	};

	static PyMethodDef UnrealPyEmbed_Methods[] = {
		{NULL}
	};

} // namespace UnrealPyEmbedExtOutputWriter

PyObject* FUnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_New(PyTypeObject* Type, PyObject* Args, PyObject *Kwds)
{
	UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter* Self;

	Self = (UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter*)Type->tp_alloc(Type, 0);
	if (Self != NULL)
	{
		Self->Severity = 0;
	}

	return (PyObject*)Self;
}

int FUnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Init(UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter* Self, PyObject* Args, PyObject* Kwds)
{
	static char* Kwlist[] = {"severity", NULL};

	if (!PyArg_ParseTupleAndKeywords(Args, Kwds, "|i", Kwlist, &Self->Severity))
	{
		return -1;
	}

	return 0;
}

PyObject* FUnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Write(UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter* self, PyObject* args)
{
	char* CString;
	if (!PyArg_ParseTuple(args, "s:write", &CString))
	{
		return NULL;
	}

	FString String(ANSI_TO_TCHAR(CString));
	String.TrimTrailing();
	if (!String.IsEmpty())
	{
		// print('x') will send both 'x' and '\n' in separate calls so we ignore lone new lines
		// if you want to print a newline, send a space, or double \n\n
		if (self->Severity == 0)
		{
			UE_LOG(LogPython, Log, TEXT("%s"), *String);
		}
		else
		{
			UE_LOG(LogPython, Error, TEXT("%s"), *String);
		}
	}

	return Py_BuildValue("");
}

#endif // WITH_PYTHON

void FUnrealPyEmbedExtOutputWriter::Init()
{
#if WITH_PYTHON

	PyObject* Module;

	UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Type.tp_new = PyType_GenericNew;
	if (PyType_Ready(&UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Type) < 0)
	{
		return;
	}

	Module = Py_InitModule3("_upy_ext_output", UnrealPyEmbedExtOutputWriter::UnrealPyEmbed_Methods, "Helper module for embedding Python in Unreal Editor");

	/** redirecting stdout and stderr to UE logging */
	Py_INCREF(&UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Type);
	PyModule_AddObject(Module, "OutputWriter", (PyObject*)&UnrealPyEmbedExtOutputWriter::UnrealPyEmbedOutputWriter_Type);
	PyRun_SimpleString(
		"from _upy_ext_output import OutputWriter\nimport sys\nsys.stdout = OutputWriter()\nsys.stderr = OutputWriter(1)\n"
		);

#endif // WITH_PYTHON
}
