# Aula 11 - Introdução a POO

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositado R${valor}. Saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Sacado R${valor}. Saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente!")

# Testando a classe
conta = ContaBancaria("Francisco", 100)
conta.depositar(50) # Saldo vai para 150
conta.sacar(30)     # Saldo vai para 120