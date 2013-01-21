# coding: utf-8

import re

LINHAS = 16

def gera_bin(msg):
    return ''.join(bin(ord(caractere))[2:].zfill(8) for caractere in msg)

def gera_cod(msg, arq):
    tamanho = gera_bin(str(len(msg)))
    cont = 0
    cont_linhas_contexto = 0
    arq = open(arq)
    texto_novo = []
    for linha in arq.readlines(): 
        if cont_linhas_contexto < LINHAS:
            if tamanho[cont_linhas_contexto] == '0':
                linha = linha[:len(linha)-1]
                linha = linha + '\r\n'
            cont_linhas_contexto+=1
        elif cont < len(msg):
            if msg[cont] == '0':
                linha = linha[:len(linha)-1]
                linha = linha + '\r\n'
            cont+=1
        texto_novo.append(linha)
    return ''.join(texto_novo)

def decodifica(arq):
    pass

if __name__ == '__main__':
    msg_bin = gera_bin('Batman') # mensagem
    print 'Numero do cabeçalho: ', gera_bin(str(len(msg_bin)))
    print 'Mensagem: ', msg_bin
    open('msg_nova.txt', 'w').write(gera_cod(msg_bin, 'lusiadas.txt'))
