# -*- coding: utf-8 -*-

import codecs, sys

vocab_gr = "../data/el_caps_noaccent.dict"
vocab_en = "../data/en_caps_noaccent.dict"

A1 = "A1.fsa"
dirA1 = "../out/A1/"

A2 = "A2.fsa"
dirA2 = "../out/A2/"

isyms="syms.syms"

def main(flag='A1', sample='False'):
	if flag == 'A1': dirA = dirA1; A = A1; vocab = vocab_gr
	else: dirA = dirA2; A = A2; vocab = vocab_en

	content = readContent(vocab)
	if sample == 'True': content = content[:80]
	syms = createFsa(content, dirA + A)
	symstxt(syms, dirA + isyms)

def createFsa(content, file='generic.fsa'):
	syms = set()
	fd = codecs.open(file, 'w', 'utf8')

	state = 2
	flag = 1
	for word in content:
		flag1 = 1
		for lett in word:
			if flag and dirA1 + A1 == file:
				flag = 0
				continue;
			if len(lett) > 1:
				syms.add(lett[0]); syms.add(lett[1])
			else: syms.add(lett)
			if flag1:
				flag1 = 0
				fd.write("0\t" + str(state) + "\t" + lett + "\n")
			else:
				fd.write(str(state - 1) +  "\t" + str(state) + 
					"\t" + lett + "\n")
			state += 1
		fd.write(str(state - 1) + "\t1\teps\n")
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

def usage(py):
	print "Wrong Usage!"
	print "Usage: python " + py + " '<fst>' <sample(True/False)>"

if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) != 2 or len(args[0]) == 0 or len(args[1]) == 0: usage(sys.argv[0])
	else:	main(args[0], args[1])