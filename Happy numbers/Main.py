"""HAPPY NUMBERS  if the repeated sum of squares of the digits of a number is equal to 1, it is considered to be happy
for Example: 23 is a happy number, as: 2^2 + 3^2  = 13  1^2 + 3^2  = 10 1^2 + 0^2  = 1
sequence of happy numbers: 1,7,10,13,19,23
"""


def main():
    number: str = input("Enter number you want to test:  ")
    output = easy(number)
    print(output + " number")
    medium()
    number: str = input("Enter number you want to test and see each sum of square of each digit of the number:  ")
    hard(number)


def easy(number):
    sumSq = 0
    x = 0
    while sumSq != 1 and (x != 4 or x != 5):
        sumSq = 0
        for j in number:
            d = int(j) ** 2
            sumSq += d
        number = str(sumSq)
        x += 1
    output = ('Sad', 'Happy')[number == "1"]
    return output


def medium():
    allNum = ''
    amt = int(input("Enter range:  "))
    for i in range(amt + 1):
        sumSq = 0
        number: str = str(i)
        x = 0
        while sumSq != 1 and (x != 5 or x != 5):
            sumSq = 0
            for j in number:
                d = int(j) ** 2
                sumSq += d
            number = str(sumSq)
            x += 1
        output = ('Sad', 'Happy')[number == "1"]
        if output == 'Happy':
            allNum += str(i) + " "
    print("From 1 to " + str(amt) + ", these are the happy numbers " + allNum)


def hard(number):
    output = easy(number)
    print(output + " number")
    sumSq = 0
    x = 0

    while sumSq != 1 and x != 5:
        sumSq = 0

        for j in number:
            d = int(j) ** 2
            sumSq += d
        if output == 'Happy':
            print(str(x + 1) + ". " + number + " square sum is " + str(sumSq))

        number = str(sumSq)
        x += 1


if __name__ == '__main__':
    main()
