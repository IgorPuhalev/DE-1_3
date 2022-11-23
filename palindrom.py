x = input ("Введите строку без пробелов ")
x_2 = ''.join(reversed (x))
if x==x_2:
    print (True)
else: print (False)
