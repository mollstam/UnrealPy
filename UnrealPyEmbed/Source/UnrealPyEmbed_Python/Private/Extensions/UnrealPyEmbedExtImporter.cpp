
#include "../UnrealPyEmbed_PythonPrivatePCH.h"
#include "UnrealPyEmbedExtImporter.h"
#include "PathSnooper.h"
#if WITH_PYTHON
#include <Python/structmember.h>
#include "PythonInterpreter.h"

namespace UnrealPyEmbedExtImporter
{

	static TArray<FString> DllDirectories;

	static int UnrealPyEmbedImporter_Init(UnrealPyEmbedImporter* Self, PyObject* Args, PyObject* Kwds)
	{
		if (!_PyArg_NoKeywords("Importer()", Kwds))
			return -1;

		PyObject* Path;
		if (!PyArg_ParseTuple(Args, "O:Importer",
			&Path))
			return -1;
		if (!PyString_Check(Path))
		{
			return -1;
		}
		
		return 0;
	}

	/** Check if we can import. Return self if we can, otherwise null */
	static PyObject* UnrealPyEmbedImporter_FindModule(PyObject* Obj, PyObject* Args)
	{
		UnrealPyEmbedImporter* Self = (UnrealPyEmbedImporter*)Obj;
		char* Fullname;
		if (!PyArg_ParseTuple(Args, "s:Importer.find_module",
			&Fullname))
			return 0;

		// doesn't do any checking, just say yes

		Py_INCREF(Self);
		return (PyObject*)Self;
	}

	/** Load and return the module, or raise ImportError if unable */
	static PyObject* UnrealPyEmbedImporter_LoadModule(PyObject* Obj, PyObject* Args)
	{
		UnrealPyEmbedImporter* Self = (UnrealPyEmbedImporter*)Obj;

		char* Fullname;
		if (!PyArg_ParseTuple(Args, "s:Importer.load_module", &Fullname))
		{
			return 0;
		}

		// call without any hooks or cache but reset afterwards
		PyObject* PathHooks = PySys_GetObject("path_hooks");
		Py_INCREF(PathHooks);
		PyObject* PathImporterCache = PySys_GetObject("path_importer_cache");
		Py_INCREF(PathImporterCache);
		// test
		PyDictObject* mp = (PyDictObject*)PathImporterCache;
		PyDictEntry* ep;
		Py_ssize_t fill = mp->ma_fill;
		for (ep = mp->ma_table; fill > 0; ep++) {
			if (ep->me_key) {
				--fill;
				PyObject* key = ep->me_key;
				PyObject* val = ep->me_value;
				_typeobject* val_type = val->ob_type;
			}
		}

		PyObject* EmptyHooks = PyList_New(0);
		PyObject* m = 0;
		if (PySys_SetObject("path_hooks", EmptyHooks))
		{
			UE_LOG(LogPython, Error, TEXT("Unable to set path hooks"));
		}
		else
		{
			PyObject* EmptyCache = PyDict_New();
			if (PySys_SetObject("path_importer_cache", EmptyCache))
			{
				UE_LOG(LogPython, Error, TEXT("Unable to set importer cache"));
			}
			else
			{
				const int32 MaxPathVarLen = 32768;
				TCHAR OrigPathVarMem[MaxPathVarLen];
				FPlatformMisc::GetEnvironmentVariable(TEXT("PATH"), OrigPathVarMem, MaxPathVarLen);
				FString OrigPathVar(OrigPathVarMem);
				const TCHAR* PathDelimiter = FPlatformMisc::GetPathVarDelimiter();
				FString PathVar = FString::Join(DllDirectories, FPlatformMisc::GetPathVarDelimiter())
					+ FPlatformMisc::GetPathVarDelimiter()
					+ OrigPathVar;
				FPlatformMisc::SetEnvironmentVar(TEXT("PATH"), *PathVar);

				// Do the actual import
				m = PyImport_ImportModule(Fullname);

				// restore state
				FPlatformMisc::SetEnvironmentVar(TEXT("PATH"), *OrigPathVar);

				PySys_SetObject("path_importer_cache", PathImporterCache);
			}
			PySys_SetObject("path_hooks", PathHooks);
			Py_DECREF(EmptyCache);
		}
		Py_DECREF(EmptyHooks);
		Py_DECREF(PathHooks);
		Py_DECREF(PathImporterCache);
		
		return m;
	}

