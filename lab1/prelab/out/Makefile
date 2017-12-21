SUBDIRS=G I A1 A2

draw:
	for p in $(SUBDIRS); do \
		$(MAKE) -C $$p draw; \
	done

compile:
	for p in $(SUBDIRS); do \
		$(MAKE) -C $$p compile; \
	done

clean:
	for p in $(SUBDIRS); do \
		$(MAKE) -C $$p clean; \
	done