text = input()
parts = text.split(' ')
result = []

for part in parts:
    subparts = part.split(',')
    new_subparts = []

    for word in subparts:
        if word != "" and word[0].isupper():
            new_subparts.append(word.upper())
        else:
            new_subparts.append(word)

    result.append(','.join(new_subparts))

print(' '.join(result))