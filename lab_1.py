def toplengh_function():
    text = input("введіть текст: ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    word_list = text.split(' ')
    longest_string = sorted(word_list, key=len)[-1]
    print("1: ",longest_string)
    second_longest_string = sorted(word_list, key=len)[-2]
    print("2: ",second_longest_string)
    third_longest_string = sorted(word_list, key=len)[-3]
    print("3: ",third_longest_string)
    fourth_longest_string = sorted(word_list, key=len)[-4]
    print("4: ",fourth_longest_string)
    fifth_longest_string = sorted(word_list , key=len)[-5]
    print("5: ",fifth_longest_string)

def dict_function():
    text = input("введіть текст: ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    words = text.split(' ')
    def unique_list(l):
        ulist = []
        [ulist.append(x) for x in l if x not in ulist]
        return ulist
    
    text=' '.join(unique_list(words))

    dictOfWords = { i : sorted(words)[i] for i in range(0, len(words) ) }
    print(dictOfWords)
    

def count_fuction():
    text = input("введіть текст: ")
    text = text.replace(".", " ")
    text = text.replace(",", " ")

    allWords = text.split();
    allWordsSingle = {};

    for word in allWords:
        allWordsSingle.update({word: allWords.count(word)})

    keysSorted = []
    for key in allWordsSingle:
        keysSorted.append(key)
    keysSorted.sort()

    for key in keysSorted:
        print(f"{key} - {allWordsSingle[key]}")

choose = int(input("виберіть дію(1/2/3): "))
if choose == 1 :
    toplengh_function()
elif choose == 2 :
    dict_function()
elif choose == 3 :
    count_fuction()
else:
    print("Ви вибрали не правильне значення для дії")