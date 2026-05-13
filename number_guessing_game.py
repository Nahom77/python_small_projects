import random

random_num = random.randint(1,10)

while True:
    try:
        choice = int(input('Guess the number between 1 and 10: '))

        if(choice > random_num) :
            print('Too high')
        elif (choice < random_num):
            print('Too low')
        else: 
            print('Congratulations! You guessed the number')
            break
            
    except ValueError:
        print('Please enter a valid number')



# while random_num !=  choice :
    