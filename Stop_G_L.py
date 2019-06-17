# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:52:04 2019

@author: lucas
"""

preco_acao = float(input("Digite o preço da ação: "))
lucro_desejado = float(input("Digite o lucro desejado: "))
controle_risco = float(input("Digite o controle de risco: "))

stop_gain = str((preco_acao * (((lucro_desejado/100)*controle_risco) + 1.0)))
stop_loss = str((preco_acao * (( -1*(lucro_desejado/100 - 1.0)) )))

print ("Preço de stop gain: " + stop_gain)
print ("Preço de stop loss: " + stop_loss)

    