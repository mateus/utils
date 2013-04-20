#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author: Mateus Ferreira Silva <mtsferreirasilva@gmail.com>

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='inputfile', help='Nome do arquivo de entrada (Requerido)', required = True)
parser.add_argument('-o', dest='outputfile', help='Nome do arquivo de destino')
args = parser.parse_args()

try:
    with open(args.inputfile, 'r') as f:
        html = f.read()
        html = re.sub(">\s*<","><", html)
        if args.outputfile:
            outputFileName = args.outputfile
        else:
            outputFileName = '{}_res.html'.format(args.inputfile.split('.')[0])
        with open(outputFileName, 'w') as o:
            o.write(html)
        print 'Arquivo {} criado com sucesso.'.format(outputFileName)
except IOError:
    print 'Arquivo de entrada não encontrado.'
