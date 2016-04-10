
#include "UnrealPyEmbed_PythonPrivatePCH.h"
#include "PythonInterpreter.h"
#include "Extensions/UnrealPyEmbed.h"

#if WITH_PYTHON
	#include "Python/Python.h"
#endif // WITH_PYTHON

/** This is a small guard class to handle the case of Python calling exit() during init */
namespace PythonExitGuard
{
	static bool InScope = false;
}
struct FPythonExitGuard
{
	FPythonExitGuard()
	{
		PythonExitGuard::InScope = true;
		int i = atexit(&FPythonExitGuard::AtExit);
		if (i != 0)
		{
			UE_LOG(LogPython, Fatal, TEXT("Unable to register atexit in FPythonExecContext"));
		}
	};

	~FPythonExitGuard()
	{
		PythonExitGuard::InScope = false;
	}

	static void AtExit()
	{
		if (PythonExitGuard::InScope)
		{
			// Python encountered a fatal error, check stderr for more information e.g. by running 'UE4Editor-Cmd.exe -stdout'
			// We cannot log here, probably since things are falling around us
			FPlatformMisc::DebugBreak();
		}
	}

};

FPythonInterpreter* FPythonInterpreter::Instance = nullptr;

FPythonInterpreter* FPythonInterpreter::Get()
{
	if (Instance == nullptr)
	{
		Instance = new FPythonInterpreter();
	}

	return Instance;
}


FPythonInterpreter::FPythonInterpreter()
{
#if WITH_PYTHON
	Py_IgnoreEnvironmentFlag = 1;
	{
		FPythonExitGuard ExecContext;
		Py_InitializeEx(0);
		FUnrealPyEmbed::Init();
	}
#endif //WITH_PYTHON
}

void FPythonInterpreter::Destroy()
{
#if WITH_PYTHON
	Py_Finalize();
#endif //WITH_PYTHON
	Instance = nullptr;
	delete this;
}

void FPythonInterpreter::RunString(const FString& String)
{
	UE_LOG(LogPython, Log, TEXT(">>> %s"), *String);
#if WITH_PYTHON
	PyRun_SimpleString(TCHAR_TO_ANSI(*String));
#endif // WITH_PYTHON
}

void FPythonInterpreter::RunFile(const FString& Path)
{
#if WITH_PYTHON
	PyObject* PyFileObject = PyFile_FromString(TCHAR_TO_ANSI(*Path), "r");
	PyRun_SimpleFileEx(PyFile_AsFile(PyFileObject), TCHAR_TO_ANSI(*Path), 1);
#endif // WITH_PYTHON
}
