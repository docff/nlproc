PY=A.py
EXE=fstG.py fstI.py
SUBDIRS=out
VOC='A1' 'A2'

$(PY):

$(VOC):

$(EXE):

run: $(PY) $(VOC) $(EXE)
	for p in $(EXE); do \
		python $$p; \
	done
	for p in $(VOC); do \
		python $< $$p 'False'; \
	done

sample: $(PY) $(VOC) $(EXE)
	for p in $(EXE); do \
		python $$p; \
	done
	for p in $(VOC); do \
		python $< $$p 'True'; \
	done

compile:
	$(MAKE) -C $(SUBDIRS) compile

draw:
	$(MAKE) -C $(SUBDIRS) draw

clean:
	$(MAKE) -C $(SUBDIRS) clean