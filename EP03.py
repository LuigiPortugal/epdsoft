# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:31:15 2018

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
            preco_unidade = float(input("Preço Unitário do produto: "))
            if quantidade < 0:
                print("A quantidade inicial não pode ser negativa")
            else:
                Estoque.update({produto:{"quantidade":quantidade , "valor":preco_unidade}})
                
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
    
    # Alteração no Estoque
    estoque_json = json.dumps(arquivo_dicionario, sort_keys = True , indent = 2 )
    with open("Estoque.json" , "w") as saida:
        saida.write(estoque_json)