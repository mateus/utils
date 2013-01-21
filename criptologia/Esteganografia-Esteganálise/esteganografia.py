# coding: utf-8

import re
import Image

# Define quantos pixels serão utilizados para informar o tamanho da mensagem oculta
PIXELS_RESERVADOS = 10

def pixels(tam):
    '''Facilita a iteração pelos pixels da imagem'''
    for y in xrange(tam[1]):
        for x in xrange(tam[0]):
            yield (x, y)


def esteganografar(img_orig, img_esteg, str_bin):
    # Abre a imagem e obtém seus atributos
    img = Image.open(img_orig)
    largura, altura = img.size

    # Verifica se o formato da imagem é compatível e se ela possui capacidade
    if img.mode[:3] != 'RGB' or largura * altura * 3  < len(str_bin) + PIXELS_RESERVADOS * 3:
        raise IndexError('O tamanho da mensagem excede a capacidade da imagem ou não há suporte para a mesma')

    # Os primeiros pixels definem o tamanho da informação a ser ocultada
    bits_tam = bin(len(str_bin))[2:].zfill(PIXELS_RESERVADOS * 3)
    str_bin = bits_tam + str_bin
    
    # Completa a informação tornando-a múltipla de 3 e iterável;
    str_bin = enumerate(str_bin + '0' * (3 - len(str_bin) % 3))

    # Carrega os pixels da imagem para a memória;
    pix = img.load()
    
    # Percorre cada pixel da imagem
    for x, y in pixels(img.size):
        try:
            # Altera o valor dos bits menos significativos
            rgb = map(lambda cor, bit: cor - (cor % 2) + int(bit), pix[x, y][:3], [str_bin.next()[1] for _ in xrange(3)])
            pix[x, y] = tuple(rgb)
        except StopIteration:
            # Quando não houver mais bits para se esteganografar, str_bin disparará uma
            # exceção do tipo StopIteration, e a nova imagem estará pronta para ser salva;
            img.save(img_esteg, 'PNG', quality=100)
            return


def recuperar(img_esteg):
    # Abre a imagem, obtém seus atributos e carrega os pixels para a memória
    img = Image.open(img_esteg)
    tam = img.size
    pix = img.load()

    # Obtém os primeiros pixels, que definem o tamanho da informação embutida;
    info_tam = ''
    for p in pixels(tam):
        info_tam += ''.join('1' if cor % 2 else '0' for cor in pix[p][:3])
        if len(info_tam) >= PIXELS_RESERVADOS * 3:
            info_tam = int(info_tam, 2)
            break  
    
    # Extrai a informação binária da imagem
    info_bin = ''
    for p in pixels(tam):
        info_bin += ''.join('1' if cor % 2 else '0' for cor in pix[p][:3])
    
    return info_bin[PIXELS_RESERVADOS * 3:info_tam + PIXELS_RESERVADOS * 3]


def gera_bin(msg):
    '''Para cada caractere, obtém o valor binário de seu código ASCII'''
    return ''.join(bin(ord(caractere))[2:].zfill(8) for caractere in msg)


def recupera_str(str_bin):
    '''Converte cada grupo de 8 bits no seu respectivo caractere'''
    return ''.join(chr(int(bin, 2)) for bin in re.findall(r'.{8}', str_bin))


if __name__ == '__main__':    
    # Oculta a mensagem "Viva o Linux" na imagem "img.jpg" e
    # salva o resultado como "img_msg.png";
    msg_bin = gera_bin(open('lusiadas.txt').read())
    esteganografar('img.jpg', 'img_msg.png', msg_bin)
    
    # Recupera a mensagem
    msg_bin = recuperar('img_msg.png')
    print recupera_str(msg_bin)
