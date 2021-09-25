import random as r
def num_gen(l):
   x=''
   nums= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   for i in range(0,l):
       x=x+str(r.choice(nums))
   x=int(x)
   return x
#------------------------------------------------------------------------------
player_name = input("Hello, What's your name?")
user_len=int(input("enetr the required length of the number to be guess   :"))
number = num_gen(user_len)
number_of_guesses = int(input("hi %s how many number of attemps u wnat? \n >>>>>>>>>>>" %(player_name)))
x=number_of_guesses
#------------------------------------------------------------------------------
def hint_gener(number):
    my_hints=[]
    my_h=[]
    if(number%2==0):
        my_hints.append("number is divisible by 2")
    else:
        my_hints.append("number is odd")
    my_hints.append("it is %d digit number" %len(str(number)))
    for i in str(number):
        my_h.append(("one of the digit is %s" %(i)))
    my_net=my_hints+my_h
    return my_net
#------------------------------------------------------------------------------
hints_list= hint_gener(number)
while number_of_guesses >0:
    guess = int(input("start guessing a number:"))
    number_of_guesses -= 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
    x=input(" need hint  ?\n enter y or n \n Or enter STOP to termnate the game  : \n >>")
    if(x=="STOP"):
        break
    if (x=="y"):
        print(r.choice(hints_list))
#------------------------------------------------------------------------------
if(x=="STOP"):
    print('You did not guess the number, The number was ' + str(number))

elif guess == number:
    print('You guessed the number in ' + str(x-number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
