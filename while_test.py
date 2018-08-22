# while kontroluje podminku tak dlouho dokud je TRUE, dokud je spam mensi nez 11
# jakmile spam = 11, while se stane FALSE a smycka skonci

spam = 1
while spam < 11:
    print('Hello world! ' + str(spam))
    spam += 1
