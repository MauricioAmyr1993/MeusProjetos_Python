nome=input("Digite o nome do aluno: ")
ano=(input("Digite o ano em que está o aluno: "))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
nota4=float(input("Digite a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/2
if media>=7.0:
    print("Aluno aprovado!")
else:
    print("Aluno Reprovado")
