"""EX01 - One-Shot Wordle - Loops!"""
__author__ = "730619940"

secret: str = "python"
length: int = len(secret)
guess: str = input(f"What is your {length}-letter guess? ")

while (len(guess) != len(secret)):  # The length of the guess is not equal to that of the secret word
    guess = input(f"That was not {length} letters! Try again: ")

playing: bool = True

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

guess_idx: int = 0

stored_variable: str = ""

while playing:
    # Green Box if the character exists and in the right position
    while guess_idx < len(secret):
        if (guess[guess_idx] == secret[guess_idx]):
            stored_variable = stored_variable + green_box
        # Yellow Box if the character exists in the secret word but in wrong position
        else:
            character_exists: bool = False
            alternate_index: int = 0
            while (character_exists is False) and (alternate_index < len(secret)):
                if (secret[alternate_index] == guess[guess_idx]):
                    character_exists = True    
                else:       
                    alternate_index = alternate_index + 1        
            if (character_exists is True):
                stored_variable = stored_variable + yellow_box
            else:  # White box if the character does not exist
                stored_variable = stored_variable + white_box
        guess_idx = guess_idx + 1
    print(stored_variable)
    if (guess != secret):
        print("Not quite. Play again soon!")
    else:
        print("Woo! You got it!")
    playing = False