# ./CSC221/dev-project-1/Dev1.py
# Joseph Wilson CSC221 development assignment 1

from collections import namedtuple


def findQuotient(x, num) -> int:
    """Given two whole integer numbers greater than 0 function returns Quotient
    of x in regards to num
    """

    # test assertion of positive integer
    assert (x > 0) and isinstance(x, int)
    assert (num > 0) and isinstance(num, int)

    return x // num


def findRemainder(x, num) -> int:
    """Given two whole integer numbers greater than 0 function returns Remainder
    of x in regards to num
    """

    # test assertion of positive integer
    assert (x > 0) and isinstance(x, int)
    assert (num > 0) and isinstance(num, int)

    return x % num


def findFloatRemainder(x: int, num: int) -> float:
    """Returns float component of remainder
    e.g findFloatRemainder(5,2) will return 0.5 because
    (5/2) - (5//2) == 2.5 - 2 == 0.5
    """
    return (x / num) - findQuotient(x, num)


def convertM2H(minutes: int) -> int:
    """Converts given minutes to integer hours"""
    return findQuotient(minutes, 60)


if __name__ == "__main__":

    # making a namedtuple to make keeping track of each time object easier
    # than having variables t1_minutes,t2_minutes,t1_hours,t2_hours
    Time = namedtuple("Time", ["hours", "minutes"])

    # create new Time tuple from striped input from user, cast to integer
    t1 = Time(int(input().strip()), int(input().strip()))

    # create new Time tuple from striped input from user, cast to integer
    t2 = Time(int(input().strip()), int(input().strip()))

    # find the sum of each time component (minutes, hours)
    min_sum = t1.minutes + t2.minutes
    hour_sum = t1.hours + t2.hours

    # add quotient hours into hours
    hour_sum += convertM2H(min_sum)

    # find the number of minutes left over
    min_remains = findRemainder(min_sum, 60)
    min_remains_float = findFloatRemainder(min_sum, 60)

    # print the results to output
    print(f"{hour_sum} hours {min_remains} minutes")
    # using f-string float_value:.2f to limit the result to 2 decimal places
    print(f"{hour_sum + min_remains_float:.2f} hours")
