"""EX01 - One-Shot Wordle - Loops!"""
__author__ = "730619940"

SECRET: str = "python"
length: str= len(SECRET)
guess: str = input(f"What is your {length} -letter guess? ")
if (len(guess) != len(SECRET)):
        guess = input(f"That was not {length} letters! Try again: ")
playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_idx: int=0



stored_variable: str=""


while playing:
    # Green Box
    while guess_idx < len(SECRET):
        if(guess[guess_idx]==SECRET[guess_idx]):
            stored_variable=stored_variable + GREEN_BOX
        # Yellow Box
        else:
            Character_exists: bool=False
            Alternate_index:int=0
            while (Character_exists is False) and (Alternate_index<len(SECRET)):
                if (SECRET[Alternate_index] == guess[guess_idx]):
                    Character_exists=True    
                else:       
                    Alternate_index=Alternate_index+1        
            if(Character_exists is True):
                stored_variable=stored_variable + YELLOW_BOX
            else:
                stored_variable=stored_variable + WHITE_BOX
        guess_idx = guess_idx+1
    print(stored_variable)
    if (guess != SECRET):
        print("Not quite. Play again soon!")
    else:
        print("Woo! You got it!")
    playing = False

    

    

