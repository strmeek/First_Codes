# -*- coding: utf-8 -*-
"""Fundamentos de Progr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lh5qfca6J8lahP093j9JVM_L1cUgsSb5
"""

import datetime

hoje = date.today()

br_date = '{}/{}/{}' .format(hoje.day,hoje.month,hoje.year)

print(br_date)

prices = []
for i in range(3):
  value = float(input("valor de compra: "))
  prices.append(value)

x = min(prices)
print("o {1}º produto de valor:{0} ".format(x, prices.index(x) + 1))

meses = ["Janeiro",
         "Fevereiro",
         "Março",
         "Abril",
         "Maio",
         "Junho",
         "Julho",
         "Agosto",
         "Setembro",
         "Outubro",
         "Novembro",
         "Dezembro",]

n = int(input("mês desejado?"))

if 1<= n <= 12:
  print(meses[n - 1])
else:
  print("inválido")

#divisão até 0 while
x = int(input('Digite um número: '))
def div0(x):
  while x > 0:
    x //= 2
    print(x)
div0(x)
#soma de numeros com while
preco = float(input('Digite o preço do produto: '))
def whilesum(preco):
  total = 0
  while preco != 0:
    total += preco
    preco = float(input('Digite o preço do produto: '))
  print(f'Total da venda: {total}')
whilesum(preco)