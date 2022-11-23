x = (input ("ВВедите строку из скобок:  "))
a1 = ("{")
a2 = ("}")
a3 = ("[")
a4 = ("]")
a5 = ("(")
a6 = (")")
a1_1=0
a2_1=0
a3_1=0
a4_1=0
a5_1=0
a6_1=0
for i in x:
    if i==a1:
        a1_1=a1_1+1
    elif i==a2:
        a2_1=a2_1+1
    elif i==a3:
        a3_1=a3_1+1
    elif i==a4:
        a4_1=a4_1+1
    elif i==a5:
        a5_1=a5_1+1
    elif i==a6:
        a6_1=a6_1+1  
print (a1_1, a2_1, a3_1, a4_1, a5_1, a6_1)         
if a1_1==a2_1:
    if a3_1==a4_1:
        if a5_1==a6_1:
            print ("True")
else: print ("False")
