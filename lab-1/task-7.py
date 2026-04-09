addresses = [
    "www.google",
    "www.youtube.com",
    "mail.ru",
    "www.github",
    "example.org"
]

new_addresses = [
    ("http://" + address if address.startswith("www") else address) +
    ("" if address.endswith(".com") else ".com")
    for address in addresses
]

print(new_addresses)