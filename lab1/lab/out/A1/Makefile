FILES=A1.fsa A1bin.fsa A1opt.fsa syms.syms

compile: A1.fsa syms.syms
	fstcompile --acceptor --isymbols=syms.syms $< A1bin.fsa
	fstcompile --acceptor --isymbols=syms.syms $< | \
	fstrmepsilon | fstdeterminize | fstminimize > A1opt.fsa

clean:
	rm $(FILES)
