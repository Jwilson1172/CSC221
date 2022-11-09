# Joseph Wilson CSC221

# 2. Write a program that takes an integer as input. Add 25 to the number that is entered. If
# the new number is greater than 75, print the new number to the screen. If the new
# number is less than 75, print “lower” to the screen.
# Save this code as Question2.py
# Submit Question2.py in Canvas.


if __name__ == "__main__":

    # catch input and conver to int then add 25
    n = int(input) + 25
    # compare n to conditions and respond with appropiate output
    if n > 75:
        print(n)
    else:
        print("lower")
