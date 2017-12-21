import codecs, subprocess

test_en = "../../data/test_greng.txt"
test_gr = "../../data/test_gr.txt"

W = "W.fsa"
dirW = "out/W/"

output = "out.txt"
def main():
	gr_content = readContent(test_gr)
	en_content = readContent(test_en)

	while '' in gr_content:
		gr_content.remove('')
	while '' in en_content:
		en_content.remove('')

	count = 0
	r_count = 0
	en_to_gr = 0
	n_count = 0
	w_count = 0
	out = codecs.open(output, "w", 'utf8')
	for word_gr, word_en in zip(gr_content, en_content):
		createFsa(word_en, W)
		
		subprocess.call(["fstcompile",  "--acceptor", "--isymbols=syms.syms", "W.fsa", "Wacc.fsa"])
		subprocess.call(["fstarcsort", "Wacc.fsa", "Wacc.fsa"])
		subprocess.call(["fstcompose", "Wacc.fsa", "T.fst", "WT.fst"])
		subprocess.call(["fstshortestpath", "WT.fst", "transducer.fst"])
		word = subprocess.check_output(["farprintstrings", "--token_type=utf8", "transducer.fst"])
		word = word.replace('\n', '')
		word = word.replace('\0', '')
		word = word.replace('0', '')
		count += 1
		
		if word == '':
			n_count += 1
			v = str('UNMATCHED')
		elif word_gr == word_en:
			if word.decode('utf8') == word_gr:
				r_count += 1
				v = str('CORRECT')
			else:
				en_to_gr += 1
				v = str('WRONG CONVERTION')
		elif word.decode('utf8') == word_gr:
			r_count += 1
			v = str('CORRECT')
		else:
			w_count += 1
			v = str('WRONG')

		out.write(word_en + " : " + word_gr + " \n-> \t" + word.decode('utf8') + " : " + v + "\n")
	right = 100 * float(r_count) / count; wrong = 100 * float(w_count) / count
	unmatched = 100 * float(n_count) / count; w_conv = 100 * float(en_to_gr) / count
	out.write("\nright: %.2f%% wrong: %.2f%%\nwrong convertion to greek: %.2f%% unmatched: %.2f%% " % (right, wrong, w_conv, unmatched))
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

if __name__ == "__main__":
	main()