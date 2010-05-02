
all: *.py
	$(MAKE) $$(echo *ui | sed -e 's/ui/py/g')

clean:
	$(RM) -vf *BA.py
	$(RM) -vf *BA.pyc

%.py: %.ui
	pyuic4 -w -o $*.py $<
