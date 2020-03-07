nivelDeAcesso = input("Insira seu nivel de Acesso(ADM/USER/GUEST): ").upper()
genero = input("Insira seu genero(M/F): ").upper()

while nivelDeAcesso != "ADM" and nivelDeAcesso != "USER" and nivelDeAcesso != "Guest":
    nivelDeAcesso = input("Insira apenas seu nivel de Acesso! (ADM/USER/GUEST):")

while genero != "M" and genero != "F" :
    genero = input("Insira apenas o seu genero(M/F): ")

if nivelDeAcesso == "ADM" and genero == "M":
    print("Ola Administrador")
else:
    print("Ola Administradora")

if nivelDeAcesso == "USER" and genero == "M":
    print("Ola Usuario")
else:
    print("Ola Usuaria")
    
if nivelDeAcesso == "GUEST" and genero == "M":
    print("Ola Desconhecido")
else:
    print("Ola Desconhecida")