
alunos = []
cont = 0
quantidadealunos = int(input("quantidade de alunos: "))

while cont <= quantidadealunos:
     nome = input("nome ")
     alunos.append(nome)
     faltas = int(input("digite a quantidade de faltas "))

     print("digite a nota do aluno: ")
     nota1 = float(input())
     nota2 = float(input())
     nota3 = float(input())
     nota4 = float(input())
     media = (nota1 + nota2 + nota3 + nota4) /4


     if media >= 8 and faltas <= 30:
          situacao ="O aluno (A) foi aprovado"
     elif media >= 5 and faltas <= 30: 
          situacao = "o aluno esta de recuperação"
          recuperacao= float (input("nota de recuperação:"))
          calculodarecuperacao= (10-media)
          if recuperacao > calculodarecuperacao:
               situacao = "aprovado na recuperação"
          else:
               situacao = "reprovado na recuperação"
     else:
          situacao ="reprovado"
     cont += 1

     print ("nome:", nome)
     print("media:", media)
     print("faltas:", faltas)
     print("esta: ", situacao)