	static PyMethodDef UnrealPyEmbedImporter_Methods[] = {
		{ "find_module", UnrealPyEmbedImporter_FindModule, METH_VARARGS,
		"find_module(fullname, path=None) -> self or None." },
		{ "load_module", UnrealPyEmbedImporter_LoadModule, METH_VARARGS,
		"load_module(fullname) -> module." },
		{ NULL, NULL }
	};

	static PyTypeObject UnrealPyEmbedImporter_Type = {
		PyObject_HEAD_INIT(NULL)
		0,                         													/*ob_size*/
		"_upy_ext_import.Importer",												/*tp_name*/
		sizeof(UnrealPyEmbedImporter), 											/*tp_basicsize*/
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
		0,												/*tp_call*/
		0,                         													/*tp_str*/
		0,                         													/*tp_getattro*/
		0,                         													/*tp_setattro*/
		0,                         													/*tp_as_buffer*/
		Py_TPFLAGS_DEFAULT,        													/*tp_flags*/
		"Class to run as path_hook for import to work inside UE4",					/* tp_doc */
		0,																			/* tp_traverse */
		0,																			/* tp_clear */
		0,																			/* tp_richcompare */
		0,																			/* tp_weaklistoffset */
		0,																			/* tp_iter */
		0,																			/* tp_iternext */
		UnrealPyEmbedImporter_Methods,																			/* tp_methods */
		0,          																/* tp_members */
		0,																			/* tp_getset */
		0,																			/* tp_base */
		0,																			/* tp_dict */
		0,																			/* tp_descr_get */
		0,																			/* tp_descr_set */
		0,																			/* tp_dictoffset */
		(initproc)UnrealPyEmbedImporter_Init,									/* tp_init */
		PyType_GenericAlloc,																			/* tp_alloc */
		PyType_GenericNew												/* tp_new */
	};

	static PyMethodDef UnrealPyEmbedImporterModule_Methods[] = {
		{NULL}
	};

} // namespace UnrealPyEmbedExtImporter

#endif // WITH_PYTHON

void FUnrealPyEmbedExtImporter::Init()
{
#if WITH_PYTHON
	if (PyType_Ready(&UnrealPyEmbedExtImporter::UnrealPyEmbedImporter_Type) < 0)
	{
		return;
	}

	PyObject* Module = Py_InitModule3("_upy_ext_import", UnrealPyEmbedExtImporter::UnrealPyEmbedImporterModule_Methods, "Helper module for embedding Python in Unreal Editor");
	Py_INCREF(&UnrealPyEmbedExtImporter::UnrealPyEmbedImporter_Type);
	PyModule_AddObject(Module, "Importer", (PyObject*)&UnrealPyEmbedExtImporter::UnrealPyEmbedImporter_Type);
	
	PyObject* ImportModule = PyImport_ImportModule("_upy_ext_import");
	PyObject* Importer = PyObject_GetAttrString(Module, "Importer");
	Py_DECREF(ImportModule);
	if (Importer == nullptr)
	{
		UE_LOG(LogPython, Error, TEXT("Couldn't find _upy_ext_import.Importer"));
		return;
	}
	PyObject* PathHooks = PySys_GetObject("path_hooks");
	if (PathHooks == nullptr || !PyList_Check(PathHooks))
	{
		UE_LOG(LogPython, Error, TEXT("Unable to get sys.path_hooks, it it a list?"));
	}
	else
	{
		if (PyList_Append(PathHooks, Importer) != 0)
		{
			UE_LOG(LogPython, Error, TEXT("Can't append sys.path_hooks"));
		}
		Py_DECREF(Importer);
	}
	// clear python's importer cache
	PyObject* PathImporterCache = PySys_GetObject("path_importer_cache");
	if (PathImporterCache == nullptr || !PyDict_Check(PathImporterCache))
	{
		UE_LOG(LogPython, Error, TEXT("Unable to get sys.path_importer_cache, is it a dict?"))
	}
	else
	{
		PyDict_Clear(PathImporterCache);
	}

	// Populate dll directories we want to prepend path when importing
	UnrealPyEmbedExtImporter::DllDirectories.Add(FPaths::ConvertRelativePathToFull(FPaths::EnginePluginsDir() / "Developer" / "UnrealPyEmbed" / "Binaries" / FPlatformProcess::GetBinariesSubdirectory()));
	UnrealPyEmbedExtImporter::DllDirectories.Add(FPaths::ConvertRelativePathToFull(FPaths::EngineDir() / "Binaries" / FPlatformProcess::GetBinariesSubdirectory()));

#endif // WITH_PYTHON
}
