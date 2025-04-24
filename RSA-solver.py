import math

inOrOut = input("Would you like to encrypt or decrypt a message? Type E to encrypt and D to decrypt ")

def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return a * b // gcd(a, b)

def messageToInt(message):
    p = 0
    messageLength = len(message)
    for i in range(messageLength):
        p = p + ord(message[i])*10**(3*i)
    return p

def intToMessage(messageInt):
    message = ""
    while messageInt > 0:
        message = chr(messageInt%1000) + message
        messageInt = messageInt//1000
    return message

def encrypt(message, publicKey, eValue):
    messageInt = messageToInt(message)
    encryptedValue = ((messageInt**int(eValue)) % int(publicKey))
    return encryptedValue

def decrypt(message, privateKey1, privateKey2, eValue):
    j=0
    lambdaN = (int(privateKey1)-1) * (int(privateKey2)-1)
    while True:
        if (j * int(eValue)) % lambdaN == 1:
            d=j
            break
        j += 1
        if j % 1000 == 0:
            print(j/1000)
    decryptedValue = (int(message) ** d) % (int(privateKey1) * int(privateKey2))
    decryptedMessage = intToMessage(decryptedValue)
    print(lambdaN)
    return decryptedMessage

    

if inOrOut == "E":
    messageOut = input("Please enter your message: ")
    publicKey = input("Please enter the public key of the recipient: ")
    eValue = input("Please enter the value of e: ")
    print("Your encrypted message is: " + str(encrypt(messageOut, publicKey, eValue)))

if inOrOut == "D":
    messageIn = input("Please enter your message: ")
    privateKey1 = input("Please enter the your first prime numbers: ")
    privateKey2 = input("Please enter the your second prime numbers: ")
    eValue = input("Please enter the number you chose for e: ")
    print("Your decrypted message is: " + decrypt(messageIn, privateKey1, privateKey2, eValue))
