print("======NOTAS ESCOLARES======")
nome = (input("Digite o nome do aluno: "))
ano = (input("Digite o ano do aluno: "))

print("++++ Notas do Primeiro Semestre ++++")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media1 = (nota1 + nota2 + nota3 + nota4) / 2

if media1 >= 7:
    print("Aluno aprovado no primeiro bimestre com sucesso!")

else:
    print("Aluno ficou de recuperação no primeiro bimestre!")

notarec = float(input("Digite a nota da recuperação: "))
media2 = (media1 + notarec) / 2

while media2 and media2 >= 7:
    print("O aluno passou em recuperação no primeiro bimestre")
else:
    print("O aluno não passou na recuperação e foi reprovado no primeiro bimestre")

print("++++ Notas do Segundo Bimestre ++++")

nota5 = float(input("Digite a primeira nota: "))
nota6 = float(input("Digite a segunda nota: "))
nota7 = float(input("Digite a terceira nota: "))
nota8 = float(input("Digite a quarta nota: "))

media3 = (nota5 + nota6 + nota7 + nota8) / 2

if media3 >= 7:
    print("Aluno aprovado no segundo bimestre com sucesso!")
else:
    print("Aluno reprovado no segundo bimestre!")

notarec2 = float(input("Digite a nota da recuperação: "))
media4 = (media3 + notarec2) / 2

while media3 and media4 >= 7:
    print("O aluno passou em recuperação no segundo bimestre")
else:
    print("O aluno não passou na recuperação e foi reprovado no segundo bimestre")
