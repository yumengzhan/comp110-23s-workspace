"""Choose your own adventure."""
__author__ = "730619940"


from random import randint
points: int = 1
player: str = "name of the player"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def main() -> None:
    global points
    greet()
    user_action:str = input("What is your choice? End the experience or start new?")
    while user_action != "End the experience":
        points=1
        guessing()
        user_action: str = input("What is your choice? End the experience, continue, or start new?")
    print(f"Goodbye "+ player+ f"! You got {points} points.")


def greet() -> None:
    print("Welcome to number guessing game! The computer will be generating a random number. We will see when you can get the number, and you will get the points of your guessing times.")
    global player
    player = input("What is your name?")


def guessing() -> None:
    global points
    global player
    userchoice:int=int(input("Enter your guess:"))
    computerchoice:int = randint(1,10)
    while computerchoice != userchoice:
        print (guessingtimes(points))
        print (yellow_box)
        points += 1
        userchoice = int(input("Try again:"))
    print(f"Congratulations! You did it in {str(points)} turn.")
    print(green_box)


def guessingtimes(x:int) ->int:
    global player
    return (f"{player}, this is your {points} try." )


if __name__ == "__main__":
    main()