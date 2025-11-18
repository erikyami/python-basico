# Aula 08 - Jogo de Adivinhação
import random # Importando módulo nativo

numero_secreto = random.randint(1, 10) # Aleatório entre 1 e 10
palpite = 0

print("Tente adivinhar o número entre 1 e 10!")

while palpite != numero_secreto:
    palpite = int(input("Seu palpite: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
    elif palpite < numero_secreto:
        print("É maior...")
    else:
        print("É menor...")