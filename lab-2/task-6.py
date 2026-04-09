import os
import shutil
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True)
parser.add_argument("--days", type=int, required=True)
parser.add_argument("--size", type=int, required=True)

args = parser.parse_args()

source = args.source
days_limit = args.days
size_limit = args.size

archive_files = []
small_files = []

now = datetime.now()

for name in os.listdir(source):
    path = os.path.join(source, name)

    if os.path.isfile(path):
        mtime = datetime.fromtimestamp(os.path.getmtime(path))
        diff_days = (now - mtime).days
        file_size = os.path.getsize(path)

        if diff_days > days_limit:
            archive_files.append(path)

        if file_size < size_limit:
            small_files.append(path)

if archive_files:
    archive_dir = os.path.join(source, "Archive")
    os.makedirs(archive_dir, exist_ok=True)
    for path in archive_files:
        new_path = os.path.join(archive_dir, os.path.basename(path))
        if os.path.abspath(path) != os.path.abspath(new_path):
            shutil.move(path, new_path)

if small_files:
    small_dir = os.path.join(source, "Small")
    os.makedirs(small_dir, exist_ok=True)
    for path in small_files:
        if os.path.exists(path):
            new_path = os.path.join(small_dir, os.path.basename(path))
            if os.path.abspath(path) != os.path.abspath(new_path):
                shutil.move(path, new_path)