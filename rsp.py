import random
import re
class Myrps:
    def Rps(self):
        while (1 < 2):
            print("\n")
            print("Rock, Paper, Scissors - Shoot!")
            userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
            if not re.match("[SsRrPp]", userChoice):
                print("Please choose a letter:")
                print("[R]ock, [S]cissors or [P]aper.")
                continue
            print("My Choice: " + userChoice)
            choices = ['R', 'P', 'S']
            opponenetChoice = random.choice(choices)
            print("computer Choice: " + opponenetChoice)
            if opponenetChoice == str.upper(userChoice):
                print("Tie! ")
            elif opponenetChoice == 'R' and userChoice.upper() == 'S':
                print("Scissors beats rock, Computer win! ")
                continue
            elif opponenetChoice == 'S' and userChoice.upper() == 'P':
                print("Scissors beats paper! computer win! ")
                continue
            elif opponenetChoice == 'P' and userChoice.upper() == 'R':
                print("Paper beat rock, computer win! ")
            else:
                print("You win!")
obj=Myrps()
obj.Rps()

