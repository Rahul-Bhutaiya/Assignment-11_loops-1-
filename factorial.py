#Write a python script to calculate factorial of a given number

fact=int(input("Enter a Number : "))
if fact==0:
    print('Factorial :',1)
else:
    for x in range(fact,1,-1):
        fact=fact*(x-1)
    print('Factorial :',fact)
