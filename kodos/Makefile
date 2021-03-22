
all: *.py
	$(MAKE) $$(echo *ui | sed -e 's/ui/py/g')

clean:
	$(RM) -vf *BA.py
	$(RM) -vf *.pyc

%.py: %.ui
	pyuic5 --from-imports -o $*.py $<
