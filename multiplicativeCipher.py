# making multiplicative cipher encryption and decryption using python

import sys
import os

domain = 26
string = "abcdefghijklmnopqrstuvwxyz"


design = """
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+               _ _   _       _ _           _   _               ___ _       _                +
+   /\/\  _   _| | |_(_)_ __ | (_) ___ __ _| |_(_)_   _____    / __(_)_ __ | |__   ___ _ __  +
+  /    \| | | | | __| | '_ \| | |/ __/ _` | __| \ \ / / _ \  / /  | | '_ \| '_ \ / _ \ '__| +
+ / /\/\ \ |_| | | |_| | |_) | | | (_| (_| | |_| |\ V /  __/ / /___| | |_) | | | |  __/ |    +
+ \/    \/\__,_|_|\__|_| .__/|_|_|\___\__,_|\__|_| \_/ \___| \____/|_| .__/|_| |_|\___|_|    +
+                      |_|                                           |_|                     +
+                                                                            -By 7omahawk    +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


# making multiplicative inverse
def multiplicativeInverse(key, domain):

    r2 = key
    r1 = domain
    Q = ""
    flag = 0

    for i in range(r1):
        q = int(r1 / r2)
        Q = Q + str(q)
        r = r1 % r2

        temp1 = r2
        r1 = temp1  # r2-------->r1
        temp2 = r
        r2 = temp2  # r-------->r2

        flag += 1

        if r2 == 0:
            break

    if r1 == 1:
        t1 = 0
        t2 = 1
        q = int(str(Q)[::-1])  # reverse the value of q by string slicing reverse method

        for i in range(flag):
            fakeQ = q
            q = fakeQ % 10
            t = t1 - (t2 * q)  # the main equation
            q = int(fakeQ / 10)

            temp1 = t2
            t1 = temp1  # t2-------->t1
            temp2 = t
            t2 = temp2  # t-------->t2

        if t1 < 0:
            t1 = t1 + domain
    else:
        print("For this key there will be no multiplicative inverse.")

    return t1


# encryption method
def encryption(userInput, key, domain, string):

    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = string[(j * key) % domain]
                cipher = cipher + text

    print(f"The encrypted message is: {cipher}")
    print("\n")


# decryption method
def decryption(userInput, key, t1, domain, string):

    multiplicativeInverse(key, domain)

    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = string[(j * t1) % domain]
                cipher = cipher + text

    print(f"The encrypted message is: {cipher}")
    print("\n")


# choice the what you need to do (encrypt/decrypt)
while True:
    print(design)
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt (A-Z): ")
            key = int(input("Enter the key (Prime number, ex: 5): "))
            userInput = userInput.lower()
            encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt (A-Z): ")
            key = int(input("Enter the key (Prime number, ex: 5): "))
            userInput = userInput.lower()
            t1 = multiplicativeInverse(key, domain)
            # print(type(t1))  # return type else er vitore upore thakle nonetype ashe
            # if int(t1 or 0) % 2 == 0:
            #     print("For this key there will be no multiplicative inverse.")
            # else:
            decryption(userInput, key, t1, domain, string)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number)

    input()             # press enter to clear screen
    os.system('clear')  # clear screen
