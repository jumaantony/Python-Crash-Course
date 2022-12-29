print('CHECKING PASSWORD LENGTH')

userName = input('What is your name?')
password = input('Input your password')

password_length = len(password)
hidden_password = '*' * password_length

print(f'hello? {userName}, your password, {hidden_password}, is {password_length} letters long')