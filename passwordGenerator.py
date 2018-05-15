"""
This application creates strong, random passwords to the length specified by the user(s).
"""
# Dependencies
import random as rnd
import pandas as pd
import numpy as np

# Creating lists to store user input future enhancements.
YES_D = ["YES","YE","Y","1"]
NO_D=["NO","N","0"]

# Establishes password character lists
ALPHA_UP = ["A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X",
            "Y", "Z"]
ALPHA_LW = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]
NUMERIC = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "_", "=", "<", ">", "%"]
PW_FOUR=[0,0,0,0]
NO_PASSWORDS = []

PW_W = "password.txt"
try:
    PASSWORD_LEN = int(input("Enter a value for the length of your password: "))
except ValueError:
    print("VALUE MUST BE AN INTEGER GREATER THAN 0")
    PASSWORD_LEN = int(input("Enter a value for the length of your password: "))
PW_W = "password.txt"
try:
    TOTAL_PASSWORDS = int(input("Number of passwords to generate: "))
except ValueError:
    print("VALUE MUST BE AN INTEGER GREATER THAN 0")
    TOTAL_PASSWORDS = int(input("Number of passwords to generate: "))    

RAND_PW = PASSWORD_LEN - 4
PW_TAIL = [[0] * PASSWORD_LEN for i in range(RAND_PW)]

for item in range(TOTAL_PASSWORDS):
    # Establishing the first 4 charcters of a password
    for i in range(0,3):
        char = rnd.randint(1, 3)
        if char == 1:
            PH = rnd.choice(ALPHA_UP)
        elif char == 2:
            PH = rnd.choice(ALPHA_LW)
        else:
            PH = rnd.choice(NUMERIC)
        PW_FOUR[i] = str(PH)

    PW_HEAD=str(PW_FOUR[0])+str(PW_FOUR[1])+str(PW_FOUR[2])+str(PW_FOUR[3])

    for i in range(RAND_PW):
        char = rnd.randint(1, 4)
        if char == 1:
            pw = rnd.choice(ALPHA_UP)
        elif char == 2:
            pw = rnd.choice(ALPHA_LW)
        elif char == 3:
            pw = rnd.choice(NUMERIC)
        else:
            pw = rnd.choice(SPECIAL)
        PW_TAIL[i] = pw

    BUFFER = "_" * PASSWORD_LEN
    PSWD_GEN = PW_HEAD+"".join(PW_TAIL)
    #print(BUFFER + "\n")
    #print(PSWD_GEN)
    NO_PASSWORDS.append(PSWD_GEN)
    
    PASS_OUT = pd.DataFrame(np.column_stack([NO_PASSWORDS]),columns=[{"ID","Passwords"}])

#Creating a loop that will ask the user to save the password, if they decline
# the application will not save the password and close.
CHK = 0
while CHK == 0:
    USER_RESPONSE=input("Would you like to save your password to file? ").upper() or "YES"
    if USER_RESPONSE in YES_D:
        try:
            print("Please enter a filename or leave blank for the default filename.")
            FILE_NAME= str(input()) or "password.txt"
            FILE_NAME=str(FILE_NAME).replace(".txt","")+".txt"
        except ValueError:
            FILE_NAME="password.txt"
            CHK = CHK + 1
        F = open(FILE_NAME, "w+")
        F.write(PSWD_GEN)
        F.close()
        if len(NO_PASSWORDS) > 1:
            PASS_OUT.to_csv(str(FILE_NAME).replace(".txt","")+".csv", index_label="ID",encoding="Latin-1")
        CHK = CHK + 1
    elif USER_RESPONSE in NO_D:
        CHK = CHK + 1
        exit()
    else:
        print("That was not a valid entry, please enter [y/n]")
        
print(PSWD_GEN)