import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

# the list has indeces 0,1,2,3,4,5,6,7,8, there is not index '9'
# len(message) returns '9' but there is not index with number 9!
rnd1 = random.randint(0, len(messages) - 1)
print('Index number: ', rnd1)
rnd2 = messages[rnd1]
print(rnd2)
