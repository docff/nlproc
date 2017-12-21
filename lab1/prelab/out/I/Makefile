FST=I.fst
BIN=Ibin.fst
PDF=I.pdf
SYMS=isyms.syms osyms.syms
FILES=$(PDF) $(BIN) $(FST) $(SYMS)

$(FST):

$(SYMS):

$(BIN):

compile: $(FST) $(SYMS)
	fstcompile --isymbols=isyms.syms --osymbols=osyms.syms $< $(BIN)

draw: $(BIN)
	fstdraw --isymbols=isyms.syms --osymbols=osyms.syms $(BIN) | \
	dot -Tpdf > $(PDF)

clean:
	rm $(FILES)