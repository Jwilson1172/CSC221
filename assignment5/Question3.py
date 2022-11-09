# Joseph Wilson

# 3. Write a program that takes 3 integers as input. Compute the average of the 3 values. If
# the average is greater than 25 display “larger”. If the average is lower than or equal to
# 25 display “lower than or equal”.
# Save this code as Question3.py
# Submit Question3.py in Canvas.


if __name__ == "__main__":
    # create list to store values
    d = []
    # gather inputs
    for i in range(3):
        d.append(int(input()))

        # sanity check
        assert isinstance(d[i], int)
    # find sum
    s = sum(d)
    # find average of 3
    avg = s / 3
    # filter more restrictive edge case
    if avg <= 25:
        print("lower than or equal")
    # catch all other cases
    else:
        print("larger")
