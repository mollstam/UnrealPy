PYCHART_DIR=..
PYTHON_DOC_DIR=$(HOME)/Python-2.4.2/Doc
all: pychart examples

pychart: pychart.tex
	$(PYTHON_DOC_DIR)/tools/mkhowto --html pychart.tex
	$(MAKE) markup

pychart.pdf: pychart.tex
	$(PYTHON_DOC_DIR)/tools/mkhowto --pdf pychart.tex

pychart.tex: template.tex doc.py
	make -C$(PYCHART_DIR)/demos colorpng
	PYTHONPATH=$(PYCHART_DIR):$(PYCHART_DIR)/demos python doc.py --pychart-dir=$(PYCHART_DIR) template.tex >$@

markup:
	for f in pychart/*.html; do echo $$f; python markuphtml.py <$$f >foo.html; mv foo.html $$f; done

clean:
	rm -f *.pyc *~ *.html *.info tmp.texi *.png *.eps pychart.tex
	rm -rf examples html demos

demo:
	PYTHONPATH=..:../demos python demodoc.py
examples: examples.py $(wildcard ../demos/*.py)
	python examples.py

index.html: index.html $(GIFFILES)
	gtml index.gtml
