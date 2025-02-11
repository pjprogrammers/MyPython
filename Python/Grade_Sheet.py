p=print
n=int(input('Enter Number Of Students : ' ))
for i in range (1,n+1):
	s_name = input("Enter Name Of Student %d : " %i)
	m= float(input("Enter Marks Of Student %d: " %i ))
	if m<=100 and m>=80:
		p("Grade A")
	elif m<80 and m>=70 :
		p("Grade B")
	elif m<70 and m>=50 :
		p("Grade C")
	elif m<50 and m>=35 :
		p("Grade D")
	elif m<35 :
		p("Reappear")
	else :
		p("Invalid Value Error")
