# -*- coding: utf-8 -*-

import codecs, math

train_wr = "../data/train_wr.txt"
train_co = "../data/train_co.txt"

rulesf = "rules.txt"
convertions = "convertions.txt"

dirC = "../out/C/"
fstC = "C.fst"

syms_wr = "isyms.syms"
syms_co = "osyms.syms"

sp_ch_wr =  {u'Ω' : [u'ΟΥ'], u'Ι' : [u'ΕΙ'], u'Η' : [u'ΕΙ'], u'ΕΙ' : [u'Η', u'Ι', u'Ή', u'Υ'], u'Υ' : [u'ΕΙ'], u'ΛΛ' : [u'Λ'], u'ΑΙ' : [u'Ε'], u'Ε' : [u'ΑΙ'], u'ΜΜ' : [u'Μ'], u'Γ' : [u'ΓΓ'], u'ΓΓ' : [u'ΓΚ'], u'ΓΚ' : [u'ΓΓ'], u'Ν' : [u'ΝΝ'], u'ΝΝ' : [u'Ν'], u'Η' : [u'ΟΙ'], u'ΟΙ' : [u'Η']}
sp_ch_co =  {u'ΟΥ' : [u'Ω'], u'ΕΙ' : [u'Ι', u'Η', u'Ή', u'Υ'], u'Λ' : [u'ΛΛ'], u'ΛΛ' : [u'Λ'], u'Ε' : [u'ΑΙ'], u'ΑΙ' : [u'Ε'], u'Μ' : [u'ΜΜ'], u'ΓΓ' : [u'Γ', u'ΓΚ'], u'ΓΚ' : [u'ΓΓ'], u'ΝΝ' : [u'Ν'], u'Ν' : [u'ΝΝ'], u'Η' : [u'ΟΙ'], u'ΟΙ' : [u'Η']}

def main():
	wrong = readContent(train_wr)
	correct = readContent(train_co)
	(rules, i_count, d_count, r_count, e_count, n) = matchingRules(wrong, correct, dirC + convertions, True)
	
	matchingProbs(rules, i_count, d_count, r_count, e_count, n, dirC + rulesf)

def readContent (file):
	fd = codecs.open(file, 'r', 'utf8')
	content = fd.read().split()
	fd.close()
	return content

