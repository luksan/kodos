
all: *.py
	$(MAKE) $$(echo *ui | sed -e 's/ui/py/g')

clean:
	$(RM) -vf *BA.py

%.py: %.ui
	pyuic4 -w -o $*.py $<
