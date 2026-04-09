def non_empty(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [x for x in result if x is not None and x != ""]
    return wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None]


print(get_pages())