#coding: utf-8

import operator

texto = raw_input('Texto: ')
dic = {}

for letra in set(texto):
	dic[letra] = texto.count(letra)

print '\nLetra | Ocorrências'
for ordem in sorted(dic.iteritems()):
	print '    {} = {}'.format(ordem[0], ordem[1])
	
maior = max(dic.iteritems())
l = []
for valor in dic:
	if dic[valor] == maior[1]:
		l.append(valor)
l = ', '.join(l)
print '\nMaior ocorrência foi {} em "{}"\n'.format(maior[1], l)

