# Aula 09 - Diário de Bordo

texto = input("Escreva uma anotação para salvar no arquivo: ")

# 'a' (append) adiciona conteúdo sem apagar o anterior
# 'encoding=utf-8' garante que acentos funcionem
with open("notas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(texto + "\n")

print("Sucesso! Verifique o arquivo 'notas.txt' na pasta.")