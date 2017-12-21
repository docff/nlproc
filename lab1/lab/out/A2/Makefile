FILES=A2.fsa A2bin.fsa A2opt.fsa syms.syms

compile: A2.fsa syms.syms
	fstcompile --acceptor --isymbols=syms.syms $< A2bin.fsa
	fstcompile --acceptor --isymbols=syms.syms $< | \
	fstrmepsilon | fstdeterminize | fstminimize > A2opt.fsa
	
clean:
	rm $(FILES)
