# WAP to calculate x^y where x and y are positive integers greater than 1
# you should not use multiply(*) or power function. only add(+) is allowed
def multiply(a: int, b: int) -> int:
    res = 0
    for i in range(b):
        print(f"res : {res}")
        res += a
    return res


print("Added a new line")


def power(a: int, b: int) -> int:
    #   a^b = a*a*a*a....b  times
    res = 1
    for i in range(b):
        res = multiply(res, a)

    return res


if __name__ == "__main__":
    print(power(2, 3))

    
'''
Dry Run:


power(2, 3)

     Power                Multiply
  a  b.    Res.            A.  B. res
  2. 3        1            1.   2.  0         
multiply(1, 2)                    0+a = 0+1 = 1
                                  1+a = 1+1 = 2

                res =2
multiply(2, 2)
                           2.  2.   0 
                                    0+a = 0+2 = 2
                                    2+a = 2+2 = 4
                Res = 4
multiply(4, 2)         
				4 2   0  
                                         res = 0 + a = 0 + 4
                                         res = 4 + a = 4 + 4 = 8
8
'''

