#!/usr/bin/env python
#coding: utf-8
#Author: Mateus Ferreira Silva

import requests
import re

class tradutor():
    def __init__(self):
        self.url = 'http://translate.google.com/translate_t?q=%s&sl=%s&tl=%s'
        self.texto = ''
        self.deIdioma = 'en'
        self.paraIdioma = 'pt'

    def menu(self):
        print '\n\033[1;34m1 - Inglês -> Português'
        print '2 - Português -> Inglês'
        print '0 - Sair\033[0m\n'

    def setTexto(self, texto):
        self.texto = texto.replace(' ', '+')

    def setOpcao(self, op):
        if op == '1':
            self.deIdioma = 'en'
            self.paraIdioma = 'pt'
        elif op == '2':
            self.deIdioma = 'pt'
            self.paraIdioma = 'en'

    def traduzir(self):
        html = requests.get(self.url % (self.texto, self.deIdioma, self.paraIdioma, )).text.encode('utf8')
        resultado = re.search(r'TRANSLATED_TEXT=\'(.+?)\'', html).group(1)
        return '\033[1;33mResposta: \033[1;32m{}\033[0m'.format(resultado)

    def appTradutor(self):
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
            self.setOpcao(op)
            while len(texto.strip()) == 0:
                texto = raw_input('\033[1;33mTexto: \033[1;32m')
            self.setTexto(texto)
            resultado = self.traduzir()
            print resultado

if __name__ == "__main__":
    t = tradutor()
    try:
        t.appTradutor()
    except KeyboardInterrupt:
        print '\n'
        exit()
    