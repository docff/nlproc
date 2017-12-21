FILES=I.fst Ibin.fst syms.syms

compile: I.fst syms.syms
	fstcompile --isymbols=syms.syms --osymbols=syms.syms $< Ibin.fst

clean:
	rm $(FILES)
