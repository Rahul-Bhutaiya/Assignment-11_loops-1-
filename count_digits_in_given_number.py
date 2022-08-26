#Write a python script to count digits in a given number

count=0
digit=int(input('Enter a Number : '))

while digit>0:
    count+=1
    digit//=10
print('%d Digits in Entered Number.'%count)