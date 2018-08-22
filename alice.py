# pokud je vek pod 12 let pak se splni prvni ELIF a program ignoruje ostatni ELIF
# pokud je vek vyssi jak 12 ale mensi jak 110 pak je splneno ELSE
# pokud je vek nad 3000 je splneno ELSE
# pokud je vek nad 110 ale pod 3000 je splneno druhe ELIF


name = input('Enter you name.\n')
age = int(input('Enter your age.\n'))

if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif 110 < age < 3000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
else:
    print('Your are of normal age.')
