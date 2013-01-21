# coding: utf-8

import Image
import pylab

def ataque_estatistico(imagem):
    # Abre a imagem, obtém seus atributos e carrega os pixels para a memória
    img = Image.open(imagem)
    largura, altura = img.size
    pix = img.load()
    
    # Lista de valores para o eixo y
    coord_y = []

    # Percorre cada linha da imagem
    for y in xrange(altura):
        # Percorre todos os pixels da linha contando a quantidade de bits 1
        cont = 0
        for x in xrange(largura):
            cont += len([cor for cor in pix[x, y][:3] if cor % 2])
        coord_y.append((cont * 100) / (3 * largura))
        
    # Define os rótulos do gráfico
    ytext = pylab.ylabel('LSB valor 1 (%)')
    xtext = pylab.xlabel('Linhas')
    
    # Plota e exibe a imagem
    pylab.plot(xrange(altura), coord_y, 'o')
    pylab.show() 

ataque_estatistico('img_msg.png')
