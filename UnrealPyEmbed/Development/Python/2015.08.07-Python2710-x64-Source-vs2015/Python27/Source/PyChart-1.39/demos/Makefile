# Works only for gmake.
#
# Just typing "make" creates all eps, pdf, color eps, color pdf files.
#
#

SAMPLEFILES=$(shell python ./list_sources.py)
PSFILES=$(SAMPLEFILES:.py=.eps)
PDFFILES=$(SAMPLEFILES:.py=.pdf)
COLOR_PSFILES=$(SAMPLEFILES:.py=-c.eps)
COLOR_PDFFILES=$(SAMPLEFILES:.py=-c.pdf)
COLOR_PNGFILES=$(SAMPLEFILES:.py=-c.png)
PNGFILES=$(SAMPLEFILES:.py=.png)
SVGFILES=$(SAMPLEFILES:.py=.svg)

all: $(PSFILES) $(PDFFILES) $(COLOR_PSFILES) $(COLOR_PDFFILES) $(COLOR_PNGFILES)

ps: $(PSFILES)
pdf: $(PDFFILES)
svg: $(SVGFILES)
colorps: $(COLOR_PSFILES)
colorpdf:    $(COLOR_PDFFILES)
png: $(PNGFILES)
colorpng: $(COLOR_PNGFILES)

regression: all
	for psfile in *.eps; do echo $$psfile; ps2ps $$psfile /dev/null; done

clean:
	rm -f *.eps *~ *.pyc *.ps foo.* *.bak *.gif *.png *.pdf *.svg

PYTHON?=python
#PYTHON=jython
#PYTHON=python2 coverage.py -x

%.eps: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="output=$@" $(PYTHON) $*.py
%.pdf: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="output=$@" $(PYTHON) $*.py
%.svg: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="output=$@" $(PYTHON) $*.py

%-c.eps: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="output=$@ color=yes" $(PYTHON) $*.py
%-c.pdf: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="output=$@ color=yes" $(PYTHON) $*.py
%.png: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="scale=2 output=$@" $(PYTHON) $*.py
%-c.png: %.py
	PYTHONPATH=.. PYCHART_OPTIONS="scale=2 output=$@ color=yes" $(PYTHON) $*.py
