def count_words(text):
    return len(text.split())

def character_counter(text):
    text = text.lower()
    words = text.split()
    dict = {}
    for word in words:
        for letter in word:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict

def sort_on(dict):
    return list(dict.values())[0]

def dict_sorter(dict):
    count_list = []
    for letter, count in dict.items():
        if letter.isalpha():
            letter_dict = {letter: count}
            count_list.append(letter_dict)
    count_list.sort(reverse=True, key=sort_on)
    return count_list