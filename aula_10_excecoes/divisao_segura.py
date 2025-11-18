# Aula 10 - Divisão Segura

try:
    n1 = float(input("Numerador: "))
    n2 = float(input("Denominador: "))
    
    divisao = n1 / n2
    print(f"Resultado: {divisao}")

except ZeroDivisionError:
    print("Erro: Impossível dividir por zero!")
except ValueError:
    print("Erro: Digite apenas números!")