import math

inOrOut = input("Would you like to encrypt or decrypt a message? Type E to encrypt and D to decrypt")

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

def encrypt(message, publicKey, eValue):
    messageInt = messageToInt(message)


def decrypt(message, privateKey1, eValue):
    messageInt = messageToInt(message)    
    

if inOrOut == "E":
    messageOut = input("Please enter your message: ")
    publicKey = input("Please enter the public key of the recipient: ")
    eValue = input("Please enter the value of e: ")
    print("Your encrypted message is: ")
    print(messageToInt(messageOut))

if inOrOut == "D":
    messageIn = input("Please enter your message: ")
    privateKey1 = input("Please enter the your first prime numbers: ")
    privateKey2 = input("Please enter the your second prime numbers: ")
    eValue = input("Please enter a number you like between 1 and " + str(lcm(int(privateKey1)-1, int(privateKey2)-1) + ": ")
    print("Your decrypted message is: ")