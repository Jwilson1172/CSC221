# Joseph Wilson CSC221

# 1. Write a program that takes a string as an input. If the string entered is equal to
# “ITP100”, print “This is equal” to the screen. If the string entered is not equal to
# “ITP100”, print “This is not equal” to the screen.
# Save this code as Question1.py
# Submit Question1.py in Canvas

if __name__ == "__main__":
    # catch input strip leading/lagging spaces and compare edge case
    if input().strip() == "ITP100":
        print("This is equal")
    # respond to all other input
    else:
        print("This is not equal")
