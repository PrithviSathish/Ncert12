import random

lot_no = random.choice([1, 2, 3, 4, 5, 6])
if int(input("Enter your lottery number: ")) == lot_no:
    print("Congrats! You have won the lottery!!")

else:
    print("Sorry, you missed the lottery :(. Better luck next time!")
