#Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

number=int(input('Enter a Number : '))
oct=''
while number>0:
    oct=str(number%8)+oct
    number//=8
print('Octal :',oct)