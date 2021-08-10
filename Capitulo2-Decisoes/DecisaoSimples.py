nome=input(("Digite o nome: "))
idade=int(input("igite a idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
print("O paciente " + nome + " Possuí atendimento prioritário? " + prioridade)