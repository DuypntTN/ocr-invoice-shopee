from YOLO.yolov5.detect import start_detect_v2
from OCR.OCR import OCR
from pathlib import Path
import sys
import os
import json
# Get the root path of the project
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

print("Root", ROOT)
start_detect_v2()

# Get root image list
root_image = ROOT / "YOLO" / "yolov5" / "data" / "images"
root_image_list = list()
for file in root_image.iterdir():
    if file.is_file():
        root_image_list.append(str(file.name.split(".")[0]))
print("IMAGE LIST", root_image_list)


ocr = OCR(ROOT=ROOT, root_image_list=root_image_list)
ocr.getItemToOCR()
arr = ocr.runOCR()
# ocr.printOutputOCR()
