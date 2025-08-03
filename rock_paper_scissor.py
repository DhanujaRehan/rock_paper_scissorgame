import random


emojies = {'r':"✊", 'p':"✋", 's':"✌️"}
choices = ('r', 'p', 's')
while True:

    user_choice = input('Rock, Paper , Scissor? (r,p,s) :' ).lower()
    if user_choice not in choices:
        print('Invalid choice. Please choose r, p, or s.')
        
    computer_choice = random.choice(choices)
    
    print(f"🫵 You chose: {emojies[user_choice]}, 💻 Computer chose: {emojies[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win! 🎉")
        
    else:
        print("You lose! 😢")
        
    should_continue = input('Continue? Press y or n: ').lower()
    if should_continue == 'n':
        break