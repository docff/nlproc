FILES=Ibin.fst Eopt.fst Iclos.fst S1.fst

compile:
	cp ../I0/Ibin.fst .
	cp ../E/Eopt.fst .
	
	fstclosure Ibin.fst Iclos.fst
	fstconcat Iclos.fst Eopt.fst S1.fst
	
	fstconcat S1.fst Iclos.fst S1.fst
	fstminimize --allow_nondet=true S1.fst S1.fst
	fstarcsort S1.fst S1.fst

clean:
	rm $(FILES)
