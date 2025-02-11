p = print
p("Do You Have A Problem ?")
n = input("Enter Yes Or No ➟ ")
if n=="Yes" or n=="YES" or n=="yes":
    p("Can You Solve It ?")
    m = input("Enter Yes Or No ➟ ")
    if m=="Yes" or m=="YES" or m=="yes":
        p("Then Why Worry ?")
    elif m=="No" or m=="NO" or m=="no":
        p("Then Why Worry ?")
    else :
        p("Invalid Value")
elif n=="No" or n=="NO" or n=="no" :
    p("Then Why Worry ?")
else :
    p("Invalid Value")        