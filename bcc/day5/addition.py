# def msg():
#     val1 = int(input("Enter first number: "))
#     val2 = int(input("Enter second number: "))
#     # result = val1 + val2
#     # print("The sum of", val1, "and", val2, "is", result)

#     return val1 + val2
# res  = msg()
# print("The sum is", res)

# def msg():
#     val1 = int(input("Enter first number: "))
#     val2 = int(input("Enter second number: "))
#     return val1 + val2

# print("The sum is", msg())


def msg():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    sum = val1 + val2
    mul = val1 * val2
    sub = val1 - val2
    div = val1 / val2
    return sum, mul, sub, div
res = msg()
print("Results:", res)
