def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


text = "This  is  an  example!"
print(reverse_words(text))
