#Exercicio Hospital

pacienteNome = input("Nome do Paciente: ")
pacienteIdade= int(input("Idade do paciente: "))
risco = input("Tem risco?(S/N): ").upper()

if risco != "S" and risco != "N" :
    risco = input("Digite apenas (S/N): ").upper() 
else:
    if pacienteIdade < 15 or pacienteIdade > 60 :
        print("O Paciente esta em grupo de risco")
    elif risco == "S":
        print("Grupo de Risco")
    else:
        print("Esta sem nenhum problema")
