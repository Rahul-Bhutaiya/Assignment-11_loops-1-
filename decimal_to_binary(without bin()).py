#Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)

number=int(input('Enter a Number : '))
bin=''
while number>0:
    bin=str(number%2)+bin
    number//=2
print('Binary :',bin)