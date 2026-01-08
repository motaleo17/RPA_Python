import time
import os
import sys
from pathlib import Path

#Atalho
atalho = r"C:\Projetos\Python\RPA_Python\Teste_Leonardo.exe"

#JANELAS
janelaPrincipal = "TESTE LEONARDO"
janelaBotaoUm = "Teste_Leonardo.exe"

numeroum = "C:\\Lighthouse\\Testes\\Python\\img\\um.png"
numerodois = "C:\\Lighthouse\\Testes\\Python\\img\\dois.png"
numerotres = "C:\\Lighthouse\\Testes\\Python\\img\\tres.png"
numeroquatro = "C:\\Lighthouse\\Testes\\Python\\img\\quatro.png"
numerocinco = "C:\\Lighthouse\\Testes\\Python\\img\\cinco.png"
numeroseis = "C:\\Lighthouse\\Testes\\Python\\img\\seis.png"
numerosete = "C:\\Lighthouse\\Testes\\Python\\img\\sete.png"
numerooito = "C:\\Lighthouse\\Testes\\Python\\img\\oito.png"
numeronove = "C:\\Lighthouse\\Testes\\Python\\img\\nove.png"
numerozero = "C:\\Lighthouse\\Testes\\Python\\img\\zero.png"
divisao = "C:\\Lighthouse\\Testes\\Python\\img\\divisao.png"
multiplicacao = "C:\\Lighthouse\\Testes\\Python\\img\\multiplicacao.png"
adicao = "C:\\Lighthouse\\Testes\\Python\\img\\adicao.png"
subtracao = "C:\\Lighthouse\\Testes\\Python\\img\\subtracao.png"
igual = "C:\\Lighthouse\\Testes\\Python\\img\\igual.png"

NUMBERS = {
    "0": numerozero,
    "1": numeroum,
    "2": numerodois,
    "3": numerotres,
    "4": numeroquatro,
    "5": numerocinco,
    "6": numeroseis,
    "7": numerosete,
    "8": numerooito,
    "9": numeronove,
}

OPERATIONS = {
    "+": "add",
    "-": "sub",
    "*": "mul",
    "/": "div"
}

CALCULATOR_TITLE = "Calculadora"



#Janelas
CALCULATOR_TITLE = "Calculadora"