RULES=convertions.txt rules.txt
FST=G.fst
BIN=Gbin.fst
PDF=G.pdf
SYMS=isyms.syms osyms.syms
FILES=$(PDF) $(BIN) $(FST) $(SYMS) $(RULES)

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