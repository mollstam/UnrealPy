from distutils.core import setup
import pychart.version

setup (name = "PyChart",
       version = pychart.version.version,
       description = "Python Chart Generator",
       author = "Yasushi Saito",
       author_email = "yasushi@cs.washington.edu",
       url = "http://www.hpl.hp.com/personal/Yasushi_Saito/pychart",
       license = "GPL",
       long_description = """
Pychart is a Python library for creating high-quality
charts in Postscript, PDF, PNG, and SVG. 
It produces line plots, bar plots, range-fill plots, and pie
charts.""",
       packages = ['pychart', 'pychart.afm']
      )
