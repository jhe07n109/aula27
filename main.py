# CADASTRO DE USUÁRIO E SENHA 
saldo = 0.0 # VARIAVEL QUE GUARDARÁ O SALDO DO USUÁRIO
while True:
     # MENU PRINCIPAL
     print("BEM VINDO! /n digite 1. Cadastrar 2. Login 3.Encerrar")
     # LER A ESCOLHA PRINCIPAL
     escolha_menu = int (input()) # LER A ESCOLHA 1

    # USE USUÁRIO ESCOLHER CADASTRO
     if escolha_menu == 1:
    # CRIAR UM USUÁRIO E UMA SENHA COM TIPO STRING
      usuario = input ("Crie um nome de usuário ")
      senha = input ("Crie uma senha ")
     elif escolha_menu == 2: #SE USUÁRIO ESCOLHER LOGIN
      #COMPARAR AS INF. CADASTRADAS COM UMA LEITURA 
      login_usuario = input("Digite seu usuário ")
      login_senha = input("Digite sua senha ")
      if login_usuario == usuario and login_senha == senha:
          print ("LOGIN REALIZADO COM SUCESSO")
          # SE O LOGIN CORRETO, ENTRA NO MENU PRINCIPAL DO APP
          print("BEM VINDO", usuario)
          while True: # ENQUANTO EXIBIR O MENU PRINCIPAL
             print("1. DEPOSITO 2.SACAR 3.PIX 4.EXTRATO 5.ENCERRAR")
             escolha_principal = int(input())
             # SE O USUARIO ESCOLHER DEPOSITO
             if escolha_principal == 1:
                # LÊ VALOR A SER DEPOSITADO
                print("VALOR DEPOSITADO: ")
                valor_deposito = float (input())
                saldo = saldo + valor_deposito #ATUALIZAR VALOR
                print("NOVO SALDO É: ", saldo)
             elif escolha_principal == 2: #SAQUE
                valor_saque = float (input("DIGITE O VALOR DO SAQUE: "))
                senha_saque = input("DIGITE SUA SENHA:")
                if senha_saque == senha: # SENHA CORRETA 
                   saldo = saldo - valor_saque #SUBTRAI O VALOR DO SALDO
                else:
                   print("SENHA INCORRETA!")
             elif escolha_principal == 3: # SE O USUARIO ESCOLHER PIX
                valor_pix = float (input("DIGITE O VALOR DO PIX: "))
                senha_pix = (input("DIGITE SUA SENHA: "))
                if senha_pix == senha:
                   saldo = saldo - valor_pix
                else:
                   print("Senha incorreta!")
             elif escolha_principal == 4: # SE O USUÁRIO ESCOLHER VISUALIZAR
                senha_extrato = input ("DIGITE SUA SENHA: ")
                if senha_extrato == senha:
                   print("Extrato:", saldo)
                else:
                   print("SENHA INCORRETA!")
             elif escolha_principal == 5: #ENCERRAR
                senha_encerrar = input("DIGITE SUA SENHA: ")
                if senha_encerrar == senha:
                   break
                else:
                   print("SENHA ICORRETA!")
      else:
        print("USUÁRIO OU SENHA INCORRETA")

