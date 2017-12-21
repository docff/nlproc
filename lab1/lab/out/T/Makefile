FILES=Gbin.fst Ibin.fst A1opt.fsa A2opt.fsa GI.fst A12.fsa T.fst

compile:
	cp ../G/Gbin.fst .
	cp ../I/Ibin.fst .
	cp ../A1/A1opt.fsa .
	cp ../A2/A2opt.fsa .

	fstunion Gbin.fst Ibin.fst GI.fst
	fstunion A1opt.fsa A2opt.fsa A12.fsa

	fstclosure GI.fst GI.fst
	
	fstarcsort GI.fst GI.fst
	fstarcsort A12.fsa A12.fsa

	fstminimize --allow_nondet=true GI.fst GI.fst
	fstminimize --allow_nondet=true A12.fsa A12.fsa

	fstcompose GI.fst A12.fsa T.fst

clean:
	rm $(FILES)
