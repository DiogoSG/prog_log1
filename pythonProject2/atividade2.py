N1 = int(input("Escreva a nota: "))
N2 = int(input("Escreva a nota: "))
N3 = int(input("Escreva a nota: "))
N4 = int(input("Escreva a nota: "))
if N1 and N2 and N3 and N4 > 10:
    print("A nota deve ser menor que 10")
nota = N1 + N2 + N3 + N4
media = nota // 4
print ('a media desse aluno é:', media)

if media >= 7:
    print("Aluno aprovado")
elif media == 5:
    print("Aluno de exame final")
else:
    print("Aluno reprovado")

