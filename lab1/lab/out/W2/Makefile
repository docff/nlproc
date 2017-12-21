FILES=W.fsa GI.fst L.fst S1.fst S2.fst Wacc.fsa WT.fst WTS.fst transducer.fst out_S1.txt out_S2.txt syms.syms

copy:
	cp ../E/syms.syms .
	cp ../T/GI.fst .
	cp ../L/L.fst .
	cp ../S1/S1.fst .
	cp ../S2/S2.fst .

v1:
	python W.py S1

v2:
	python W.py S2

word:
	fstcompile --acceptor --isymbols=syms.syms W.fsa | fstarcsort > Wacc.fsa
	fstcompose Wacc.fsa T.fst | fstrmepsilon | fstshortestpath > transducer.fst
	
clean:
	rm $(FILES)
