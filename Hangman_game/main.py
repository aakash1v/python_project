import random
import time

def main():
    global count
    global display
    global word
    global already_gussed
    global length
    global play_game
    words_to_guess = ['apple','banana','mango','guava','papaya','orange','grapes']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display= '_'*length
    already_gussed = []
    play_game= ""


    #Initial step to invite in the game :
    print("\n------------------ Welcome to Hangman game --------------\n")
    name = input("Enter the name : ")
    print(f"Hello {name}, ! Best of luck...")
    time.sleep(2)
    print("The game is about to start \nLet's play Hangman!")
    print('Guess the fruit...\n')
    hangman()


# A loop to re-execute the game when the first round ends..
def play_loop():
    global play_game
    play_game = input("Do u want to play again ?? (y = yes/n = no) :")
    while play_game not in ['y','Y','n','N']:
        play_game = input("Do u want to play again ?? (y = yes/n = no) :")
    
    #conditions....
    if play_game.lower().startswith('y'):
        main()
    elif play_game.lower() == 'n':
        print('Thank you for playing ! We are excepting u back again  !!')
        exit()

# Initializing all the conditions required fo the game :
def hangman():
    global count
    global display
    global word
    global already_gussed
    global play_game
    limit = 5
    guess = input("This is the Hangman word : "+ display + " Enter your guess : \n")
    guess = guess.strip()

    while (len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= '9'):
        print('Invalid input. Try a letter\n')
        guess = input("This is the Hangman word : "+ display + " Enter your guess : \n")


    if guess in word:
        already_gussed.extend(guess)
        index= word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')

    elif guess in already_gussed:
        print("Try another letter. \n")

    # displaying if guess is incorrect......
    else:
        count +=1

        if count ==1:
            print("   ____\n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  " __|__\n")
            print("Wrong guess. "+ str(limit - count) + " guess remaining\n")
            
        elif count ==2:
            time.sleep(1)
            print("   ____\n"
                  "   |     | \n"
                  "   |     |\n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  " __|__\n")
            print("Wrong guess. "+ str(limit - count) + " guess remaining\n")
            
        elif count ==3:
            time.sleep(1)
            print("   ____\n"
                  "   |     | \n"
                  "   |     |\n"
                  "   |     | \n"
                  "   |     \n"
                  "   |     \n"
                  "   |     \n"
                  " __|__\n")
            print("Wrong guess. "+ str(limit - count) + " guess remaining\n")
            
        elif count ==4:
            time.sleep(1)
            print("   ____\n"
                  "   |     | \n"
                  "   |     |\n"
                  "   |     | \n"
                  "   |     o \n"
                  "   |     \n"
                  "   |     \n"
                  " __|__\n")
            print("Wrong guess. "+ str(limit - count) + " guess remaining\n")
            
        elif count ==5:
            time.sleep(1)
            print("   ____\n"
                  "   |     | \n"
                  "   |     |\n"
                  "   |     | \n"
                  "   |     o \n"
                  "   |    /|\ \n"
                  "   |    / \ \n"
                  " __|__\n")
            print("Wrong guess. "+ str(limit - count) + " guess remaining\n")
            print('The word was : ',already_gussed,word)
            play_loop()

            
    if word == '_'*length:
        print('Congrats! u have gussed the word correctly!')
        play_loop()
    
    elif count !=limit:
        hangman()

main()


    
