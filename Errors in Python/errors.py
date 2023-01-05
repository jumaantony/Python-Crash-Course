"""
error handling allows code execution even when
an error has been encountered

Types of errros
1. Syntax Error
2. Name error
3. Type Error
4. Index error for list
5. key error for dict
6. Zero division error when a number is divided by zero.


The try statement works as follows.

First, the try clause (the statement(s) between the try and except keywords) is executed.

If no exception occurs, the except clause is skipped and execution of the try statement is finished.

If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.
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
