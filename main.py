# WAP to calculate x^y where x and y are positive integers greater than 1
# you should not use multiply(*) or power function. only add(+) is allowed
def multiply(a: int, b: int) -> int:
    # 2*3 = 2+2+2
    # a*b=a+a+a... b times
    res = 0
    for i in range(b):
        res += a
    return res


if __name__ == "__main__":
    print(multiply(2, 3))
