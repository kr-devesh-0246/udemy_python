x = int(input("Enter a year"))

if x % 100 == 0:
    if x % 400 == 0:
        print(f"{x} is a Leap year")
    else:
        print(f"{x} is a Non-Leap year")

else:
    if x % 4 == 0:
        print(f"{x} is a Leap year")
    else:
        print(f"{x} is a Non-Leap year")

