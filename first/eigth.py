is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are a master magician')

if is_magician and not is_expert:
    print('at least you getting there')

not_magician = not is_magician

if not_magician:
    # is_magician == False:
    print("you need magic powers")