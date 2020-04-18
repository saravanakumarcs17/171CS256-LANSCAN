all:

clean:

install:
	chmod 755 banner.py
	chmod 755 install.py
	chmod 755 run.sh
	chmod 755 lanscan.py
	mkdir -p $(DESTDIR)/opt/lanscan/
	mkdir -p $(DESTDIR)/usr/share/doc/lanscan/
	mkdir -p $(DESTDIR)/opt/lanscan/tools/
	mkdir -p $(DESTDIR)/usr/bin/
	cp banner.py $(DESTDIR)/opt/lanscan/
	cp install.py $(DESTDIR)/opt/lanscan/
	cp LICENSE $(DESTDIR)/opt/lanscan/
	cp Makefile $(DESTDIR)/opt/lanscan/
	cp README.md $(DESTDIR)/opt/lanscan/
	cp README.md $(DESTDIR)/usr/share/doc/lanscan/
	cp run.sh $(DESTDIR)/opt/lanscan/
	cp run.sh $(DESTDIR)/usr/bin/
	cp lanscan.py $(DESTDIR)/opt/lanscan/
	cp -r tools $(DESTDIR)/opt/lanscan/
	

