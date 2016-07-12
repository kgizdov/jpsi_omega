# Location of "common" libraries from ssh://git@gitlab.cern.ch:7999/admorris/common.git
COMMONDIR  = $(PWD)/../common
# Compiler and shell
CC         = g++
SHELL      = /bin/bash
RM         = rm -f
ROOTSYS    = /usr/local
ifeq ($(USER), gizdov)
	ROOTSYS = /usr
endif

# Include ROOT files as system headers as they're NOT standards complient and we do not want to waste time fixing them!
# ROOT has some broken backwards compatability for OSX so won't claim to be a set of system headers
ROOTCFLAGS = -L$(ROOTSYS)/lib $(shell $(ROOTSYS)/bin/root-config --cflags | awk -F "-I" '{print $$1" -isystem"$$2}' )
ROOTLIBS   = -L$(ROOTSYS)/lib $(shell $(ROOTSYS)/bin/root-config --libs)
EXTRA_ROOTLIBS=-lRooFit -lRooStats -lRooFitCore

# Extensions
SRCEXT     = cpp
HDREXT     = h
OBJEXT     = o
LIBEXT     = so

# Directories
PWD        = $(shell pwd)
SRCDIR     = src
BINSRCDIR  = app
LIBSRCDIR  = lib
HDRDIR     = include
OBJDIR     = build
LIBDIR     = $(PWD)/lib
BINDIR     = bin
COMHDRDIR  = $(COMMONDIR)/include
COMLIBDIR  = $(COMMONDIR)/lib
# Get files and make list of objects and libraries
# BINSRCS   := $(shell find $(SRCDIR)/$(BINSRCDIR) -name '*.$(SRCEXT)')
BINSRCS   := $(shell find $(SRCDIR) -name '*.$(SRCEXT)')
# LIBSRCS   := $(shell find $(SRCDIR)/$(LIBSRCDIR) -name '*.$(SRCEXT)')
LIBSRCS   := $(shell find $(SRCDIR) -name '*.$(SRCEXT)')
HDRS      := $(shell find $(HDRDIR) -name '*.$(HDREXT)')
# LIBS      := $(patsubst $(SRCDIR)/$(LIBSRCDIR)/%.$(SRCEXT), $(LIBDIR)/lib%.$(LIBEXT), $(LIBSRCS))
LIBS      := $(patsubst $(SRCDIR)/%.$(SRCEXT), $(LIBDIR)/lib%.$(LIBEXT), $(LIBSRCS))
# BINS      := $(patsubst $(SRCDIR)/$(BINSRCDIR)/%.$(SRCEXT), $(BINDIR)/%, $(BINSRCS))
BINS      := $(patsubst $(SRCDIR)/%.$(SRCEXT), $(BINDIR)/%, $(BINSRCS))
COMLIBS   := $(shell find $(COMLIBDIR) -name '*.$(LIBEXT)')

# Where the output is
OUTPUT     = $(OBJDIR)/*/*.$(OBJEXT) $(OBJDIR)/*.$(OBJEXT) $(LIBDIR)/*.$(LIBEXT) $(BINDIR)/*

# Compiler flags
CXXFLAGS   = -Wall -fPIC -I$(HDRDIR) -I$(COMHDRDIR) $(ROOTCFLAGS) -std=c++11
LIBFLAGS   = -L$(LIBDIR) -L$(COMLIBDIR) $(ROOTLIBS) -lboost_program_options $(EXTRA_ROOTLIBS)

## THIS WORKS
# g++ -I../common/include -L../common/lib `root-config --cflags` `root-config --libs` src/compareBranch.cpp -o test -lRooFit -lRooStats -lRooFitCore -lboost_program_options -lplotmaker -lGetTree

all : dir_struct $(BINS) $(HDRS) Makefile
libs : $(LIBS)
# Build binaries
# $(BINDIR)/% : $(OBJDIR)/$(BINSRCDIR)/%.$(OBJEXT) $(LIBS)
$(BINDIR)/% : $(OBJDIR)/%.$(OBJEXT) $(LIBS)
	# $(CC) $(LIBFLAGS) $^ $(LIBS) $(COMLIBS) -o $@
	$(CC) $^ -o $@ $(LIBFLAGS) $(COMLIBS) $(LIBS)
# Build libraries
# $(LIBDIR)/lib%.$(LIBEXT) : $(OBJDIR)/$(LIBSRCDIR)/%.$(OBJEXT)
$(LIBDIR)/lib%.$(LIBEXT) : $(OBJDIR)/%.$(OBJEXT)
	$(CC) -shared $< -o $@
# Build objects
$(OBJDIR)/%.$(OBJEXT) : $(SRCDIR)/%.$(SRCEXT)
	$(CC) $(CXXFLAGS) -c $< -o $@
# make sure dirs exist
dir_struct:
	@mkdir -p bin build lib include
# Remove all the output
clean :
	$(RM) $(OUTPUT)
