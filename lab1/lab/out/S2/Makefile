FILES=Ibin.fst Eopt.fst Iclos.fst S1.fst S2.fst

compile:
	cp ../I0/Ibin.fst .
	cp ../E/Eopt.fst .
	cp ../S1/S1.fst .
	
	fstclosure Ibin.fst Iclos.fst
	
	fstconcat S1.fst Eopt.fst S2.fst
	fstconcat S2.fst Iclos.fst S2.fst
	
	fstminimize --allow_nondet=true S2.fst S2.fst
	fstarcsort S2.fst S2.fst

clean:
	rm $(FILES)
