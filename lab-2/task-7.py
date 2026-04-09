import os
import random
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--source", "-s", required=True)
parser.add_argument("--destination", "-d")
parser.add_argument("--count", "-c", type=int)
parser.add_argument("--frame", "-f", type=int, default=10)
parser.add_argument("--log", "-l", action="store_true")
parser.add_argument("--extended", "-e", action="store_true")

args = parser.parse_args()

source = args.source
destination = args.destination
count = args.count
frame = args.frame

if destination is None:
    destination = os.path.join(source, "mix.mp3")

files = [f for f in os.listdir(source) if f.lower().endswith(".mp3")]
files.sort()

if count is not None:
    files = files[:count]

temp_files = []

for i, name in enumerate(files, start=1):
    input_path = os.path.join(source, name)
    temp_path = os.path.join(source, f"part_{i}.mp3")

    if args.log:
        print(f"--- processing file {i}: {name}")

    start_time = random.randint(0, 20)

    command = [
        "ffmpeg",
        "-y",
        "-ss", str(start_time),
        "-t", str(frame),
        "-i", input_path
    ]

    if args.extended:
        command += [
            "-af", "afade=t=in:ss=0:d=1,afade=t=out:st={}:d=1".format(max(frame - 1, 0))
        ]

    command.append(temp_path)

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    temp_files.append(temp_path)

list_path = os.path.join(source, "files.txt")

with open(list_path, "w", encoding="utf-8") as file:
    for temp_file in temp_files:
        file.write(f"file '{temp_file}'\n")

command = [
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", list_path,
    "-c", "copy",
    destination
]

subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for temp_file in temp_files:
    if os.path.exists(temp_file):
        os.remove(temp_file)

if os.path.exists(list_path):
    os.remove(list_path)

if args.log:
    print("--- done!")