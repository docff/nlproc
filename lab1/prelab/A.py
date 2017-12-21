# -*- coding: utf-8 -*-

import codecs, sys

vocab_gr = "data/el_caps_noaccent.dict"
vocab_en = "data/en_caps_noaccent.dict"

A1 = "A1.fsa"
dirA1 = "out/A1/"

A2 = "A2.fsa"
dirA2 = "out/A2/"

isyms = "isyms.syms"

def main(flag='A1', sample=True):
	if flag == 'A1': dirA = dirA1; A = A1; vocab = vocab_gr
	else: dirA = dirA2; A = A2; vocab = vocab_en

	content = readContent(vocab)
	if sample: content = content[:80]
	syms = createFsa(content, dirA + A)
	symstxt(syms, dirA + isyms)

def createFsa(content, file='generic.fsa'):
	syms = set()
	fd = codecs.open(file, 'w', 'utf8')

	state = 1
	for word in content:
		state += 1
		fd.write("0\t" + str(state) + "\teps\n")
		for lett in word:
			if len(lett) > 1:
				syms.add(lett[0]); syms.add(lett[1])
			else: syms.add(lett)
			fd.write(str(state) +  "\t" + str(state + 1) + 
				"\t" + lett + "\n")
			state += 1
		fd.write(str(state) + "\t1\teps\n")
	fd.write("1\n")
	fd.close()
	return syms

def readContent (file):
	fd = codecs.open(file, 'r', 'utf8')
	content = fd.read().split()
	fd.close()
	return content

def symstxt(syms, file='syms.syms'):
	fd = codecs.open(file, 'w', 'utf8')
	fd.write("eps\t0\n")
	for sym in syms: fd.write(sym + '\t' + str(ord(sym)) + '\n')
	fd.close()

def usage():
	print "Wrong Usage!\n"
	print "Usage: python " + py + " '<fst>' <sample(True/False)>"

if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) != 2 or len(args[0]) == 0 or len(args[1]) == 0: usage(sys.argv[0])
	else: main(args[0], bool(args[1]))