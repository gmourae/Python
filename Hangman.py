import random

#Desenvolvido por Gabriel de Moura em 02/10/2023

# Lista de palavras para o jogo
word_list = ["python", "forca", "programa", "computador", "jogo", "desenvolvedor", "inteligencia-artificial", "deafio"]

# Funcao para escolher uma palavra da lista
def choose_word():
    return random.choice(word_list)

# Funcao para mostrar o atual estado da palavra
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Funcao para rodar o jogo Forca
def play_hangman():
    word = choose_word()
    guessed_letters = []
    max_attempts = 6  # e possivel alterar a quantidade maxima de tentativas
    attempts = 0 

    print("Bem-vindo ao jogo de forca!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Adivinhe uma letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Digite apenas uma letra.")
            continue

        if guess in guessed_letters:
            print("Você já usou esta letra.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print(f"Errado! Tentativas restantes: {max_attempts - attempts}")

        print(display_word(word, guessed_letters))

        if set(word).issubset(set(guessed_letters)):
            print("Parabéns! Você acertou a palavra.")
            break

        if attempts >= max_attempts:
            print(f"Game over! A palavra era '{word}'.")
            break

if __name__ == "__main__":
    play_hangman()