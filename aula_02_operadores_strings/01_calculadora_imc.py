# Aula 02 - Calculadora de IMC
print("=== Calculadora de IMC ===")

# Convertendo a entrada (string) para float (número decimal)
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo: Peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

# Exibindo com 2 casas decimais usando :.2f
print(f"Seu Índice de Massa Corporal é: {imc:.2f}")