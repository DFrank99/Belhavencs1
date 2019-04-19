import random

def print_intro():
    print("Welcome valued player, to Le Camel!\n")
    print("You are here to play a game where you voyage with Camel \'Whoms name is Camel'...")
    print("\t In \t The \t Desert! \t OoOOoo~")
    print("To win, you must cross the desert before locals capture you. \n Do you have what it takes?\n ")

print_intro()
# Variables
miles_traveled = 0
thirst = 0
tiredness = 0
local_distance = -20
canteen = 4

def main():

    done = False
    while not done:
        print("A. Drink from your canteen.\nB. Ahead moderate speed.")
        print("C. Ahead full speed.\nD. Stop for the night.")
        print("E. Status check.\nQ. Quit.")

        answer_choice = input("\nThe choice is yours. ")
        if answer_choice == "q":
            print("You did'nt even try.")
            done = True
        # Check stats
        elif answer_choice == "e":
            print("Miles treked: ", miles_traveled)
            print("Canteens left: ", canteen)
            print("Mr. Camel is", tiredness,"% tired")
            print("Locals are", miles_traveled - local_distance," miles behind you.\n")
        # Stop
        elif answer_choice == "d":
            print("Happy happy camel! With happy player, too!")
            print("Sadly the locals are approaching!")
            print("They are catching up by",current_local, " miles.")
            tiredness = 0
            local_distance += random.randrange(7, 14)
        # Full speed
        elif answer_choice == "c":
            print("Onward and upward, Camel!")
            miles = random.randrange(5, 12)
            miles_traveled += miles
            thirst += 1
            tiredness += random.randrange(1, 3)
            local_distance += local_closer
            print("You have traveled", miles)
            print("Natives caught up by",current_local,)
            oasis = random.randrange(1, 20)
            if not done and thirst > 4:
                thirst = 0
                camelTiredness = 0
                canteen = 4
                print("Oh snap, an oasis!")
                print("You fill your canteen and rest ye Mr. Camel")
                print("However, locals continue toward you.\n")
            else :
                print("Full throttle, moving ", miles, "miles")
                print("Man your getting thirsty.")
                print("Locals are still coming.\n")
        # Moderte speed
        elif answer_choice == "b":
            miles = random.randrange(5, 12)
            miles_traveled += miles
            print("You have gone",miles_traveled,"miles.")
            thirst += 1
            tiredness += 1
            local_distance += random.randrange(7, 14)
            oasis = random.randrange(1, 21)
            if not done and thirst > 4:
                thirst = 0
                camelTiredness = 0
                canteen = 4
                print("Oh snap, an oasis!")
                print("You fill your canteen and rest ye Mr. Camel")
                print("However, locals continue toward you.\n")
            else :
                print("You have moved ", miles, "miles")
                print("Man your getting thirsty.")
                print("Locals are still coming.\n")
      # Drink canteen
        elif answer_choice == "a":
            print("Man me thirsty!")
            print("You drink one canteen.")
            if canteen > 0:
                canteen -= 1
                thirst = 0
                print("You have",canteen,"canteens left.")
            # Delirious
            else:
                print("Thinking of water makes you think of water and you H2O while aqua water H2O H2O...")
        else:
            print("I don't understand this.")
        # Died of thirst
        if thirst > 6 :
            print("You was so thirsty THAT EVERYONE DIED.\nTHE END")
            done = True
        # Very thirsty
        elif thirst > 4 :
            print("It's hot and you thirsty! Just sayin...")
        # Dead camel
        if tiredness > 5 :
            print("Your camel died of exhaustion!")
            print("Without Mr. camel, the sun burns you to death along with Mr. Camel's carcass")
            done = True
        # Tired
        elif tiredness > 5 :
            print("Bro, Camel out here stupid tired.")
        # Local travel
        if miles_traveled - local_distance <= 0 :
            print("You done got caught by the locals!")
            print("You suck.")
            done = True
        elif miles_traveled - local_distance < 15 :
            print("Halucinations are way far out, like, I can see space...in the desert.")
            print("Locals are still chasing.")
        # Win
        if miles_traveled >= 200 :
            print("Congratulations! You have crossed the entire desert!")
            print("You win!")
            print()
            done = True

if __name__=='__main__':
    main()
