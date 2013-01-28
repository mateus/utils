#!/usr/bin/env python
#coding: utf-8

import distancia_levenshtein

from unicodedata import normalize

def verifica(palavra):
    wordlist = {}
    distancia = 2
    margem = 2
    menor = 500
    quiz_dizer = []
    with open('wordlist-pt-br.txt') as wl:
        for p in wl.readlines():
            p = p.strip()
            p = normalize('NFKD', p.decode('utf-8')).encode('ASCII','ignore')
            if len(p) in wordlist:
                wordlist[len(p)].append(p)
            else:
                wordlist[len(p)] = list(p)
    tam_palavra = len(palavra)
    valores = [n for n in xrange(tam_palavra-margem,tam_palavra+margem+1) if n > 0]
        
    for valor in valores:
        for palavraWl in wordlist[valor]:
            if distancia_levenshtein.levenshtein(palavra, palavraWl) <= distancia:
                if len(palavraWl) < menor:
                    quiz_dizer = [palavraWl, ]
                    menor = len(palavraWl)
                elif len(palavraWl) == menor:
                    quiz_dizer.append(palavraWl)
                if distancia_levenshtein.levenshtein(palavra, palavraWl) == 0:
                    print 'Palavra correta'
                    return
    print 'Você quiz dizer:', ' ou '.join(quiz_dizer), '?'

while True:
    verifica(raw_input('\nPalavra: '))
