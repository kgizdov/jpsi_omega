SUBDIRS = common analysis
SUBDIRSCLEAN=$(addsuffix .clean,$(SUBDIRS))

.PHONY: subdirs $(SUBDIRS) $(SUBDIRSCLEAN) clean

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

analysis: common

clean: $(SUBDIRSCLEAN)

$(SUBDIRSCLEAN): %.clean:
	$(MAKE) -C $* clean