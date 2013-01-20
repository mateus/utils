#coding: utf-8

import string

texto = raw_input('Texto cifrado: ')
for k in xrange(26):
	alternado_lowercase = string.ascii_lowercase[k:] + string.ascii_lowercase[:k]
	tabela_traducao = string.maketrans(string.ascii_lowercase, alternado_lowercase)
	texto = texto.lower()
	print texto.translate(tabela_traducao), '- Chave:', k
	
