PDFmin=A2min.pdf
PDF=A2.pdf
SYMS=isyms.syms
FSA=A2.fsa
OPT=A2opt.fsa
BIN=A2bin.fsa
FILES=$(PDFmin) $(PDF) $(SYMS) $(FSA) $(OPT) $(BIN)

$(FSA):

$(SYMS):

$(OPT):

compile: $(FSA) $(SYMS)
	fstcompile --acceptor --isymbols=isyms.syms $< | \
	fstrmepsilon | fstdeterminize | fstminimize > $(OPT)
	fstcompile --acceptor --isymbols=isyms.syms $< $(BIN)

draw: $(OPT) $(SYMS)
	fstdraw --acceptor --isymbols=isyms.syms $(BIN) | dot -Tpdf > $(PDF)
	fstdraw --acceptor --isymbols=isyms.syms $< | dot -Tpdf > $(PDFmin)

clean:
	rm $(FILES)