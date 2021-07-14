is_old = True
is_licenced = True
#this is a tenary opereator
can_drive = "you are old enough to drive" if is_old else "wait till you get of age"

can_drive2 = "you can now drive since you have a driving licence" if is_licenced else "go get a driving licence"

print(can_drive)

print(can_drive2)

# if is_old and is_licenced:
   # print('your old enough to drive and you have a licence')
#elif:
   # print('wait till you become of age and have a licence too')
    # if is_licenced:
        # print("you can drive now")
# else:
    # print('checkcheck')