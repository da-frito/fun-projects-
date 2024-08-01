import random

words_in_stock = ['python' , 'library' , 'stupid' , 'smart']
guessed_one = random.choice(words_in_stock)
display_state = ["_"]*len(guessed_one)
tries = 9

def display_word():
    print(" ".join(display_state))

while tries > 0 :
    display_word()
    guess = input("guess a letter: ").lower()

    if guess in guessed_one:
        for index , letter in enumerate(guessed_one):
            if letter ==  guess:
                display_state[index] = guess
    else:
        tries -= 1
        print(f"nuh uh , u got {tries} more tries ")
    
    if "_" not in display_state:
        print("well done")
        break
else:
    print(f"GGs word was {guessed_one}")