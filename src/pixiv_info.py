from pathlib import Path 
from PIL import Image
root = Path(__file__).parent.parent/"image/pixiv/"

files = [x for x in root.rglob('*') if x.is_file() and x.suffix!=".csv"]

for img in files:
    imgg = Image.open(img)
    w,h = imgg.size
    imgg.close()
    if h/w < 0.8:
        aim_dir = "horizontal"
    elif h/w > 1.25:
        aim_dir = "vertical"
    else:
        aim_dir = "square"
    aim_path = root/aim_dir/img.parent.name/img.name 
    if aim_path == img:
        continue
    if aim_path.exists():
        aim_path.unlink()
    else:
        aim_path.parent.mkdir(parents=True,exist_ok=True)
        img.rename(aim_path)

files = [x for x in root.rglob('*') if x.is_file() and x.suffix!=".csv"]

with open(root/"file_list.csv","w") as f:
    for fl in files:
        f.write(f"{fl.relative_to(root.parent.parent).as_posix()}\n")