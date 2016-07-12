# Much of this makefile is nicked from RapidFit and slimmed down considerably
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
ifeq ($(USER), gizdov)
	ROOTCFLAGS = -L$(ROOTSYS)/lib/root $(shell $(ROOTSYS)/bin/root-config --cflags | awk -F "-I" '{print $$1" -isystem"$$2}' )
endif
ROOTLIBS   = -L$(ROOTSYS)/lib $(shell $(ROOTSYS)/bin/root-config --libs)
ifeq ($(USER), gizdov)
	ROOTLIBS   = -L$(ROOTSYS)/lib/root $(shell $(ROOTSYS)/bin/root-config --libs)
endif
EXTRA_ROOTLIBS=-lRooFit -lRooStats -lRooFitCore

# Extensions
SRCEXT     = cpp
HDREXT     = h
OBJEXT     = o
LIBEXT     = so

# Directories
SRCDIR     = src
HDRDIR     = include
OBJDIR     = build
LIBDIR     = lib

# Get files and make list of objects and libraries
SRCS      := $(shell find $(SRCDIR) -name '*.$(SRCEXT)')
HDRS      := $(shell find $(HDRDIR) -name '*.$(HDREXT)')
OBJS      := $(patsubst $(SRCDIR)/%.$(SRCEXT),$(OBJDIR)/%.$(OBJEXT),$(SRCS))
LIBS      := $(patsubst $(SRCDIR)/%.$(SRCEXT),$(LIBDIR)/lib%.$(LIBEXT),$(SRCS))

# Where the output is
OUTPUT     = $(OBJDIR)/*.$(OBJEXT) $(LIBDIR)/*.$(LIBEXT)

# Compiler flags
CXXFLAGS   = -Wall -Werror -fPIC -std=c++11 -I$(HDRDIR) $(ROOTCFLAGS)
LIBFLAGS   = -L$(LIBDIR) $(ROOTLIBS) $(EXTRA_ROOTLIBS)

# Make the libraries
all : dir_struct $(LIBS)
# Make object files
objects : $(OBJS)
# Build libraries
$(LIBDIR)/lib%.$(LIBEXT) : $(OBJDIR)/%.$(OBJEXT)
	$(CC) -shared $< -o $@ $(LIBFLAGS)
# Build objects
$(OBJDIR)/%.$(OBJEXT) : $(SRCDIR)/%.$(SRCEXT)
	$(CC) $(CXXFLAGS) -c $< -o $@
# make sure dirs exist
dir_struct:
	@mkdir -p build lib
# Remove all the output
clean :
	$(RM) $(OUTPUT)
.PHONY : all objects dir_struct clean
