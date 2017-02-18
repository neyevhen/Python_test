# 1 _______________________
def text_parc(text):
    result = ""
    text = "".join(sorted(text))
    last_letter = ""
    for letter in text:
        if letter == last_letter:
            result += letter
        last_letter = letter
    return result

print text_parc("agcdcgia")


"""def text_parc_lists(text):
    result = ["", ""]  # 0 - last_letter; 1 - result;
    for letter in text:
        result.append(letter)
    result.sort()
    for letter in range(2, len(result)):
        if result[letter] == result[0]:
            result[1] += result[letter]
        result[0] = result[letter]
    return result[1]

print text_parc_lists("agcdcgia")"""

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
extend_letters = "!\"$%&\'*+,-./:;<=>?[\\]^`{|}~ \t\n\x0b\x0c\r"


def normalize(text):
    result = ""
    for letter in text:
        for symbol in extend_letters:
            if letter == symbol:
                break
        if letter != symbol:
            result += letter
    return result


print normalize("X > %Y")
print normalize("  X >      Y    >")
print normalize("\"X\" >'Y'> I  \t> 1Z2")


# 4 _______________________
# miss

# 5 _______________________

def select_keys(dic, keys):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = dic[keys[i]]
    return result

print select_keys({'a': 1, 'b': 2}, ['b'])
print select_keys({'a': 1, 'b': 2, 'c': 3, 'i': 4}, ['a', 'c'])


# 6 _______________________


def toArray(dic):
    lists = []
    for key in dic:
        lists.append([key, dic[key]])
    return lists

print toArray({"0": "a", "1": "b", "2": "c"})




