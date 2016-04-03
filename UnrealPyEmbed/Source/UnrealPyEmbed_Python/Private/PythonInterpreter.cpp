
#include "UnrealPyEmbed_PythonPrivatePCH.h"
#include "PythonInterpreter.h"
#include "Extensions/UnrealPyEmbed.h"

#if WITH_PYTHON
	#include "Python/Python.h"
#endif // WITH_PYTHON

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
	Py_InitializeEx(0);
	FUnrealPyEmbed::Init();
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
#if WITH_PYTHON
	PyRun_SimpleString(TCHAR_TO_ANSI(*String));
#endif // WITH_PYTHON
}

