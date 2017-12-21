FILES=G.fst Gbin.fst isyms.syms osyms.syms rules.txt convertions.txt

compile: G.fst isyms.syms osyms.syms
	fstcompile --isymbols=isyms.syms --osymbols=osyms.syms $< Gbin.fst

clean:
	rm $(FILES)
