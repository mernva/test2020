def break_words(stuff):
    words=stuff.split(' ')  #分隔
    return words

def sort_words(words):
    return sorted(words)   #排序

def print_first_word(words):
    word=words.pop(0)
    return word
def print_last_word(words):
    word =words.pop(-1)
    print(word)
def sort_sentence(sentence):
    words=break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    words =break_words(sentence)
    print(print_first_word(words))
    print(print_last_word(words))
def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print(print_first_word(words))
    print(print_last_word(words))


sentence="All will goes well to you"
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
a=break_words(sentence)
print(a)
print(sort_words(a))
print(print_first_word(a))
print(print_last_word(a))
