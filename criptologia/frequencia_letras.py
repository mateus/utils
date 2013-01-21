#coding: utf-8

import operator
import string

from unicodedata import normalize

texto = raw_input('Mensagem: ')
dic = {}

texto = texto.lower()
texto = normalize('NFKD', texto.decode('utf-8')).encode('ASCII','ignore') 

total = 0
for letra in set(texto):
	if letra in string.ascii_lowercase:
		dic[letra] = texto.count(letra)
		total += texto.count(letra)

print '\nLetra | Ocorrências'
for ordem in sorted(dic.iteritems()):
	print '    {} = {}'.format(ordem[0], ordem[1])

print '\nLetra | Freqência'
for ordem in sorted(dic.iteritems()):
	print '    {} = {}%'.format(ordem[0], round((float(ordem[1])*100)/total, 2))

