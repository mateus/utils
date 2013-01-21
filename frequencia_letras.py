#coding: utf-8

import operator
import string

texto = raw_input('Texto: ')
dic = {}
texto = texto.lower()

texto = texto.replace('á', 'a')
texto = texto.replace('à', 'a')
texto = texto.replace('ã', 'a')
texto = texto.replace('â', 'a')
texto = texto.replace('Á', 'a')
texto = texto.replace('À', 'a')
texto = texto.replace('Ã', 'a')
texto = texto.replace('Â', 'a')

texto = texto.replace('é', 'e')
texto = texto.replace('ê', 'e')
texto = texto.replace('É', 'e')
texto = texto.replace('ê', 'e')

texto = texto.replace('í', 'i')
texto = texto.replace('Í', 'i')

texto = texto.replace('ó', 'o')
texto = texto.replace('õ', 'o')
texto = texto.replace('ô', 'o')
texto = texto.replace('ó', 'o')
texto = texto.replace('Õ', 'o')
texto = texto.replace('Ô', 'o')

texto = texto.replace('ú', 'u')
texto = texto.replace('ú', 'u')

texto = texto.replace('ç', 'c')
texto = texto.replace('Ç', 'c')

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

