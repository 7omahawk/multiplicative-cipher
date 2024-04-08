# making multiplicative cipher encryption and decryption using python


domain = 26
string = "abcdefghijklmnopqrstuvwxyz"


userInput = input("Enter your text to encrypt: ")
key = int(input("Enter the key: "))
userInput = userInput.lower()

# def encryption(userInput, key, domain, string):
    
#     cipher = ""
#     for i in range(len(userInput)):
#         for j in range(len(string)):
#             if string[j] == userInput[i]:
#                 text = (string[(j*key)%domain])
#                 cipher = cipher + text
                
#     print(f"The encrypted message is: {cipher}")
#     print('\n')

# encryption(userInput, key, domain, string)


r2 = key
r1 = domain
Q = ''

for i in range(r1):       
    q = int(r1/r2) 
    Q = Q + str(q)
    r = r1%r2 

    temp1 = r2
    r1 = temp1 #r2-------->r1
    temp2 = r 
    r2 = temp2 #r2-------->r

    if r2 ==0:
        break

print(Q)
print(r1)
