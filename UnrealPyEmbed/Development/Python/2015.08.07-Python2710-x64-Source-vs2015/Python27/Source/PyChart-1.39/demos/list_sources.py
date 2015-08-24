import glob
import os.path

def list_sources(dir):
    """Return the list of Python source files under demos/ directory.
    Parameter "dir" specifies the locatino of the demos/ directory."""
    
    l = glob.glob(dir + "/*.py")
    r = []
    for path in l:
        basename = os.path.basename(path)
        if basename in ("tocslib.py", "twographs.py", "chartdemo.py",
                        "list_sources.py"):
            continue
        if basename.startswith(",,"):
            # tla/baz temp file.
            continue
        r.append(basename)
    r.sort()        
    return r

if __name__ == '__main__':
    # When invoked from the cmdline, just print the list of files to
    # the stdout.
    r = list_sources(".")
    print " ".join(r)

