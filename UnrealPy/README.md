unrealpy is a Python API for the Unreal Engine 4 Editor to manipulate UAssets, EdGraphs, and more in a scripted manner.

Currently *very rough* developer version which isn't fit to clone for anyone. :)

## Structure & Setup ##

The custom command `build_ue` added to `setup.py` will scan for Cython modules and generate their C++ code. UE modules are generated for the generated code which is compiled and linked by UBT. The command will also extract these build artifacts and stage them properly in the UnrealPy Python module, ready to use. That's the theory anyway.

_If you're looking for a step-by-step of how to get this into UE you'll have to come back, as the development loop isn't really closed yet. Still have some wrestling with tox. /Tobias (Dec 2nd 2015)_
