#!/usr/bin/env python
#coding: utf-8
#Author: Mateus Ferreira Silva

import requests
import re

class tradutor():
    def __init__(self):
        self.url = 'http://translate.google.com/translate_t?q=%s&sl=%s&tl=%s'

    def menu(self):
        print '\n\033[1;34m1 - Inglês -> Português'
        print '2 - Português -> Inglês'
        print '0 - Sair\033[0m\n'

    def traduzir(self):
        op = '-1'
        ops = ['0', '1', '2']
        while op != '0':
            texto = ''
            op = '-1'
            while op not in ops:
                self.menu()
                op = raw_input('\033[1;33mOpção: \033[1;32m')
            if op == '0':
                break
            if op == '1':
                deIdioma = 'en'
                paraIdioma = 'pt'
            else:
                deIdioma = 'pt'
                paraIdioma = 'en'
            while len(texto.strip()) == 0:
                texto = raw_input('\033[1;33mTexto: \033[1;32m')
            texto = texto.replace(' ', '+')
            self.url = 'http://translate.google.com/translate_t?q=%s&sl=%s&tl=%s' % (texto, deIdioma, paraIdioma, )
            html = requests.get(self.url).text.encode('utf8')
            resultado = re.search(r'TRANSLATED_TEXT=\'(.+?)\'', html).group(1)
            print '\033[1;33mResposta: \033[1;32m{}\033[0m'.format(resultado)

if __name__ == "__main__":
    t = tradutor()
    try:
        t.traduzir()
    except KeyboardInterrupt:
        print '\n'
        exit()
    