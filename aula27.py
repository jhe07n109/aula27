uantidadealunos =- int(input("quantos alunos deseja cadrastar?"))
alunos = input("nome do aluno (a):")
print("digite a nota do aluno: ")

cont = 0
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

faltas = int(input("digite a quantidade de faltas"))

media = (nota1 + nota2 + nota3 + nota4) /4
 
if media > 8 and faltas <= 30:
     print("O aluno (A)",alunos ,"foi aprovado")
elif media >= 5 and faltas <= 30: 
     print("o aluno esta de recuperação")
     recuperacao= float (input("nota de recuperação:"))
     calculodarecuperacao= (10-media)
     if recuperacao > calculodarecuperacao:
        print("aprovado na recuperação")
     else:
        print("reprovado na recuperação")
else:
        print("reprovado")

