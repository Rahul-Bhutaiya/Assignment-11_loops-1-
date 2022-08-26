#Write a python script to calculate sum of first N even natural numbers

#METHOD:1
"""
sum=0
n=int(input("Enter N Value : "))
i=1
while i<=n:
    sum+=i*2
    i+=1
print('Sum',sum)
"""
#METHOD:2
sum=0
for x in range(int(input('Enter N Value : '))):
    sum+=(x+1)*2
print('Sum :',sum)