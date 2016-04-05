
#pragma once

class UNREALPYEMBED_PYTHON_API FPythonInterpreter
{

public:

    static FPythonInterpreter* Get();

    void Destroy();

    void RunString(const FString& String);

private:

    FPythonInterpreter();

private:

    static FPythonInterpreter* Instance;

};
