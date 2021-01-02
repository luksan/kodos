all: kodos/kodos_rc.py
	$(MAKE) -C kodos
	pylupdate4 kodos.pro
	$(MAKE) -C translations

clean:
	$(RM) -fv kodos/kodos_rc.py
	$(MAKE) clean -C kodos

kodos/kodos_rc.py: kodos.qrc
	pyrcc4 -py3 -o $@ $<
