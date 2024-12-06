
alunos = [] #alunos
notas= [] #notas dos alunos
# menu de situacao de alunos
while True:

     print ("1.cadastro, 2.ver relatorio, 3.encerrar")
     decisao= input() #numero de cadastro
     #cadastro do aluno
     if decisao =="1":
          print("faça o cadastro: ")
          quantidadealuno= int (input("quantidade de aluno: "))
          cont = 0
          situacao = ""
          while cont < quantidadealuno:
               nome = input("nome do aluno: ")
               #ler notas e faltas
               faltas = int(input("quantidades de faltas: "))
               #4 notas
               for i in range(4):
                    notas.append(float(input(f"digite a nota do {i+1} bimestre")))

                    #calculo da media

               media = (notas[0] + notas[1] + notas[2] + notas[3]) /4
                    #aprovado, recuperacao, reprovado
               if faltas > 30:
                    situacao =" aluno esta reprovado por falta"
               elif media >= 8 and faltas <= 30: 
                    situacao = "apOrovado"
               elif media >= 5 and faltas <= 30:
                    situacao = "recuperação"
                    recuperacao= float (input("nota da recuperação: "))
                    calculodarecuperacao= (10-media)
                    if recuperacao > calculodarecuperacao:
                         situacao = "aprovado na recuperacao"
                    else:
                         situacao = "reprovado na recuperacao"
               else:
                    situacao = "reprovado"

                    alunos.append({nome, faltas, notas, media, situacao}) #guardando
               notas = []
               cont += 1
                    
     #relatorio
     elif decisao == "2":
          cont += 1
          if not alunos : #se nao tiver dados do aluno
               print("ainda nao tem dados de um aluno")
               #relatorio do aluno
          for i in alunos:
               print(f"nome do aluno{i[0]}")
               print(f"faltas:{i[1]}")
               print(f"notas:{', '.join(map(str, i[2]))}")
               print(f"media:{i[3]}")
               print(f"situacao{i[4]}")
     #encerramento
     elif decisao == "3": 
               print("the end")
               break 
     else:
          print("digite um valor valido")