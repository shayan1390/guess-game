import random
import os

os.system('cls' or 'clear ')


class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[0m'


print(Color.BLUE +
      "سلام:) \n وقتي حرف سبر باشه يعني حرف و جاش درسته. \n وقتي حرف قرمز باشه يعني حرف درسته ولي تو جاي مناسب "
      "نيست. \n وقتي دو بار اون حرف نوشته شه يعني دو تا از اون حرف تو كلمه هست. \n موفق باشيييي:)")
world = ["dag", "pig", "bag", "egg", "cry", "dad", "mom", "nit", "fun", "sad", "bad", "six", "one", "two",
         "leg", "eye", "sun", "son", "tie", "ice", "ant", "unt", "run", "odd", "out", "big", "new", "now"]
while True:
    TryCount = 0
    answer = random.choice(world)
    print("_" * len(answer))
    while TryCount < 10:
        guess = input(Color.BLUE + "please insert the guess: ")
        if len(guess) != len(answer):
            print("error")
        else:
            if len(guess) == len(answer):
                TryCount += 1
                if guess == answer:
                    print(Color.GREEN + answer)
                    print("you won!!!")
                    break
                else:
                    if answer[0] == guess[0]:
                        print(Color.GREEN + answer[0], end="")
                    elif answer[0] == guess[1]:
                        print(Color.RED + answer[0], end="")
                    elif answer[0] == guess[2]:
                        print(Color.RED + answer[0], end="")
                    if answer[1] == guess[1]:
                        print(Color.GREEN + answer[1], end="")
                    elif answer[1] == guess[0]:
                        print(Color.RED + answer[1], end="")
                    elif answer[1] == guess[2]:
                        print(Color.RED + answer[1], end="")
                    if answer[2] == guess[2]:
                        print(Color.GREEN + answer[2], end="")
                    elif answer[2] == guess[0]:
                        print(Color.RED + answer[2], end="")
                    elif answer[2] == guess[1]:
                        print(Color.RED + answer[2], end="")

            print("")
        if TryCount == 10:
            print(f"{answer} \n you lose.0,0.")
    x = input("do you want play agine??(1.yes 2.no)\n")
    if x == "2":
        print("thank you to play:D\n")
        break
