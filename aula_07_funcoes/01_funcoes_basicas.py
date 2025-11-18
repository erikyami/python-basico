# Aula 07 - Funções

# Definindo a função
def calcular_area_retangulo(largura, comprimento):
    area = largura * comprimento
    return area

# Programa principal
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))

# Chamando a função e guardando o resultado
resultado = calcular_area_retangulo(l, c)

print(f"A área total é de {resultado} m².")