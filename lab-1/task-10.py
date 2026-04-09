password = input()
score = 0

if len(password) >= 8:
    score += 1
if any(ch.islower() for ch in password):
    score += 1
if any(ch.isupper() for ch in password):
    score += 1
if any(ch.isdigit() for ch in password):
    score += 1
if any(not ch.isalnum() for ch in password):
    score += 1

if score <= 2:
    print("Слабый пароль")
elif score <= 4:
    print("Средний пароль")
else:
    print("Надежный пароль")