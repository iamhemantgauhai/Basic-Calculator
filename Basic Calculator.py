n1,op,n2=int(input("No.1: ")),input("Arithmatical Operators: "),int(input("No.2: "))
if op=="+": print(n1,"+",n2,"=",n1+n2) 
elif op=="-": print(n1,"-",n2,"=",n1-n2)
elif op=="*": print(n1,"*",n2,"=",n1*n2)
elif op=="/": print(n1,"/",n2,"=",n1/n2)
elif op=="%": print(n1,"%",n2,"=",n1%n2)
elif op=="**": print(n1,"**",n2,"=",n1**n2)
else: print("Not Accepted")