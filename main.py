# WAP to calculate x^y where x and y are positive integers greater than 1
# you should not use multiply(*) or power function. only add(+) is allowed
def multiply(a: int, b: int) -> int:

    for i in range(b):
        print(f"res : {res}")
        res += a
    return res


def power(a: int, b: int) -> int:
    #   apowerb = a*a*a*a....b  times
    res = 1
    for i in range(b):
        res = multiply(res, a)

    return res


if __name__ == "__main__":
    print(power(2, 3))
