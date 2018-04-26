# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:31:15 2018

@author: Luigi e Felipe
"""

import json
with open("Estoque.json" , "r") as entrada:
    dicionario_lojas = json.loads(entrada.read())

dicionario_lojas = {}

print("Controle de lojas:")
print("0 - Sair.")
print("1 - Acessar uma loja.")
print("2 - Adicionar uma loja.")
print("3 - Remover uma loja.")
e = int(input("Faça sua escolha: "))
while e != 0:    
    if e == 2:
        print("Voce deseja adicionar uma loja.")
        loja = input("Qual o nome da loja a ser adicionada? ")
        dicionario_lojas[loja]={}
        print("Controle de lojas:")
        print("0 - Sair.")
        print("1 - Acessar uma loja.")
        print("2 - Adicionar uma loja.")
        print("3 - Remover uma loja.")
        e = int(input("Faça sua escolha: "))
        
    elif e == 3:
        print("Voce deseja remover uma loja.")
        loja = input("Qual o nome da loja a ser removida?")
        del dicionario_lojas[loja]
        print("Controle de lojas:")
        print("0 - Sair.")
        print("1 - Acessar uma loja.")
        print("2 - Adicionar uma loja.")
        print("3 - Remover uma loja.")
        e = int(input("Faça sua escolha: "))
       
 #   elif e == 0:
 #      print("Obrigado! Volte sempre!")
  
    elif e == 1:
        #print("Acessando lojas ja cadastradas: ")
        
        loja = input("Qual o nome da loja desejada? ")
        if loja not in dicionario_lojas:
            print("Loja não cadastrada.")
            print("Controle de lojas:")
            print("0 - Sair.")
            print("1 - Acessar uma loja.")
            print("2 - Adicionar uma loja.")
            print("3 - Remover uma loja.")
            e = int(input("Faça sua escolha: "))
        else:                
                print("Controle de Estoque:")
                print("0 - sair")
                print("1 - adicionar item")
                print("2 - remover item")
                print("3 - alterar item")
                print("4 - imprimir estoque")
                print("5 - imprimir valor monetário total")
                print("6 - imprimir estoque negativo")
                escolha = int(input("Faça sua escolha: "))
            
                while escolha != 0:
#                if escolha == 0:
#                    print("Voltando para o Controle de Lojas.")
#                    print("Controle de lojas:")
#                    print("0 - Sair.")
#                    print("1 - Acessar uma loja.")
#                    print("2 - Adicionar uma loja.")
#                    print("3 - Remover uma loja.")
#                    e = int(input("Faça sua escolha: "))
#                   escolha = 0
                    
                    if escolha == 1:
                        produto = input("Nome do Produto: ")
                        if produto not in dicionario_lojas[loja]:
                            dicionario_lojas[loja][produto] = {}  
                            quantidade = int(input("Quantidade Inicial: "))
                            while quantidade < 0:
                                print("Quantidade Negativa: Erro.")
                                quantidade = int(input("Quantidade inicial: "))
                            dicionario_lojas[loja][produto]["Quantidade"]=quantidade
                            preco_unidade = float(input("Preço Unitário do produto: "))
                            while preco_unidade < 0:
                                print("Valor negativo: Erro.")
                                preco_unidade = float(input("Preço unitário do produto: "))
                            dicionario_lojas[loja][produto]["Preço unitário"]=preco_unidade
                        else:
                            print("O produto já foi cadastrado.")
                        print("Controle de Estoque:")
                        print("0 - sair")
                        print("1 - adicionar item")
                        print("2 - remover item")
                        print("3 - alterar item")
                        print("4 - imprimir estoque")
                        print("5 - imprimir valor monetário total")
                        print("6 - imprimir estoque negativo")
                        escolha = int(input("Faça sua escolha: "))
        
                    elif escolha == 2:
                        produto = input("Nome do Produto: ")
                        if produto in dicionario_lojas[loja]:
                            del dicionario_lojas[loja][produto]
                            print("Controle de Estoque:")
                            print("0 - sair")
                            print("1 - adicionar item")
                            print("2 - remover item")
                            print("3 - alterar item")
                            print("4 - imprimir estoque")
                            print("5 - imprimir valor monetário total")
                            print("6 - imprimir estoque negativo")
                            escolha = int(input("Faça sua escolha: "))
                        else:
                            print("Elemento não encontrado.")
                            print("Controle de Estoque:")
                            print("0 - sair")
                            print("1 - adicionar item")
                            print("2 - remover item")
                            print("3 - alterar item")
                            print("4 - imprimir estoque")
                            print("5 - imprimir valor monetário total")
                            print("6 - imprimir estoque negativo")
                            escolha = int(input("Faça sua escolha: "))
                    
                    elif escolha == 3:
                        produto = input("Nome do Produto: ")
                        alterar_item = int(input("Para alterar a quantidade digite 1 ; Para alterar o preço digite 2: "))
                        if produto in dicionario_lojas[loja] and alterar_item == 1:
                            quantidade_nova = int(input("Quantidade a ser somada(positiva para adicionando e negativa para removendo): "))
                            dicionario_lojas[loja][produto]["Quantidade"] += quantidade_nova
                            print("Controle de Estoque:")
                            print("0 - sair")
                            print("1 - adicionar item")
                            print("2 - remover item")
                            print("3 - alterar item")
                            print("4 - imprimir estoque")
                            print("5 - imprimir valor monetário total")
                            print("6 - imprimir estoque negativo")
                            escolha = int(input("Faça sua escolha: "))
                            
                        elif produto in dicionario_lojas[loja] and alterar_item == 2:
                            valor_novo = float(input("Novo valor: "))
                            dicionario_lojas[loja][produto]["valor"] = valor_novo
                            print("Nova Quantidade e/ou preço de {0}: {1} , R${2}".format(produto , dicionario_lojas[loja][produto]["Quantidade"] , dicionario_lojas[loja][produto]["valor"]))
                            print("Controle de Estoque:")
                            print("0 - sair")
                            print("1 - adicionar item")
                            print("2 - remover item")
                            print("3 - alterar item")
                            print("4 - imprimir estoque")
                            print("5 - imprimir valor monetário total")
                            print("6 - imprimir estoque negativo")
                            escolha = int(input("Faça sua escolha: "))
                            
                        else:
                            print("Elemento não Encontrado")
                            print("Controle de Estoque:")
                            print("0 - sair")
                            print("1 - adicionar item")
                            print("2 - remover item")
                            print("3 - alterar item")
                            print("4 - imprimir estoque")
                            print("5 - imprimir valor monetário total")
                            print("6 - imprimir estoque negativo")
                            escolha = int(input("Faça sua escolha: "))
                            
                    elif escolha == 4:
                        
                        for produto in dicionario_lojas[loja]:
                            print("{0}: {1}: {2}, R$ {3} cada".format(loja , produto, dicionario_lojas[loja][produto]["Quantidade"] , dicionario_lojas[loja][produto]["Preço unitário"]))
                        print("Controle de Estoque:")
                        print("0 - sair")
                        print("1 - adicionar item")
                        print("2 - remover item")
                        print("3 - alterar item")
                        print("4 - imprimir estoque")
                        print("5 - imprimir valor monetário total")
                        print("6 - imprimir estoque negativo")
                        escolha = int(input("Faça sua escolha: "))
                        
                    #Imprimir valor monetário total em estoque
                    elif escolha == 5:
                        valor_monetário_total = 0
                        for produto in dicionario_lojas[loja]:
                            valor_monetário_total = dicionario_lojas[loja][produto]["Quantidade"] * dicionario_lojas[loja][produto]["Preço unitário"]
                            print("O valor monetario total é: {0}".format(valor_monetário_total))
                        print("Controle de Estoque:")
                        print("0 - sair")
                        print("1 - adicionar item")
                        print("2 - remover item")
                        print("3 - alterar item")
                        print("4 - imprimir estoque")
                        print("5 - imprimir valor monetário total")
                        print("6 - imprimir estoque negativo")
                        escolha = int(input("Faça sua escolha: "))
                        
                    #Listagem dos produtos com quantidade de estoque negativa
                    elif escolha == 6:
                        for produto in dicionario_lojas[loja]:
                            if dicionario_lojas[loja][produto]["quantidade"] < 0:
                                print(produto)
                        print("Controle de Estoque:")
                        print("0 - sair")
                        print("1 - adicionar item")
                        print("2 - remover item")
                        print("3 - alterar item")
                        print("4 - imprimir estoque")
                        print("5 - imprimir valor monetário total")
                        print("6 - imprimir estoque negativo")
                        escolha = int(input("Faça sua escolha: "))
                if escolha == 0:
                    print("Voltando para o Controle de Lojas.")
                    print("Controle de lojas:")
                    print("0 - Sair.")
                    print("1 - Acessar uma loja.")
                    print("2 - Adicionar uma loja.")
                    print("3 - Remover uma loja.")
                    e = int(input("Faça sua escolha: "))
                    escolha = 0

print("Obrigado! Volte sempre!")                        

# Alteração no Estoque
estoque_json = json.dumps(dicionario_lojas, sort_keys = True , indent = 2 )
with open("Estoque.json" , "w") as saida:
    saida.write(estoque_json)
                    
with open ("Estoque.json", "w") as entrada:
    entrada.write(json.dumps(dicionario_lojas, sort_keys=True, indent=4))  
    
    
    
    
    
    
    
    
    
    
    