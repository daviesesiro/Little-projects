def main():
    information = input("Enter data to encrypt\t")
    information = encrypt(information, 1)
    print(information)


def encrypt(data, incr):
    A = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrytion = ''
    for i in range(len(data)):
        letter = data[i]
        pos = (A.find(letter), A.find(letter) + incr)[letter != " "]
        encrytion += A[pos]
    return encrytion


def decrypt(data, dcr):
    A = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrytion = ''
    for i in range(len(data)):
        letter = data[i]
        pos = (A.find(letter), A.find(letter) + dcr)[letter != " "]
        decrytion += A[pos]
    print(decrytion)


main()
