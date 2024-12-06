#LISTA PARA ARMAZENAR OS ALUNOS
alunos = []

while True:
    print("1.Cadastro, 2. Ver relatório, 3. Encerrar")
    decisao = input("escolha uma opção: ")

    if decisao == "1":
        print("Faça o cadatro")
        quantidade_alunos = int(input("Quantidade de alunos: "))

        for _ in range (quantidade_alunos):
            nome = input ("Nome do aluno : ")
            faltas = int(input("Quantidade de faltas: "))

            #COLETAR AS 4 NOTAS
            notas = []
            for i in range (4):
                nota = float(input(f"digite a nota de {i + 1}° bimestre: "))
                notas.append(nota)

                #CALCULAR A MEDIA
            media = sum(notas)/4

                    #DETERMINAR SITUACAO
            if faltas > 30 :
                    situacao = "Reprovado por faltas."
            elif media >= 8.0 and faltas <= 30:
                    situacao = "Aprovado"
            elif media >= 5 and faltas <= 30:
                    situacao = "O aluno está de recuperação"
                    recuperacao = float(input("Nota da recuperação: "))
                    media_final = (media + recuperacao)/2
                    if media_final >= 5:
                        situacao = " Aprovado na recuperação"
                    else:
                        situacao = "Reprovado na recuperação"
            else:
                    situacao = "Reprovado por media"

                #ADICIONAR O ALUNO NA LISTA
            alunos.append([nome, faltas, notas, media, situacao])

            
    elif decisao == "2":
          #MOSTRAR O RELATORIO DE TODOS OS ALUNOS 
          if not alunos:
                print("Ainda não há alunos cadastrados.")
          else:
                print("Relatório dos alunos: ")
                for aluno in alunos:
                      print(f"Nome:{aluno[0]}")
                      print(f"Faltas: {aluno[1]}")
                      print(f"Notas: {aluno[2]}")
                      print(f"Média: {aluno[3]}")
                      print(f"Situação {aluno[4]}/n")
    elif decisao == "3":
          print("Encerrando o programa.")
          break
    else:
          print("Opção inválida. Tente novamente!")