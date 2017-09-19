def uinput():
    count = input("Input an integer (0 terminates):")
    count = int(count)
    return count


def lab02():
    count = uinput()
    ctotal = 0
    codd = 0
    ceven = 0
    evensum = 0
    oddsum = 0
    while count != 0:
        if count > 0:
            ctotal += 1
            if count % 2 == 0:
                ceven += 1
                evensum += count
            else:
                codd += 1
                oddsum += count
        else:
            print("Negative int entered")
        count = uinput()
    print("Sum of odds: ", oddsum)
    print("Sum of evens: ", evensum)
    print("Odd Count: ", codd)
    print("Even count:", ceven)
    print("Total Positive Int Count:", ctotal)


lab02()
