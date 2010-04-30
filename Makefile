all: modules/kodos_rc.py
	$(MAKE) -C modules

clean:
	$(RM) -fv modules/kodos_rc.py
	$(MAKE) clean -C modules

modules/kodos_rc.py: kodos.qrc
	pyrcc4 -o $@ $<
