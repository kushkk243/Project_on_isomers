# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:42:14 2019

@author: Kush kumar
"""
print("                      WELCOME TO ISOMER BUILDER                       ")
a = input("Enter compound : ")
C=0
N=0
H=0
O=0
X=0
for i in range (0,len(a)):
    if a[i] =="C" or a[i]=="c":
        if a[i+1].isdigit() or a[i+1]=="H" or a[i+1] == "h":
            if a[i+1].isdigit():
                C = int(a[i+1])
            elif a[i+1]=="H" or a[i+1]=="h":
                C = 1
            elif a[i+1].isdigit() and a[i+2].isdigit():
                C = int(a[i+1]+a[i+2])
    if a[i] == "H" or a[i] == "h":
        if a[i+1].isdigit():
            H=int(a[i+1])
        elif a[i+1].isalpha():
            H=1
        elif a[i+1].isdigit() and a[i+2].isdigit():
            H = int(a[i+1]+a[i+2])
    if a[i] == "N" or a[i] == "n":
        if a[i+1].isdigit():
            N = int(a[i+1])
        else:
            N = 1
    if a[i] in ["C","B"] or a[i] in ["c","b"]:
        if a[i+1] in ["l","r"]:
            if a[i+2].isdigit():
                X = int(a[i+2])
            else:
                X = 1
    if a[i] in ["F","I"] or a[i] in ["f","i"]:
        if a[i+1].isdigit():
            X = int(a[i+1])
        else:
            X = 1
DBE = C + 1 +((N- (H + X))/2)
if DBE == 0:
    print("No unsaturated isomers are possible for : " , a)
elif DBE == 1:
    poss = { 1:{1:" double bond"} , 2:{1:"ring"}}
    print("The isomer may contain : ",poss , sep = "\n")
elif DBE == 2:
    poss = {1:{1:" triple bond"}, 2:{2:"double bond"} , 3:{1:"ring",2:{1:"double bond"}}}
    print("The isomer may contain : ",poss , sep = "\n")
elif DBE == 3:
    poss = {1:{1:"triple bond",2:{1:"double bond"}},2:{1:"triple bond",2:{1:"ring"}},3:"double bond",4:{3:"ring"},5:{"ring":1,"double bond":2},6:{"ring":2,"double bond":1}}
    print("The isomer may contain : ",poss , sep = "\n")

