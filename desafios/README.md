# Lista de Desafios Práticos

Bem-vindo à área de desafios! Aqui você encontrará exercícios propostos para praticar "além da sala de aula".
A programação só se aprende praticando, então tente resolver cada um deles sem olhar o gabarito imediatamente.

---

## Aula 01: Fundamentos
**Desafio: O Gerador de Crachá**
Crie um programa que peça ao usuário: Nome, Cargo e Salário.
O programa deve limpar a tela e exibir um crachá formatado com bordas, e o salário deve aparecer formatado (ex: converter ponto para vírgula se possível ou apenas adicionar o R$).

**Requisitos:**
* Usar `input()` para ler os dados.
* Usar *f-strings* para formatar a saída.
* Criar uma borda visual com caracteres (ex: `==========`).

---

## Aula 02: Operadores
**Desafio: Conversor de Mundos**
Escreva um programa que receba um valor em **Reais (R$)** e uma temperatura em **Celsius (°C)**.
O programa deve converter e exibir:
1. O valor em Dólares e Euros (considere taxas fixas, ex: 5.50 e 6.20).
2. A temperatura em Fahrenheit (Fórmula: `F = C * 1.8 + 32`).

**Requisitos:**
* Usar operadores aritméticos (`*`, `/`, `+`).
* Limitar as casas decimais para 2 dígitos.

---

## Aula 03: Condicionais
**Desafio: Verificador de Triângulos**
Peça ao usuário o comprimento de 3 retas (lados). O programa deve responder:
1. Se esses lados **podem** formar um triângulo (Soma de dois lados > terceiro lado).
2. Se formarem, qual o tipo: **Equilátero** (3 iguais), **Isósceles** (2 iguais) ou **Escaleno** (todos diferentes).

**Requisitos:**
* Usar `if`, `elif`, `else` aninhados.
* Usar operadores lógicos `and` ou comparações encadeadas.

---

## Aula 04: Repetição
**Desafio: A Urna Eletrônica**
Crie um menu de votação:
`1. Candidato A | 2. Candidato B | 3. Branco | 0. Encerrar`
O programa deve ficar pedindo votos infinitamente. Quando o usuário digitar 0, o loop para e o sistema exibe o total de votos de cada um e quem venceu.

**Requisitos:**
* Usar `while True`.
* Usar contadores (`votos_a += 1`).

---

## Aula 05: Listas
**Desafio: O Analista de Números**
Peça para o usuário digitar 5 números inteiros e armazene-os em uma lista.
Ao final, mostre:
1. A lista completa.
2. O maior e o menor número (sem mudar a ordem da lista original).
3. A soma de todos os valores e a média.

**Requisitos:**
* Usar métodos de lista (`append`).
* Funções nativas (`max`, `min`, `sum`).

---

## Aula 06: Dicionários
**Desafio: Contador de Vogais**
O usuário digita uma frase longa (pode ser um texto).
O programa deve contar quantas vezes cada vogal (A, E, I, O, U) apareceu na frase e armazenar isso em um dicionário.

**Saída esperada:** `{'a': 5, 'e': 2, 'i': 0...}`

**Requisitos:**
* Usar dicionário para contagem.
* Iterar sobre a *string* da frase.

---

## Aula 07: Funções
**Desafio: Calculadora de Tinta**
Crie uma função chamada `calcular_latas(largura, altura, rendimento)`.
O usuário digita o tamanho da parede e quanto a tinta rende por litro. O programa deve retornar quantas latas de tinta ele precisa comprar.

**Requisitos:**
* Definição de função com parâmetros `def`.
* Retorno de valor `return`.
* Lógica de arredondamento (se precisar de 2.1 latas, tem que comprar 3).

---

## Aula 08: Módulos
**Desafio: Simulador da Mega-Sena**
Gere 6 números aleatórios entre 1 e 60 para um jogo da Mega-Sena.
Os números **não podem se repetir** e devem ser exibidos em **ordem crescente**.

**Requisitos:**
* Importar módulo `random`.
* Usar lógica para evitar repetidos (ou usar `random.sample`).

---

## Aula 09: Arquivos
**Desafio: Log de Acesso Persistente**
Pergunte o nome do usuário.
O programa deve abrir um arquivo `log.txt` e adicionar uma linha com o texto: *"O usuário [NOME] acessou o sistema as [HORA]"*.
Não apague os registros anteriores!

**Requisitos:**
* Manipulação de arquivos (`open`, `write`).
* Modo `append` ('a').

---

## Aula 10: Exceções
**Desafio: Entrada Blindada**
Crie um programa que pede dois números para dividir.
Se o usuário digitar uma letra, o programa diz "Digite apenas números" e pede de novo.
Se o usuário tentar dividir por zero, o programa avisa "Não existe divisão por zero" e pede de novo.
O programa só para quando a conta der certo.

**Requisitos:**
* `try`, `except` (`ValueError`, `ZeroDivisionError`).
* Loop `while`.

---

## Aula 11: Orientação a Objetos
**Desafio: A Batalha RPG**
Crie uma classe `Heroi` com atributos: `nome`, `vida` e `ataque`.
Crie um método `atacar(outro_heroi)` que retira vida do oponente baseada no ataque.
Simule uma luta entre dois objetos dessa classe no terminal.

**Requisitos:**
* Classe, Construtor (`__init__`).
* Métodos e alteração de atributos (`self`).

---

## Projeto Final (Aula 12)
**Desafio Master: Gerenciador de Tarefas (To-Do List)**
Junte tudo o que aprendeu! Crie um sistema que:
1. Tenha um menu (Adicionar, Listar, Concluir, Sair).
2. Salve as tarefas em um arquivo `.txt` automaticamente.
3. Ao abrir o programa, carregue as tarefas salvas.
4. Trate erros se o arquivo não existir.

**Boa sorte e bom código!**