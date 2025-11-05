
# 📘 Assignment: Games in Python

## 🎯 Objetivo

Construir dois mini-jogos em Python (Hangman e Guess the Number) para praticar manipulação de strings, loops, condicionais, funções simples e seleção aleatória.

## 📝 Tarefas

### 🛠️ Hangman

#### Description
Implementar o clássico jogo da forca. O programa escolhe uma palavra aleatória e o jogador tenta adivinhar letra por letra antes que as tentativas acabem.

#### Requirements
Completed program should:

- Selecionar aleatoriamente uma palavra de uma lista pré-definida
- Mostrar o progresso da palavra como espaços com sublinhados (ex: `_ _ a _`)
- Aceitar apenas uma letra por tentativa e validar entrada (ignorar múltiplos caracteres ou números)
- Indicar letras já tentadas e não permitir repeti-las
- Contar e exibir o número de tentativas restantes para erros
- Finalizar com mensagem de vitória ao completar a palavra
- Exibir mensagem de derrota mostrando a palavra correta ao acabar as tentativas
- Usar `random.choice` para seleção de palavra

### 🛠️ Guess the Number

#### Description
Criar um jogo onde o computador escolhe secretamente um número dentro de um intervalo e o jogador tenta adivinhar recebendo dicas (maior/menor) até acertar.

#### Requirements
Completed program should:

- Gerar número aleatório entre 1 e 100
- Ler palpites do usuário até acertar ou atingir limite opcional de tentativas
- Exibir dica "Mais alto" ou "Mais baixo" após cada tentativa
- Contar número total de palpites e exibir ao final
- Tratar entradas inválidas (não numéricas ou fora do intervalo) sem quebrar o programa
- Perguntar se o jogador quer jogar novamente ao terminar (loop de reinício)
- Organizar lógica principal em uma função (ex: `play_game()`)
