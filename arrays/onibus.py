#!/usr/bin/env python



'''Uma empresa possui onibus com 48 lugares -24 nas janelas
e 24 no corredor-. Faca um programa que utilize dois
vetores para controlar as poltronas ocupadas no corredor
e na janela. Considere que zero representa poltrona
desocupada e um representa poltrona ocupada.
           +-- -+- -- +-- -+- -- +-- -+- -- +-- -+- -- +
JANELA     |  0  |  1  |  0  |  0  |  |  1  |  1  |  1 |
           +-- -+- -- +-- -+- -- +-- -+- -- +-- -+- -- +
Poltrona     1    2    3    4    ...    22    23    24
           +-- -+- -- +-- -+- -- +-- -+- -- +-- -+- -- +
CORREDOR   |  0  |  1  |  0  |  0  |  |  0  |  0  |  1  |
           +-- -+- -- +-- -+- -- +-- -+- -- +-- -+- -- +
Esse programa deve controlar a venda de passagens da
seguinte maneira:
O cliente informa se deseja poltrona no corredor ou
na janela e, depois, o programa deve informar quais
poltronas estão disponíveis para a venda;
Quando não existirem poltronas livres no corredor,
nas janelas ou, ainda, quando o ônibus estiver
completamente cheio, deve ser mostrada uma mensagem.'''