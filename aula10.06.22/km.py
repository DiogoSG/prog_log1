Km = int(input("Digite a distância: "))
horas = int(input('Digite o tempo de viagem:' ))
vel = Km / horas
if vel >= 110:
    print("Velocidade média é de %d"%vel)
elif vel < 110:
    print("Velocidade média menor que 110Km/h")
