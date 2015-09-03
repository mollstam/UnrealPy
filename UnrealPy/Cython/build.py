
from subprocess import call
import os

pch = "Private/UnrealPyPrivatePCH.h"

def process_output(file):
	lines = []
	with open(file) as fin:
		for line in fin:
			lines.extend([line])

	with open(file, "w") as fout:
		fout.write("\n#include \"{0}\"\n\n".format(pch))
		for line in lines:
			fout.write(line)

## ## ##

build_dir_base = 'F:\\UnrealEngine\\Engine\\Source\\Editor\\UnrealPy\\Private\\'

pyx_files = []

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".pyx"):
			file_path = os.path.join(root, file)
			build_dir = os.path.join(build_dir_base, root)
			file_name, file_ext = os.path.splitext(file)
			build_file = os.path.join(build_dir, file_name) + ".cpp"
			if not os.path.exists(build_dir):
				os.makedirs(build_dir)
			call(['cython', '--cplus', '-o', build_file, file_path])
			process_output(build_file)
