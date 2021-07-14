class PlayerCharacter:
    # class obj attribute
    membership = True

    # contsructor method
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')


player1 = PlayerCharacter('wicked')
player2 = PlayerCharacter('tony')

print(player1.name)
print(player2.membership)
