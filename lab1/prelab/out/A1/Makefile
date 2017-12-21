PDFmin=A1min.pdf
PDF=A1.pdf
SYMS=isyms.syms
FSA=A1.fsa
OPT=A1opt.fsa
BIN=A1bin.fsa
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