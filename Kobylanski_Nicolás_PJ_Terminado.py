import random    #Importo la librería "random".
import time      #Importo la librería "time".

def guess_number(is_replay = False, game_start = ""): 
    """
    Creo la función principal que contiene el código del juego con los 
    parámetros is_replay y game_start para implementar rejugabilidad.
    """
    def game_replay():
        """
        Creo una función secundaria llamada game_replay para acortar código a la hora
        de querer repetir el juego.
        """
        game_replay = input("Do you wish to play again? type y for yes, n for no: ")
        if game_replay == "y":
            guess_number(is_replay=True)
        elif game_replay == "n":
            print("See you soon!")
            exit
        else:
            exit

    try:
        #Si el usuario desea volver a jugar, no le saltará esta línea de diálogo.
        if is_replay == False:         
            game_start = input("Do you want to play a guessing game? type y for yes, n for no: ").lower()

        #El bucle principal que contiene el juego.
        if game_start == "y" or is_replay == True:
            ai_gameplay = int(input("Do you wish to play the game or, do you want an AI to guess the number? Type 1 to play it yourself, and 2 for an AI to play it: "))
            if ai_gameplay == 1:
                #Defino las variables de dificultad, es decir, los rangos mínimo y máximo para adivinar el número.
                diffEasy = [0, 10]
                diffMedium = [0, 50]
                diffHard = [0, 100]
                selectDifficulty = int(input("Please select 1 of 3 difficulties. 1 for easy, 2 for medium, and 3 for hard: "))

                #Dependiendo de la dificultad elegida, habrá que adivinar entre más o menos números.
                if selectDifficulty == 1:
                    minimum, maximum, max_attempts = diffEasy[0], diffEasy[1], 5
                elif selectDifficulty == 2:
                    minimum, maximum, max_attempts = diffMedium[0], diffMedium[1], 7
                elif selectDifficulty == 3:
                    minimum, maximum, max_attempts = diffHard[0], diffHard[1], 9
                else:
                    print("You chose an invalid difficulty, so you now you will have to guess a number between 0 and 1000000.")
                    minimum = 0
                    maximum = 1000000
                    max_attempts = 1

                #Defino el resto de variables necesarias para el juego, como el número secreto, el input del usuario y los intentos.
                secret_number = random.randint(minimum, maximum)
                user_guess = int(input(f"Guess the number between {minimum} and {maximum} with both ends included (You have {max_attempts} attempts): "))
                attempts = 1
                    
                #Creo un bucle while para que se ejecute hasta que el usuario adivine el número secreto.
                while user_guess != secret_number:
                    attempts += 1
                    max_attempts -= 1

                    if max_attempts == 0:
                        print("You lost! You have no remaining attempts :(")
                        game_replay()
                    elif user_guess > maximum or user_guess < minimum:
                        print(f"Please enter a number between {minimum} and {maximum}.")
                        user_guess = int(input(" "))
                    elif user_guess < secret_number:
                        print(f"The number is higher. You have {max_attempts} attempts remaining.")
                        user_guess = int(input(" "))
                    else:
                        print(f"The number is lower. You have {max_attempts} attempts remaining.")
                        user_guess = int(input(" "))

                #Una vez el usuario haya acertado el número, se sale del bucle while y le sale un breve mensaje y tiene la opción de volver a jugar.
                print(f"Congratulations! You guessed the correct number: {secret_number}, and took {attempts} attempts!")
                game_replay()

            #Código para que la máquina adivine el número mediante un algoritmo simple.
            elif ai_gameplay == 2:
                attempts = 0
                minimum = int(input("Enter a minimum number for the AI to guess: "))
                maximum = int(input("Enter a maximum number for the AI to guess: "))
                secret_number = random.randint(minimum, maximum)

                #Bucle while igual que para cuando juega el usuario.
                while True:
                    #Las variables cambian en cada intento para que el número que adivine la máquina sea el más óptimo.
                    ai_guess = (maximum+minimum)//2
                    print(f"AI guessed {ai_guess}")
                    #El time.sleep crea un delay entre cada intento de la máquina para darle una sensación de realismo.
                    time.sleep(0.25)
                    attempts += 1

                    if secret_number - ai_guess == 1:
                        print("Too low!")
                        minimum += 1
                    elif ai_guess < secret_number:
                        print("Too low!")
                        minimum = ai_guess                
                    elif ai_guess > secret_number:
                        print("Too high!")
                        maximum = ai_guess
                    else:
                        print(f"The AI guessed the number in {attempts} attempts!: {secret_number}")
                        break

                game_replay()

            else:
                ("Please enter a valid input")
                guess_number(is_replay=True)
        
        else:
            print("See you soon!")
            exit

    #El "except ValueError" se utiliza en caso de que el input del usuario no sea un número entero.
    except ValueError:
        print("Please enter a valid input")
        guess_number(is_replay=True)


#Llamo la función.
if __name__ == "__main__":      
    guess_number()


