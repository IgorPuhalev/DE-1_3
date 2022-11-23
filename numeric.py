x = int(input ("Введите число от 1 до 2000 "))
a = int(x/1000)
#print (a)

if a==1:
    rim1000= ("M")
else: 
    if a==2:
        rim1000=("MM")
    else:
        rim1000=("")
ar100 = int((x-(a*1000))/100)
if ar100==1:
    rim100=("C")
elif ar100==2:
    rim100=("CC")
elif ar100==3:
    rim100=("CCC")  
elif ar100==4:
    rim100=("CD")    
elif ar100==5:
    rim100=("D")    
elif ar100==6:
    rim100=("DC")      
elif ar100==7:
    rim100=("DCC")
elif ar100==8:
    rim100=("DCCC")    
elif ar100==9:
    rim100=("CM")  
elif ar100==0:
    rim100=("")
ar10 = int((x-(a*1000)-(ar100*100))/10)
#print (ar10)
if ar10==1:
    rim10=("X")
elif ar10==2:
    rim10=("XX")
elif ar10==3:
    rim10=("XXX")  
elif ar10==4:
    rim10=("XL")    
elif ar10==5:
    rim10=("L")    
elif ar10==6:
    rim10=("LX")      
elif ar10==7:
    rim10=("LXX")
elif ar10==8:
    rim10=("LXXX")    
elif ar10==9:
    rim10=("XC")    
elif ar10==0:
    rim10 = ("")    
ar =(x-(a*1000)-(ar100*100)-(ar10*10))
if ar==1:
    rim=("I")
elif ar==2:
    rim=("II")
elif ar==3:
    rim=("III")  
elif ar==4:
    rim=("IV")    
elif ar==5:
    rim=("V")    
elif ar==6:
    rim=("VI")      
elif ar==7:
    rim=("VII")
elif ar==8:
    rim=("VIII")    
elif ar==9:
    rim=("IX")    
elif ar==0:
    rim = ("")       
print (rim1000+rim100+rim10+rim)
