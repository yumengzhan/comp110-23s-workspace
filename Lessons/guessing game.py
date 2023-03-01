"""Ask user for numnber, give hints about number if wrong"""

SECRET: int = 10
guess: int = int(input("Guess a number!"))
playing:bool = True

while playing:
    if guess==SECRET:
        print("Correct! You did it!")
        playing = False
    else:
        if guess % 2 == 1:
            print("Your answer is odd. The answer is even.")
        if guess< SECRET:
            print("too low!")
        else:#guess is greater than SECRET
            print("too high!")
        guess= int(input("Wrong guess. Try again!"))

def hello_n(n: int) -> int:
    """A silly example function"""
    return "hello " + str(n)

print(hello_n(3))


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

        