def matchingRules(wrong, correct, file='convertions.txt', out=True):
	content = zip(wrong, correct)
	if out:
		fd = codecs.open(file, 'w', 'utf8')

	n = 0; i_count = 0; d_count = 0; e_count = 0; r_count = 0
	wr_syms = set(); co_syms = set(); rules = dict()
	for wrong_word, correct_word in content:
		if wrong_word != correct_word:
			last_wrong = last_correct = 1
			wrong_index = correct_index = 0
			wrong_length = len(wrong_word)
			correct_length = len(correct_word)
			while wrong_index < wrong_length and correct_index < correct_length:
				if wrong_index >= wrong_length - 1: last_wrong = 0
				if correct_index >= correct_length - 1: last_correct = 0

				if last_wrong and wrong_word[wrong_index] + wrong_word[wrong_index + 1] in sp_ch_wr.keys() and correct_word[correct_index] in sp_ch_wr[wrong_word[wrong_index] + wrong_word[wrong_index + 1]]:
					if (last_correct and wrong_word[wrong_index] + wrong_word[wrong_index + 1] == u'ΛΛ' and correct_word[correct_index] + correct_word[correct_index + 1] == u'ΛΛ') \
						or (last_correct and wrong_word[wrong_index] + wrong_word[wrong_index + 1] == u'ΓΓ' and correct_word[correct_index] + correct_word[correct_index + 1] == u'ΓΓ'):
							wrong_index += 1;	correct_index += 1; continue
					else:
						correct_key = correct_word[correct_index]; wrong_key = wrong_word[wrong_index] + wrong_word[wrong_index + 1]; wrong_index += 1; d_count += 1
						if wrong_word[wrong_index] != correct_word[correct_index] or wrong_word[wrong_index + 1] != correct_word[correct_index]: r_count += 1;
				elif last_correct and correct_word[correct_index] + correct_word[correct_index + 1] in sp_ch_co.keys() and wrong_word[wrong_index] in sp_ch_co[correct_word[correct_index] + correct_word[correct_index + 1]]:
						if (last_wrong and correct_word[correct_index] + correct_word[correct_index + 1] == u'ΓΓ' and wrong_word[wrong_index] + wrong_word[wrong_index + 1] == u'ΓΓ') \
							or (last_wrong and correct_word[correct_index] + correct_word[correct_index + 1] == u'ΛΛ' and wrong_word[wrong_index] + wrong_word[wrong_index + 1] == u'ΛΛ'):
								wrong_index += 1;	correct_index += 1; continue
						else:
							correct_key = correct_word[correct_index] + correct_word[correct_index + 1]; wrong_key = wrong_word[wrong_index]; correct_index += 1; i_count += 1
							if correct_word[correct_index] != wrong_word[wrong_index] or correct_word[correct_index + 1] != wrong_word[wrong_index]: r_count += 1
				elif last_wrong and correct_word[correct_index] in sp_ch_co.keys() and wrong_word[wrong_index] + wrong_word[wrong_index + 1] in sp_ch_co[correct_word[correct_index]]:
					correct_key = correct_word[correct_index]; wrong_key = wrong_word[wrong_index] + wrong_word[wrong_index + 1]; wrong_index += 1; d_count += 1
					if wrong_word[wrong_index] != correct_word[correct_index] or wrong_word[wrong_index + 1] != correct_word[correct_index]: r_count += 1;
				elif last_correct and wrong_word[wrong_index] in sp_ch_wr.keys() and correct_word[correct_index] + correct_word[correct_index + 1] in sp_ch_wr[wrong_word[wrong_index]]:
					correct_key = correct_word[correct_index] + correct_word[correct_index + 1]; wrong_key = wrong_word[wrong_index]; correct_index += 1; i_count += 1
					if correct_word[correct_index] != wrong_word[wrong_index] or correct_word[correct_index + 1] != wrong_word[wrong_index]: r_count += 1
				# special rules
				elif last_correct and (not last_wrong):
					i_count += 1
					wrong_key = 'i'
					if wrong_word[wrong_index] == correct_word[correct_index]:
						correct_key = correct_word[correct_index + 1]; correct_index += 1
					else:
						correct_key = correct_word[correct_index]
				elif (not last_correct) and last_wrong:
					d_count += 1
					wrong_key = wrong_word[wrong_index + 1]; correct_key = 'd'; wrong_index += 1
				elif wrong_word[wrong_index] != correct_word[correct_index]:
					# exchange rule
					if last_correct and last_wrong and wrong_word[wrong_index] == correct_word[correct_index + 1] and wrong_word[wrong_index + 1] == correct_word[correct_index] and wrong_word[wrong_index] != wrong_word[wrong_index + 1]:
						correct_key = correct_word[correct_index] + correct_word[correct_index + 1]; wrong_key = wrong_word[wrong_index] + wrong_word[wrong_index + 1]; correct_index += 1; wrong_index += 1; e_count += 1
					# insertion rule
					elif last_correct and wrong_word[wrong_index] == correct_word[correct_index + 1]:
						i_count += 1
						wrong_key = 'i'; correct_key = correct_word[correct_index]; correct_index += 1
					# deletion rule
					elif last_wrong and wrong_word[wrong_index + 1] == correct_word[correct_index]:
						d_count += 1
						wrong_key = wrong_word[wrong_index]; correct_key = 'd'; wrong_index += 1
					else:
						wrong_key = wrong_word[wrong_index]; correct_key = correct_word[correct_index]; r_count += 1
				else:
					wrong_index += 1;	correct_index += 1
					continue

				if wrong_key in rules.keys():
					if correct_key in rules[wrong_key].keys(): rules[wrong_key][correct_key] += 1
					else: rules[wrong_key][correct_key] = 1
				else:
					rules[wrong_key] = dict()
					rules[wrong_key][correct_key] = 1

				wrong_index += 1;	correct_index += 1
				if out: fd.write(wrong_key + " -> " + correct_key + "\n")
			if out: fd.write(wrong_word + " -> " + correct_word + "\n\n")
		else:
			n += 1
	if out:
		fd.write("insertion: %d\ndeletion: %d\nreplace: %d\nexhange: %d\ncorrect: %d" % (i_count, d_count, r_count, e_count, n))
		fd.close()
	return (rules, i_count, d_count, r_count, e_count, n + i_count + d_count + r_count + e_count)

def matchingProbs(rules, i_count, d_count, r_count, e_count, n, file='rules.txt'):
	fd = codecs.open(file, 'w', 'utf8')
	prob_i = float(i_count) / n; prob_d = float(d_count) / n; prob_r = float(r_count) / n; prob_e = float(e_count) / n
	fd.write("insertion: %.2f %.4f\ndeletion: %.2f %.4f\nreplace: %.2f %.4f\nexhange: %.2f %.4f\n\n" % (prob_i, -math.log(prob_i), prob_d, -math.log(prob_d), prob_r, -math.log(prob_r), prob_e, -math.log(prob_e)))
	for keys, values in rules.items():
		for key, value in values.items():
			prob = float(value) / n
			fd.write(keys + '\t->\t' + key + '\t%d\t\t%.4f\t weight = %.4f\n' % (value, prob, -math.log(prob)))
	fd.close()

def createFst(rules, n, wr_syms, co_syms, file='generic.fst'):
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