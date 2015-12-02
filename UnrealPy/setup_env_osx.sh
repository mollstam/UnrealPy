#! /bin/bash

if [ -z "$UNREAL_PATH" ]; then
	echo "Error: environment variable UNREAL_PATH must be set to point to your UE4 root"
	exit 1
fi
if [ ! -d "$UNREAL_PATH" ]; then
	echo "Error: UNREAL_PATH set, but unable to find directory '$UNREAL_PATH'"
	exit 1
fi

# Add the built Debug libraries to the search path of linker
export DYLD_LIBRARY_PATH=$UNREAL_PATH/Engine/Binaries/Mac/UE4Editor-Mac-Debug.app/Contents/MacOS
