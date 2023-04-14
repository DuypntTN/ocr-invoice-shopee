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
