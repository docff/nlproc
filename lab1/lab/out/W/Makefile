FILES=W.fsa T.fst Wacc.fsa WT.fst transducer.fst syms.syms out.txt

run:
	cp ../E/syms.syms .
	cp ../T/T.fst .
	python W.py

word:
	fstcompile --acceptor --isymbols=syms.syms W.fsa | fstarcsort > Wacc.fsa
	fstcompose Wacc.fsa T.fst | fstrmepsilon | fstshortestpath > transducer.fst
	
clean:
	rm $(FILES)
