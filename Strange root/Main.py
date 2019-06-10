import math
digit = input("Enter number: ")
sqrt = str(math.sqrt(int(digit)))
sq = str(pow(int(digit), 2))
try:
    tsqrt = sqrt.split(".")[1][:3]
    if sq in tsqrt:
        print(True)
    else:
        print(False)
except:
    print(False)




