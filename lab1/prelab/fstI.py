# -*- coding: utf-8 -*-
import codecs

dirI = "out/I/"
fstI = "I.fst"

syms_in = "isyms.syms"
syms_out = "osyms.syms"

def main():
	en_ab = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
	inf_weight = 30
	createIdFst(en_ab, inf_weight, dirI + fstI)

	symstxt(en_ab, dirI + syms_in)
	symstxt(en_ab, dirI + syms_out)

def createIdFst(syms, weight=30, file='id.fst'):
	fd = codecs.open(file, 'w', 'utf8')
	for sym in syms: fd.write('0\t0\t' + sym + '\t' + sym + '\t' + str(weight) + '\n')
	fd.write("0\n")
	fd.close()

def symstxt(syms, file='syms.syms'):
	fd = codecs.open(file, 'w', 'utf8')
	fd.write("eps\t0\n")
	for sym in syms: fd.write(sym + '\t' + str(ord(sym)) + '\n')
	fd.close()

if __name__ == "__main__":
	main()