SUBDIRS = common analysis
SUBDIRSCLEAN = $(addsuffix .clean,$(SUBDIRS))

.PHONY: all subdirs $(SUBDIRS) $(SUBDIRSCLEAN) message clean

all: subdirs message

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

analysis: common

message:
	@echo '#########################################'
	@echo '############### COMPLETED ###############'
	@echo '#########################################'

clean: $(SUBDIRSCLEAN)

$(SUBDIRSCLEAN): %.clean:
	$(MAKE) -C $* clean