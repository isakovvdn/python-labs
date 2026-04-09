text = input()
words = text.split()

long_words = []
mid_words = []
short_words = []

for word in words:
    if len(word) > 7:
        long_words.append(word)
    elif 4 <= len(word) <= 7:
        mid_words.append(word)
    else:
        short_words.append(word)

for word in long_words:
    print(word)

for word in mid_words:
    print(word)

for word in short_words:
    print(word)