FILES=L.fst S1.fst S2.fst L.fst W.fsa WS.fst WSL.fst Wacc.fsa transducer.fst syms.syms out_S1.txt out_S2.txt

copy:
	cp ../L/L.fst .
	cp ../S1/S1.fst .
	cp ../S2/S2.fst .
	cp ../E/syms.syms .

v1:
	python W.py S1

v2:
	python W.py S2
	
clean:
	rm $(FILES)
