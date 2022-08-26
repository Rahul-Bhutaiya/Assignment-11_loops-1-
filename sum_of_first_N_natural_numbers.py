#Write a python script to calculate sum of first N natural numbers

sum=0
for x in range(int(input('Enter N Value : '))):
    sum+=(x+1)
print('Sum :',sum)