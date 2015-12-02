# UnrealPy #

UnrealPy is mainly two parts: exposing Unreal Editor functionality to Python through extensions, and exposing Python to Unreal Editor through an embedded interpreter, thus closing the loop and the idea is to allow users to script their editor in Python and execute from within the editor but at the same time making that glue available for folks who want to do Python stuff without running the editor -- in a more headless fashion.

## Current Status ##

This project is still currently in the setup phase and it probably isn't that useful right now. The embedded interpreter in the editor is there, but it's only standalone vanilla Python, so not very useful. As for the extensions, I've started with the test framework to lift over Unreal datatypes into Cython, the progress/planning is somewhat available in at [the roadmap on the wiki](https://github.com/mollstam/UnrealPy/wiki/Roadmap).
