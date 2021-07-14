"""
error handling allows code execution even when
an error has been encountered

Types of errros
1. Syntax Error
2. Name error
3. Type Error
4. Index error for list
5. key error for dict
"""
while True:
    try:
        age = int(input('What is your Age?'))
        print(age)
    except ValueError as err:
        print(f'please enter a number {err}')
    else:
        print('Thank you')
        break
    finally:
        # finally runs regardless of anything
        print("Okay I am finally Done")
