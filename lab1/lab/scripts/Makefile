run: A.py C.py fstG.py fstI.py fstE.py
	python fstG.py
	python fstI.py True 25
	python fstI.py all 0
	python C.py
	python fstE.py
	for p in A1 A2; \
	do \
		python $< $$p False; \
	done
