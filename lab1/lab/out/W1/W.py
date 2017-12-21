# -*- coding: utf-8 -*-
import codecs, subprocess, sys

test_wr = "../../data/test_wr.txt"
test_co = "../../data/test_co.txt"

W = "W.fsa"
dirW = "out/W1/"

output = "out_"

def main(S='S1'):
	subprocess.call(["make", "copy"])
	wr_content = readContent(test_wr)
	co_content = readContent(test_co)

	while '' in wr_content:
		wr_content.remove('')
	while '' in co_content:
		co_content.remove('')

	count = 0
	w_count = 0
	r_count = 0
	n_count = 0
	out = codecs.open(output + S + ".txt", "w", 'utf8')
	for word_wr, word_co in zip(wr_content, co_content):
		createFsa(word_wr, W)
		
		subprocess.call(["fstcompile",  "--acceptor", "--isymbols=syms.syms", "W.fsa", "Wacc.fsa"])
		subprocess.call(["fstcompose", "Wacc.fsa", S + ".fst", "WS.fst"])
		subprocess.call(["fstcompose", "WS.fst", "L.fst", "WSL.fst"])
		subprocess.call(["fstshortestpath", "WSL.fst", "transducer.fst"])
		subprocess.call(["fsttopsort", "transducer.fst", "transducer.fst"])
		word = subprocess.check_output(["farprintstrings", "--token_type=utf8", "transducer.fst"])
		word = word.replace('\n', '')
		word = word.replace('\0', '')
		word = word.replace('0', '')
		count += 1
		
		v = ''
		if word == '':
			n_count += 1
			v = str('UNMATCHED')
		elif word.decode('utf8') == word_co:
			r_count += 1
			v = str('CORRECT')
		else:
			w_count += 1
			v = str('WRONG')

		out.write(word_wr + " : " + word_co + " \n-> \t" + word.decode('utf8') + " : " + v + "\n")
	right = 100 * float(r_count) / count; wrong = 100 * float(w_count) / count; unmatched = 100 * float(n_count) / count	
	out.write("\nright: %.2f%% wrong: %.2f%% unmatched: %.2f%%" % (right, wrong, unmatched))
	out.close()


def createFsa(content, file='generic.fsa'):
	fd = codecs.open(file, 'w', 'utf8')

	state = 0
	for lett in content:
		fd.write(str(state) + "\t" + str(state + 1) + 
			"\t" + lett + "\n")
		state += 1
	fd.write(str(state) + "\n")
	fd.close()

def readContent(file):
	fd = codecs.open(file, 'r', 'utf8')
	content = fd.read().split()
	fd.close()
	return content

def usage(py):
	print "Wrong Usage!"
	print "Usage: python " + py + " S1/S2"

if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) !=1: usage(sys.argv[0])
	main(args[0])