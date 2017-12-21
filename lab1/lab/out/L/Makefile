FILES=A12.fsa L.fst

compile:
	cp ../T/A12.fsa .
	
	fstminimize A12.fsa | fstarcsort > L.fst

clean:
	rm $(FILES)
