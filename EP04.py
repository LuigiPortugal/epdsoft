# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:08:23 2018

@author: Luigi e Felipe 
"""


import json
with open("Estoque.json" , "r") as entrada:
    arquivo_dicionario = json.loads(entrada.read())

    
Estoque = arquivo_dicionario
estoque_negativo = []

escolha = 20
while escolha != 0:
    
    print("Controle de Estoque")
    print("0 - sair")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - alterar item")
    print("4 - imprimir estoque")
    print("5 - produtos em falta")
    print("6 - valor monetário total no Estoque")
    escolha = int(input("Faça sua escolha: "))

    if escolha == 0:
        print("Até mais")
        
    elif escolha == 1:
        produto = input("Nome do Produto: ")
        if produto not in Estoque:
            quantidade = int(input("Quantidade Inicial: "))
            if quantidade < 0:
                estoque_negativo.append(produto)
            preco_unidade = float(input("Preço Unitário do produto: "))
            if preco_unidade < 0:
                print("Não é possivel atribuir um preço negativo")
            else:
                Estoque.update({produto:{"quantidade":quantidade , "valor":preco_unidade}})
           
                
                
                
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
        alterar_item = int(input("Para alterar a quantidade digite 1 ; Para alterar o preço digite 2: "))
        if produto in Estoque and alterar_item == 1:
            quantidade_nova = int(input("Quantidade: "))
            Estoque[produto]["quantidade"] += quantidade_nova
        elif produto in Estoque and alterar_item == 2:
            valor_novo = float(input("Novo valor: "))
            Estoque[produto]["valor"] = valor_novo
                    
            print("Nova Quantidade e/ou preço de {0}: {1} , R${2}".format(produto , Estoque[produto]["quantidade"] , Estoque[produto]["valor"]))
        else:
            print("Elemento não Encontrado")
        
    elif escolha == 4:
        
        for key ,value in Estoque.items():
            print("{0}: {1}, R$ {2}".format(key , value["quantidade"] , value["valor"]))
        
    elif escolha == 5:
        print(estoque_negativo)
        
    elif escolha == 6:
        preco_total = 0
        for produto in Estoque:
            preco_total += Estoque[produto]["quantidade"] * Estoque[produto]["valor"]
        print("O valor total de seu Estoque é R${0}".format(preco_total))
            
                
      
    # Alteração no Estoque
    estoque_json = json.dumps(arquivo_dicionario, sort_keys = True , indent = 2 )
    with open("Estoque.json" , "w") as saida:
        saida.write(estoque_json)