import threading
import requests

def download(url):
    name = url.split("/")[-1]
    r = requests.get(url, stream=True)

    with open(name, "wb") as f:
        for chunk in r.iter_content(4096):
            f.write(chunk)

urls = [
    input("URL1: "),
    input("URL2: "),
    input("URL3: ")
]

threads = []

for url in urls:
    if url:
        t = threading.Thread(target=download, args=(url,))
        t.start()
        threads.append(t)

for t in threads:
    t.join()

print("Готово")