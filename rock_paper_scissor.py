choices = ['r', 'p', 's']
user_choice = input('Rock, Paper , Scissor? (r,p,s) :' ).lower()

if user_choice not in choices:
    print('Invalid choice. Please choose r, p, or s.')
    