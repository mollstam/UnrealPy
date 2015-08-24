# Upgrading Python Versions #

Right now there's a custom Python 2.7.10 in there,
which sources are in the `Development` directory (in Plugin root).
It's linked statically and contains some minor code changes to
compile and link properly in the UE4 environment.

If you want to upgrade the Python version you'll have to
get the binaries and headers and put them in their proper location
(Include/ and Lib/ in this folder). You could go with the dynamic libraries
if you wanted to I guess, but you're on your own. :]

`UnrealPyEmbed_Python\UnrealPyEmbed_Python.Build.cs` includes everything
you need to change to point to another Python lib.

Have fun.

:koala:
