# coding: utf-8

import Image

def ataque_visual(imagem, destino):
    # Abre a imagem, obtém seus atributos e carrega os pixels para a memória
    img = Image.open(imagem)
    largura, altura = img.size
    pix = img.load()

    for x in xrange(largura):
        for y in xrange(altura):
            # Desloca os bits menos significativos para a posição mais significativa
            pix[x, y] = tuple(int(bin(cor)[-1] + '1111111', 2) for cor in pix[x, y])
    img.save(destino, 'PNG', quality=100) 

ataque_visual('img_msg.png', 'img_atacada.png')
