# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:21:28 2018

@author: Luigi
"""

import json
with open("Estoque.json" , "r") as entrada:
    arquivo_dicionario = json.loads(entrada.read())

    
Estoque = arquivo_dicionario
escolha = 20
while escolha != 0:
    
    print("Controle de Estoque")
    print("0 - sair")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - alterar item")
    print("4 - imprimir estoque")
    escolha = int(input("Faça sua escolha: "))

    if escolha == 0:
        print("Até mais")
        
    elif escolha == 1:
        produto = input("Nome do Produto: ")
        if produto not in Estoque:
            quantidade = int(input("Quantidade Inicial: "))
            if quantidade < 0:
                print("A quantidade inicial não pode ser negativa")
            else:
                Estoque.update({produto:{"quantidade":quantidade}})
                #print(Estoque)
        else:
            print("Produto já está cadastrado")
       
    
    elif escolha == 2:
        produto = input("Nome do Produto: ")
        if produto in Estoque:
            del Estoque[produto]
        else:
            print("Elemento não encontrado")
    
    elif escolha == 3:
        produto = input("Nome do Produto: ")
        if produto in Estoque:
            quantidade_nova = int(input("Quantidade: "))
            Estoque[produto]["quantidade"] += quantidade_nova
                    
            print("Novo Estoque de {0}: {1}".format(produto , Estoque[produto]["quantidade"]))
        else:
            print("Elemento não Encontrado")
        
    elif escolha == 4:
        
        for key ,value in Estoque.items():
            print("{0}: {1}".format(key , value["quantidade"]))
    
    # Alteração no Estoque
    estoque_json = json.dumps(arquivo_dicionario, sort_keys = True , indent = 2 )
    with open("Estoque.json" , "w") as saida:
        saida.write(estoque_json)