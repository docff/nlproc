# -*- coding: utf-8 -*-
import codecs, sys

dirE = "../out/E/"
fstE = "E.fst"

rules = '../out/C/rules.txt'
syms = "syms.syms"

ab = u"ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
	createOneFst(ab, dirE + fstE)
	symstxt(ab, dirE + syms)

def createOneFst(syms, file='one.fst'):
	fd = codecs.open(rules, 'r', 'utf8')
	lines = fd.read()
	lines = lines.split()[:12]
	prob_i = float(lines[2]); prob_d = float(lines[5])
	prob_r = float(lines[8]); prob_e = float(lines[11])
	fd.close()

	fd = codecs.open(file, 'w', 'utf8')
	for sym in syms:
		fd.write('0\t1\t' + sym + '\t' + sym + '\t0\n')
	for sym in syms:
		fd.write('0\t1\teps\t' + sym + '\t' + str(prob_i) + '\n')
	for sym in syms:
		fd.write('0\t1\t' + sym + '\teps\t' + str(prob_d) + '\n')
	for sym in syms:
		for sym1 in syms:
			if sym1 != sym:
				fd.write('0\t1\t' + sym + '\t' + sym1 + '\t' + str(prob_r) + '\n')
	state = 2
	for sym in syms:
		for sym1 in syms:
			if sym1 != sym:
				fd.write('0\t' + str(state) + '\t' + sym + '\t' + sym1 + '\t' + str(prob_e) + '\n')
				fd.write(str(state) +'\t1\t' + sym1 + '\t' + sym + '\t0\n')
				state += 1
	fd.write('1')
	fd.close()

def createIdFst(syms, weight=30, file='id.fst'):
	fd = codecs.open(file, 'w', 'utf8')
	for sym in syms: 
		print sym
		fd.write('0\t0\t' + sym + '\t' + sym + '\t' + str(weight) + '\n')
	fd.write("0\n")
	fd.close()

def symstxt(syms, file='syms.syms'):
	fd = codecs.open(file, 'w', 'utf8')
	fd.write('eps\t0\n')
	for sym in syms: fd.write(sym + '\t' + str(ord(sym)) + '\n')
	fd.close()

def usage(py):
	print "Wrong Usage!"
	print "Usage: python " + py + " 'language<False/Greek, True/English' weight<int>"

if __name__ == "__main__":
	main()