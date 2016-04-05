
#include "../UnrealPyEmbed_PythonPrivatePCH.h"
#include "UnrealPyEmbed.h"
#if WITH_PYTHON
#include <Python/Python.h>
#include <Python/structmember.h>

typedef struct {
	PyObject_HEAD
	int Severity;
} UnrealPyEmbedOutputWriter;

static PyObject* UnrealPyEmbedOutputWriter_New(PyTypeObject* Type, PyObject* Args, PyObject *Kwds)
{
	UnrealPyEmbedOutputWriter* Self;

	Self = (UnrealPyEmbedOutputWriter*)Type->tp_alloc(Type, 0);
	if (Self != NULL)
	{
		Self->Severity = 0;
	}

	return (PyObject*)Self;
}

static int UnrealPyEmbedOutputWriter_Init(UnrealPyEmbedOutputWriter* Self, PyObject* Args, PyObject* Kwds)
{
	static char* Kwlist[] = {"severity", NULL};

	if (!PyArg_ParseTupleAndKeywords(Args, Kwds, "|i", Kwlist, &Self->Severity))
	{
		return -1;
	}

	return 0;
}

static PyObject* UnrealPyEmbedOutputWriter_Write(UnrealPyEmbedOutputWriter* self, PyObject* args)
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

static PyMemberDef UnrealPyEmbedOutputWriter_Members[] = {
	{ "severity", T_INT, offsetof(UnrealPyEmbedOutputWriter, Severity), 0, "Writer severity, 0: stdout  1: stderr" },
	{NULL}
};

static PyMethodDef UnrealPyEmbedOutputWriter_Methods[] = {
	{ "write", (PyCFunction)UnrealPyEmbedOutputWriter_Write, METH_VARARGS, "Prints whatever input to Unreal Editor log" },
	{NULL}
};

static PyTypeObject UnrealPyEmbedOutputWriter_Type = {
	PyObject_HEAD_INIT(NULL)
	0,                         					/*ob_size*/
	"uepy_embed.OutputWriter",    				/*tp_name*/
	sizeof(UnrealPyEmbedOutputWriter), 			/*tp_basicsize*/
	0,                         					/*tp_itemsize*/
	0,                         					/*tp_dealloc*/
	0,                         					/*tp_print*/
	0,                         					/*tp_getattr*/
	0,                         					/*tp_setattr*/
	0,                         					/*tp_compare*/
	0,                         					/*tp_repr*/
	0,                         					/*tp_as_number*/
	0,                         					/*tp_as_sequence*/
	0,                         					/*tp_as_mapping*/
	0,                         					/*tp_hash */
	0,                         					/*tp_call*/
	0,                         					/*tp_str*/
	0,                         					/*tp_getattro*/
	0,                         					/*tp_setattro*/
	0,                         					/*tp_as_buffer*/
	Py_TPFLAGS_DEFAULT,        					/*tp_flags*/
	"Class for redirecting Python "				/* tp_doc */
	"stdout/err to UE logging",
	0,											/* tp_traverse */
	0,											/* tp_clear */
	0,											/* tp_richcompare */
	0,											/* tp_weaklistoffset */
	0,											/* tp_iter */
	0,											/* tp_iternext */
	UnrealPyEmbedOutputWriter_Methods,			/* tp_methods */
	UnrealPyEmbedOutputWriter_Members,          /* tp_members */
	0,											/* tp_getset */
	0,											/* tp_base */
	0,											/* tp_dict */
	0,											/* tp_descr_get */
	0,											/* tp_descr_set */
	0,											/* tp_dictoffset */
	(initproc)UnrealPyEmbedOutputWriter_Init,	/* tp_init */
	0,											/* tp_alloc */
	UnrealPyEmbedOutputWriter_New               /* tp_new */
};


static PyMethodDef UnrealPyEmbed_Methods[] = {
	{NULL}
};

#endif // WITH_PYTHON

void FUnrealPyEmbed::Init()
{
#if WITH_PYTHON

	PyObject* Module;

	UnrealPyEmbedOutputWriter_Type.tp_new = PyType_GenericNew;
	if (PyType_Ready(&UnrealPyEmbedOutputWriter_Type) < 0)
	{
		return;
	}

	Module = Py_InitModule3("uepy_embed", UnrealPyEmbed_Methods, "Helper module for embedding Python in Unreal Editor");

	Py_INCREF(&UnrealPyEmbedOutputWriter_Type);
	PyModule_AddObject(Module, "OutputWriter", (PyObject*)&UnrealPyEmbedOutputWriter_Type);

	PyRun_SimpleString(
		"import uepy_embed\nimport sys\nsys.stdout = uepy_embed.OutputWriter()\nsys.stderr = uepy_embed.OutputWriter(1)\n"
		);

#endif // WITH_PYTHON
}
