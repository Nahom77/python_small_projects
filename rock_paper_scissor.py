import random

choices = [{'label': 'r','emoji': '🥌', 'wins': ['s']}, 
           {'label': 's','emoji': '✂', 'wins': ['p']}, 
           {'label': 'p','emoji': '📄', 'wins': ['r']}]

labels = [choice['label'] for choice in choices]

while True:
    user_choice = input ('Rock, Paper or Scissors? (r/p/s):').lower()
    if user_choice not in labels:
        print('Invalid choice!')
        continue

    computer_choice = random.choice(labels)

    user = next(choice for choice in choices if choice['label'] == user_choice)
    computer = next(choice for choice in choices if choice['label'] == computer_choice)

    print(f'You chose {user['emoji']}')
    print(f'Computer chose {computer['emoji']}')

    if(user_choice == computer_choice):
        print('Draw')
    elif(computer_choice in user['wins']):
        print('You won')
    else:
        print('You lose')
    

    should_continue = input('Do you want to continue? (y/n)').lower()
    if(should_continue == 'n'):
        break

    
