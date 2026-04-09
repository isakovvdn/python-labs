def pre_process(a=0.97):
    def decorator(func):
        def wrapper(s):
            new_s = s[:]
            for i in range(1, len(new_s)):
                new_s[i] = new_s[i] - a * new_s[i - 1]
            return func(new_s)
        return wrapper
    return decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


plot_signal([1, 2, 3, 4, 5])