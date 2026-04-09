class StringFormatter:
    def __init__(self, text):
        self.text = text

    def remove_short_words(self, n):
        words = self.text.split()
        self.text = " ".join([w for w in words if len(w) >= n])

    def replace_digits(self):
        self.text = "".join(['*' if c.isdigit() else c for c in self.text])

    def add_spaces(self):
        self.text = " ".join(list(self.text))

    def sort_by_length(self):
        words = self.text.split()
        self.text = " ".join(sorted(words, key=len))

    def sort_lex(self):
        words = self.text.split()
        self.text = " ".join(sorted(words))


s = StringFormatter("your password abcdef12345 is not safe")

s.remove_short_words(5)
s.replace_digits()
s.sort_lex()

print(s.text)