# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if(user_choice=='r' and computer_choice=='r'):
    print("You both chose same value")
elif(user_choice=='r' and computer_choice=='p'):
    print(f"Computer chose a {computer_choice}")
elif(user_choice=='r' and computer_choice=='s'):
    print(f"Computer chose {computer_choice}")
elif(user_choice=='s' and computer_choice=='s'):
    print("You both chose same value")
elif(user_choice=='s' and computer_choice=='p'):
    print(f"Computer chose a {computer_choice}")
elif(user_choice=='s' and computer_choice=='r'):
    print(f"Computer chose {computer_choice}")
elif(user_choice=='p' and computer_choice=='p'):
    print("You both chose same value")
elif(user_choice=='p' and computer_choice=='r'):
    print(f"Computer chose a {computer_choice}")
elif(user_choice=='p' and computer_choice=='s'):
    print(f"Computer chose {computer_choice}")
else:
    print("you choose value other than r, p, s")

#if(user_choice == computer_choice):
 #   print(f"You chose {user_choice} computer chose {computer_choice} and they match! Yohoo!!")
#elif(user_choice != computer_choice):
 #    print(f"You chose {user_choice} computer chose {computer_choice} and they don't match! Sorry!!")


