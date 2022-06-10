idade = int(input("Digite a idade do aluno: "))
altura = float(input("Digite a altura do aluno: "))
aluno = 0
resultado = aluno
while altura > 0:
 aluno += 1
 if altura <= 1.50 and idade >= 13:
     resultado += aluno
 elif altura == 0:
  print(aluno)
