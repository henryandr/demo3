"""Juego de adivinar un número entre 0 y 100, el juego tiene 3 opciones:"""
#Importa la librería random"""

from random import randint

# La función menu imprime en pantalla las opciones del juego 


def menu() -> str:
    print("G. Guess\nH. Help\nE. Exit")
    option = input("Please choose your option >> ")
    return option


#La función help imprime en pantalla las opciones de ayuda 


def menu_help() -> str:
    print("If you choose a help, you will loose 2 attempts")
    print("1. Lower or higher\n2. Exit")
    option = input("Choose your option .. ")
    return option

#Función que imprime los intentos restantes y los números que ya se han ingresado

def game_state(attempts, numbers) -> str:
    print(f"You have {attempts} attempts. Good luck...!")
    if len(numbers) != 0:
        print(f"Numbers already entered: {numbers}")

# Función principal del juego


def main():
    attempts = 10
    flag_win = False
    option = ''
    numbers = []
    print("Try to guess a number between 0 y 100")
    while attempts > 0 and not flag_win and option.lower() != 'e':
        game_state(attempts, numbers)
        option = menu()
        if option.lower() == 'g':
            random_number = randint(0, 100)
            guess_number = int(input("Enter your number >> "))
            numbers.append(guess_number)
            if random_number == guess_number:
                print("Congratulations, you win...!")
                flag_win = True
            else:
                print("You failed...!\n")
                attempts -= 1
        elif option.lower() == 'h':
            help_option = menu_help()
            if help_option == '1':
                attempts -= 1
                if random_number > guess_number:
                    print("\nThe number is higher\n")
                else:
                    print("\nThe number is lower\n")
                print("You loose another attempt\n")
            elif help_option == '2':
                attempts -= 1
                print("You only lost 1 attempt\n")
        elif option.lower() == 'e':
            print("Bye...!")


# Crea la función principal
if __name__ == '__main__':
    main()
