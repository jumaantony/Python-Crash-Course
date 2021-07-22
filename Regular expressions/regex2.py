import re
# email validation using regex

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = input("Input your email address:  ")

a = pattern.search(string)

print(a)

# password validation using regex

password = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")

user_input = input("Input your password: ")
regex_pass = password.match(user_input)

print(regex_pass)