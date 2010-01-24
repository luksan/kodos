all: modules/kodos_rc.py
	$(MAKE) -C modules
	pylupdate4 kodos.pro
	$(MAKE) -C translations

modules/kodos_rc.py: kodos.qrc
	pyrcc4 -o $@ $<
