# making multiplicative cipher encryption and decryption using python

import sys

domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

# making multiplicative inverse
def multiplicativeInverse(key, domain):

    r2 = key
    r1 = domain
    Q = ''
    flag = 0

    for i in range(r1):       
        q = int(r1/r2) 
        Q = Q + str(q)
        r = r1%r2 

        temp1 = r2
        r1 = temp1 #r2-------->r1
        temp2 = r 
        r2 = temp2 #r-------->r2
    
        flag += 1

        if r2 ==0:
            break

    if r1 == 1: 
        t1 = 0
        t2 = 1
        q = int(str(Q)[::-1])   #reverse the value of q by string slicing reverse method

        for i in range(flag):
            fakeQ = q
            q = fakeQ % 10
            t = t1 - (t2 * q) #the main equation
            q = int(fakeQ / 10)

            temp1 = t2
            t1 = temp1 #t2-------->t1
            temp2 = t
            t2 = temp2 #t-------->t2

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
                text = (string[(j*key)%domain])
                cipher = cipher + text
                
    print(f"The encrypted message is: {cipher}")
    print('\n')

# decryption method
def decryption(userInput, key, t1, domain, string):
    
    multiplicativeInverse(key, domain)

    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j*t1)%domain])
                cipher = cipher + text
                
    print(f"The encrypted message is: {cipher}")
    print('\n')

# choice the what you need to do (encrypt/decrypt)
while(True):
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            t1 = multiplicativeInverse(key, domain)
            decryption(userInput, key, t1, domain, string)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 