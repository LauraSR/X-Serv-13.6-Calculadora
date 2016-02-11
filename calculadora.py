#Laura Sanz Ruano G.ITT

#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    sys.exit ("Solo acepto 3 paramentros")
    
#_, operador, operando1, operando2 = sys.argv

operador = sys.argv[1]
operando1 = sys.argv[2]
operando2 = sys.argv[3]

operadores = ["suma", "resta", "multi", "div"]

if operador not in operadores:
    sys.exist ("Solo acepto s r m d")

try:
    operando1 = int(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("Dame un numero")

if operador == "suma":
    print operando1 + operando2

if operador == "resta":
    print operando1 - operando2

if operador == "multi":
    print operando1 * operando2

if operador == "div":
    try:
        print operando1 / operando2
    except ZeroDivisionError:
        print ("No me dividas entre cero")


