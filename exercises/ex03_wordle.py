"""EX03 - Wordle"""
__author__ = "730619940"

def contains_char(searchword:str, singlechar:str) -> bool:
    """Searching a single character in a word"""
    assert len(singlechar) == 1
    i=0
    while i<=len(searchword)-1:
        if searchword[i] == singlechar:#test if the char is in the word
            return True
        i=i+1
    return False

def emojified (guess:str,secret:str) -> str:
    """Checking if the guess word matches the secret word"""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    guess_idx: int=0
    result: str=""
    while guess_idx<=len(guess)-1:
        test: bool = contains_char(secret, guess[guess_idx])
        if guess[guess_idx] == secret[guess_idx] and test:#if the char in the guess word matches the char in the secret
            result = result + green_box
        else:
            if guess[guess_idx] != secret[guess_idx] and test:# exists but in wrong place
               result = result + yellow_box
            else:
                result = result + white_box
        guess_idx=guess_idx+1
    return result

def input_guess(num:int) -> str:
    """Checking the lenghth of the guess word"""
    guess = input(f"Enter a {num} character word: ")
    while num!=len(guess):
        guess = input(f"That wasn't {num} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turntimes:int=1
    maxturns: int=6
    secret:str = "codes"
    while turntimes <= maxturns:#when trying times is less than the max
        print(f"=== Turn {turntimes}/{maxturns} ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        if guess == secret:
            print(f"You won in {turntimes}/{maxturns} turns!")
                       
        print(result)
        turntimes = turntimes+1
    if turntimes == maxturns + 1:
        print(f"X/{maxturns} - Sorry, try again tommorow!")
    
if __name__ == "__main__":
    main()
