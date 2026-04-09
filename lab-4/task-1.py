import os
import struct

directory = input("Путь к папке: ")

for file in os.listdir(directory):
    if file.endswith(".mp3"):
        path = os.path.join(directory, file)

        with open(path, "rb") as f:
            f.seek(-128, 2)
            tag = f.read(128)

            if tag[:3] == b'TAG':
                data = struct.unpack("3s30s30s30s4s30s", tag)

                title = data[1].decode().strip('\x00')
                artist = data[2].decode().strip('\x00')
                album = data[3].decode().strip('\x00')

                print(f"{artist} - {title} - {album}")