class Conta:
 def __init__(self, numero, titular, saldo, limite):
      print("Construindo objeto ... {}",format(self))
      self.numero = numero
      self.titular = titular
      self.saldo = saldo
      self.limite = limite

 #from conta import Conta

 #Conta1 = Conta(numero, titular, saldo, limite)

 def extrato(self):
     print("Saldo de {} do titular {}".format(self.saldo, self.titular))
#Conta.extrato(conta)

 def deposita(self, valor):
    self.saldo += valor
#Conta.deposita(conta,valor)

 def saca(self, valor):
    self.saldo -= valor
#Conta.saca(conta,valor)

 def transferencia(self, valor, destino):
    self.saldo -= valor
    destino.deposita(valor)

  #Conta.transferencia(conta,valor,contadestino)

