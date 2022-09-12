print("Entre com números positivos:")
lista = []
while True:
    p = int(input () )
    if p <= 0:
        break
        lista.append(p)
x = int(input("Qual o número a procurar?"))
if x in lista:
    print(x, "pertence à lista")
else:
    print(x, "não pertence à lista")