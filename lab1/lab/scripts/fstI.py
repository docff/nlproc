# -*- coding: utf-8 -*-
import codecs, sys

dirI = "../out/I/"
dirI0 = "../out/I0/"
fstI = "I.fst"

syms = "syms.syms"

en_ab = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
gr_ab = u"ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
all_ab = u"ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩABCDEFGHIJKLMNOPQRSTUWVXYZ"
def main(en='True', weight=25):
	if en == 'all':
		ab = all_ab
		dirO = dirI0
	elif en == 'False':
		ab = gr_ab
		dirO = dirI0
	else:
		ab = en_ab
		dirO = dirI

	createIdFst(ab, weight, dirO + fstI)
	symstxt(ab, dirO + syms)

def createIdFst(syms, weight=30, file='id.fst'):
	fd = codecs.open(file, 'w', 'utf8')
	for sym in syms: 
		fd.write('0\t1\t' + sym + '\t' + sym + '\t' + str(weight) + '\n')
	fd.write("1\n")
	fd.close()

def symstxt(syms, file='syms.syms'):
	fd = codecs.open(file, 'w', 'utf8')
	for sym in syms: fd.write(sym + '\t' + str(ord(sym)) + '\n')
	fd.close()

def usage(py):
	print "Wrong Usage!"
	print "Usage: python " + py + " 'language<False/Greek, True/English' weight<int>"

if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) != 2 or len(args[0]) == 0 or len(args[1]) == 0: usage(sys.argv[0])
	else:	main(args[0], args[1])
	main()