N1 = int(input("Digite um numero: "))
N2 = int(input("Digite um numero: "))
N3 = int(input("Digite um numero: "))

if N1 > N2 or N1 > N3:
    print(N1)
elif N2 > N3 or N2 > N1:
    print(N2)
else:
    print(N3)
