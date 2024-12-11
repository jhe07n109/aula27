#DECLARAR UMA FUNÇÃO
def saudacoes (hora_do_dia): #EXIBIR A SAUDAÇÃO CORRESPONDENTE A HORARIOS
     #DAR BOM DIA
 
   if hora_do_dia >= 0 and hora_do_dia <= 12:
    print("BOM DIA!")
   elif hora_do_dia >= 13 and hora_do_dia <= 18:
     print("BOA TARDE!")
   else:
     print("BOA NOITE!")

    #FORA DA FUNÇÃO
resposta = int(input("DIGITE QUE HORAS SÃO: "))
saudacoes (resposta)
 
  