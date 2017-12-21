SUBDIRS=G I I0 A1 A2 T E S1 S2 L
SUBCLEANS=G I I0 A1 A2 T C E S1 S2 L W W1 W2

v1:
	$(MAKE) -C W run

v21:
	$(MAKE) -C W1 v1

v22:
	$(MAKE) -C W1 v2

v31:
	$(MAKE) -C W2 v1

v32:
	$(MAKE) -C W2 v2

compile:
	for p in $(SUBDIRS); do \
		$(MAKE) -C $$p compile; \
	done

clean:
	$(MAKE) -C C clean
	for p in $(SUBCLEANS); do \
		$(MAKE) -C $$p clean; \
	done
