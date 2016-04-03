
#pragma once

class FPythonInterpreter
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
