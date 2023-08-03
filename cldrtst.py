def dy(a):
    if a==1:
        print("sunday")
    elif a==2:
        print('monday')
    elif a==3:
        print('tuesday')
    elif a==4:
        print("wednesday")
    elif a==5:
        print("thursday")
    elif a==6:
        print("friday")
    elif a==7:
        print("saturday")
d=int(input())
da=int(input())
def calender(x,b):
 print('Date','    Day')
 for i in range(1,b+1):
     print('   ',i,'  ',end='')
     dy(x)
     if x==7:
         x=1
     else:
         x=x+1
calender(d,da)    
    
