SUBDIRS=doc demos PyChart

dist:
	python setup.py sdist

clean:
	rm -f *~
	-for dir in $(SUBDIRS); do $(MAKE) -C$$dir clean; done

WWW_DIR=$(HOME)/gna/pychart
install:
	#rm -f $(WWW_DIR)/doc/*
	#rm -f $(WWW_DIR)/examples/*
	cp -r doc/pychart/* $(WWW_DIR)/doc
	cp -r doc/examples/* $(WWW_DIR)/examples
	baz changelog >$(WWW_DIR)/ChangeLog

copy:
	rm -rf ,,download
	mkdir ,,download
	(cd doc; tar czf ../,,download/pychart-doc.tar.gz pychart)
	cp dist/PyChart-1.38.tar.gz ,,download
	rsync --delete -avr --rsh="ssh" ,,download/* ysaito@download.gna.org:/upload/pychart
