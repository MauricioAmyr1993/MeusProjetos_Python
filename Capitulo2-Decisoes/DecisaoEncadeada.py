nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
if idade>=65:
    print("Paciente COM prioridade: ")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe para a sala AMARELA")
    elif doenca_infectocontagiosa=="NÃO":
        print("Encaminhe para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")
else:
    print("Paciente SEM Prioridade: ")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe para a sala AMARELA")
    elif doenca_infectocontagiosa=="NÃO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")
