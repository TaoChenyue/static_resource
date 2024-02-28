import tinify
from pathlib import Path
from tqdm import tqdm

with open("key.txt","r") as f:
    key = f.read().strip()

def compress_image(src:str,out:str):
    try:
        tinify.key = key
        source = tinify.from_file(src)
        source.to_file(out)
    except tinify.Error as error:
        print('TinyPNG error: ' + error.message)

if __name__ == '__main__':
    root = input("Input Path: ")
    root = Path(root)
    if not (root.exists() and root.is_dir()):
        print("Path not valid! ")
        exit(1)
    files:list[Path] = []
    suffix_list = ["*.jpg","*.png"]
    for suffix in suffix_list: 
        files += [x for x in root.rglob(suffix)]
    for f in tqdm(files):
        compress_image(f.as_posix(),f.as_posix())