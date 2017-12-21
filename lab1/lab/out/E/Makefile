FILES=E.fst Ebin.fst Eopt.fst syms.syms

compile: E.fst syms.syms
	fstcompile --isymbols=syms.syms --osymbols=syms.syms $< Ebin.fst
	fstcompile --isymbols=syms.syms --osymbols=syms.syms $< | \
	fstrmepsilon | fstminimize --allow_nondet=true > Eopt.fst

clean:
	rm $(FILES)
