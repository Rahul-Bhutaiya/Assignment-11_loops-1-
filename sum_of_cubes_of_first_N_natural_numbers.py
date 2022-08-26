#Write a python script to calculate sum of cubes of first N natural numbers

sum=0
for x in range(int(input('Enter N Value : '))):
    sum+=(x+1)**3
print('Sum :',sum)