alf = "abcdefghijkmnlopqrstuvwxyzabcdefghijkmnlopqrstuvwxyzабвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя01234567890123456789"
while True:
    message = input("введіть речення: ")
    key = 2
    encrypt = message.lower()
    encrypted = ""
    for letter in encrypt:
        position = alf.find(letter)
        newposition = position + key
        if letter in alf:
            encrypted = encrypted + alf[newposition]
        else:
            position = alf(letter)
            encrypted = encrypted + alf[newposition]
    print(encrypted)