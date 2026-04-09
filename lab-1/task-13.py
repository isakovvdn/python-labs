def extra_enumerate(x):
    total = sum(x)
    cum = 0

    for i, elem in enumerate(x):
        cum += elem
        frac = cum / total
        yield i, elem, cum, frac


x = [1, 3, 4, 2]

for i, elem, cum, frac in extra_enumerate(x):
    print(i, elem, cum, frac)