# 1 _______________________
def text_parc(text):
    result = ""
    count = 0
    for letter in text:
        for i in text:
            if letter == i:
                count += 1
        if count >= 2 and result.find(letter) == -1:
            result += letter
        count = 0
    return result


print text_parc("agcdcgia")


# 2 _______________________
array = [
    {'id': 1, 'state': True},
    {'id': 2, 'state': True},
    {'id': 8, 'state': False}
]


def update(key, status):
    for lists in array:
        if lists['id'] == key:
            lists['state'] = status


# update(2, False)
update(8, True)
# update(7, True)
print array


# 3 _______________________
extend_letters = "!\"$%&\'*+,-./:;<=?[\\]^`{|}~\t\n\x0b\x0c\r"


def normalize(text):
    result = ""
    for letter in text:
        for symbol in extend_letters:
            if letter == symbol:
                break
        if letter != symbol:
            result += letter
    # deletes more then one space
    result = " ".join(result.split())
    return result.strip()


print normalize("X > %Y")
print normalize("  X >      Y    >")
print normalize("\"X\" >'Y'> I  \t> 1Z2")


# 4 _______________________
def toHash(lsts):
    dic = {}
    for lst in lsts:
        dic[(lst[0])] = lst[1]
    return dic


print toHash([["x", "y"], ["a", "b"], ["i", "j"]])


# 5 _______________________
def select_keys(dic, keys):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = dic[keys[i]]
    return result


print select_keys({'a': 1, 'b': 2}, ['b'])
# print select_keys({'a': 1, 'b': 2, 'c': 3, 'i': 4}, ['a', 'c'])


# 6 _______________________
def toArray(dic):
    lists = []
    for key in dic:
        lists.append([key, dic[key]])
    return lists


print toArray({"0": "a", "1": "b", "2": "c"})




