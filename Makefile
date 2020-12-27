all: kodos/kodos_rc.py
	$(MAKE) -C kodos
	pylupdate5 kodos.pro
	$(MAKE) -C translations

clean:
	$(RM) -fv kodos/kodos_rc.py
	$(MAKE) clean -C kodos

kodos/kodos_rc.py: kodos.qrc
	pyrcc5 -o $@ $<
