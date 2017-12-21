# -*- coding: utf-8 -*-

import codecs, math

test_gr = "data/train_gr.txt"
test_greng = "data/train_greng.txt"

rulesf = "rules.txt"
convertions = "convertions.txt"

dirG = "out/G/"
fstG = "G.fst"

syms_gr = "osyms.syms"
syms_en = "isyms.syms"

sp_ch_gr =  {u'ΛΛ' : ['L'], u'ΜΠ': ['B'], u'ΑΙ' : ['E'], u'ΟΙ' : ['I'], u'ΕΙ' : ['I'], u'ΟΥ' : ['U'], u'ΒΒ' : ['V'], u'ΓΚ' : ['G'], u'ΝΤ' : ['D'], u'Ψ' : ['PS'], u'Θ' : ['TH'], u'Ξ' : ['KS']}
sp_ch_en =  {'L':[u'ΛΛ'] , 'B' :[u'ΜΠ'], 'E':[u'ΑΙ'] , 'I':[u'ΟΙ'], 'I':[u'ΕΙ'], 'U':[u'ΟΥ'], 'V':[u'ΒΒ'], 'G':[u'ΓΚ'], 'D':[u'ΝΤ'], 'PS':[u'Ψ'], 'TH':[u'Θ'], 'KS':[u'Ξ']}

def main():
	greek = readContent(test_gr)
	greng = readContent(test_greng)
	(rules, gr_syms, en_syms, n) = matchingRules(greek, greng, dirG + convertions, True)
	
	matchingProbs(rules, n, dirG + rulesf)
	createFst(rules, n, gr_syms, en_syms, dirG + fstG)

	symstxt(gr_syms, dirG + syms_gr)
	symstxt(en_syms, dirG + syms_en)

def readContent (file):
	fd = codecs.open(file, 'r', 'utf8')
	content = fd.read().split()
	fd.close()
	return content

def matchingRules(greek, greng, file='convertions.txt', out=False):
	content = filter(lambda (i, j): i != j , zip(greek, greng))
	if out:
		fd = codecs.open(file, 'w', 'utf8')

	n = 0; rules = dict()
	gr_syms = set(); en_syms = set()
	for gr_word, en_word in content:
		last_greek = last_greng = 1
		gr_index = en_index = 0
		gr_length = len(gr_word)
		en_length = len(en_word)
		
		if gr_length == en_length:
			for index in range(gr_length):
				en_key = en_word[index]; gr_key = gr_word[index]
				if en_key in rules.keys():
					if gr_key in rules[en_key].keys(): rules[en_key][gr_key] += 1
					else: rules[en_key][gr_key] = 1
				else:
					rules[en_key] = dict()
					rules[en_key][gr_key] = 1

				n += 1
				gr_key = gr_word[index]; gr_syms.add(gr_key)
				en_key = en_word[index]; en_syms.add(en_key)
				if out: fd.write(en_key + " -> " + gr_word[index] + "\n")
		else:
			while gr_index < gr_length and en_index < en_length:
				if gr_index >= gr_length - 1: last_greek = 0
				if en_index >= en_length - 1: last_greng = 0

				if last_greek and gr_word[gr_index] + gr_word[gr_index + 1] in sp_ch_gr.keys() and en_word[en_index] in sp_ch_gr[gr_word[gr_index] + gr_word[gr_index + 1]]:
					en_key = en_word[en_index]; gr_key = gr_word[gr_index] + gr_word[gr_index + 1]; gr_index += 1
				elif last_greng and en_word[en_index] + en_word[en_index + 1] in sp_ch_en.keys() and gr_word[gr_index] in sp_ch_en[en_word[en_index] + en_word[en_index + 1]]:
					en_key = en_word[en_index] + en_word[en_index + 1]; gr_key = gr_word[gr_index]; en_index += 1
				else: en_key = en_word[en_index]; gr_key = gr_word[gr_index]

				if en_key in rules.keys():
					if gr_key in rules[en_key].keys(): rules[en_key][gr_key] += 1
					else: rules[en_key][gr_key] = 1
				else:
					rules[en_key] = dict()
					rules[en_key][gr_key] = 1

				n += 1; gr_index += 1;	en_index += 1
				if len(gr_key) > 1:
					gr_syms.add(gr_key[0]); gr_syms.add(gr_key[1])
				else: gr_syms.add(gr_key)
				if len(en_key) > 1:
					en_syms.add(en_key[0]); en_syms.add(en_key[1])
				else: en_syms.add(en_key)

				if out: fd.write(en_key + " -> " + gr_key + "\n")
			if out:	fd.write("\n")
	if out:	fd.close()
	return (rules, gr_syms, en_syms, n)

def matchingProbs(rules, n, file='rules.txt'):
	fd = codecs.open(file, 'w', 'utf8')
	for keys, values in rules.items():
		for key, value in values.items():
			prob = float(value) / n
			fd.write(keys + '\t->\t' + key + '\t%d\t\t%.4f\t weight = %.4f\n' % (value, prob, -math.log(prob)))
	fd.close()

def symstxt(syms, file='syms.syms'):
	fd = codecs.open(file, 'w', 'utf8')
	fd.write("eps\t0\n")
	for sym in syms: fd.write(sym + '\t' + str(ord(sym)) + '\n')
	fd.close()

def createFst(rules, n, gr_syms, en_syms, file='generic.fst'):
	state = 0;
	fd = codecs.open(file, 'w', 'utf-8')
	for keys, values in rules.items():
		for key, value in values.items():
			prob = float(value) / n
			weight = -math.log(prob)
			if len(keys) == len(key):
				fd.write('0\t0\t' + keys + '\t' + key + '\t' + str(weight) + '\n')
			elif len(keys) == 2:
				state += 1
				fd.write('0\t' + str(state) + '\t' + keys[0] + '\teps\t' + str(weight) + '\n')
				fd.write(str(state) + '\t0\t' + keys[1] + '\t' + key + '\t0\n')
			elif len(key) == 2:
				state += 1
				fd.write('0\t' + str(state) + '\teps\t' + key[0] + '\t' + str(weight) + '\n')
				fd.write(str(state) + '\t0\t' + keys + '\t' + key[1] + '\t0\n')
	fd.write("0\n")
	fd.close()

if __name__ == "__main__":
	main()