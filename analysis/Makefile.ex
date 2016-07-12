CPP = g++
CPPFLAGS = -I .
CPPLIBS =
ROOTFLAGS = `root-config --cflags`
ROOTLIBS = `root-config --libs`

all: dir_struct

dir_struct:
	@mkdir -p bin lib

clean:
	@rm -f ./lib/* ./bin/*

.PHONY: all dir_struct clean
