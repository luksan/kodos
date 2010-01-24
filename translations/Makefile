TSFILES := $(wildcard *.ts)

all: $(TSFILES)
	sed -i -e 's#\(filename="\)#\1../#g' $^
