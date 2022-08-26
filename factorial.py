#Write a python script to calculate factorial of a given number

fact=int(input("Enter a Number : "))
for x in range(fact,1,-1):
    fact=fact*(x-1)
print('Factorial :',fact)