from pathlib import Path
import sys
import os
import cv2
import pytesseract
from matplotlib import pyplot as plt
import re
import json
class Object:
    def __init__(
        mysillyobject,
        **args
    ) -> None:
        for key, value in args.items():
            setattr(mysillyobject, key if key is not None else "", value)

    def print(
        mysillyobject
    ) -> None:
        print(mysillyobject.__dict__)


class OCR:
    def __init__(
        self,
        **args: dict
    ) -> None:
        self.ROOT = args.get("ROOT", Path(__file__).resolve().parents[0])
        # init classes
        """
            1: "fromAdress"
            2: "toAdress"
            3: "invoiceCode"
            4: "totalPrice"
        """
        self.classes = args.get("classes", tuple(
            ["fromAddress", "toAddress", "invoiceCode", "totalPrice"]))
        self.num_classes = len(self.classes)
        self.output_obj = list()
        # root image list
        self.root_image_list = args.get(
            "root_image_list", list())
        # input image path
        self.input_image_dir = args.get(
            "input_image_dir", self.ROOT / "YOLO" / "yolov5" / "runs" / "detect" / "exp"/"crops")
        self.ListItemToOCR = dict()

    def getItemToOCR(self) -> dict:
        # get all subfolders in input_image_dir
        for folder in self.input_image_dir.iterdir():
            if folder.is_dir():
                self.ListItemToOCR[folder.name] = list()
                for file in folder.iterdir():
                    if file.is_file():
                        self.ListItemToOCR[folder.name].append(file)
        return self.ListItemToOCR

    def runOCR(self) -> dict:
        pytesseract.pytesseract.tesseract_cmd = r'D:\ComputerVision\Tesseract_Root\tesseract.exe'
        """
        Run OCR on all images in ListItemToOCR

        ListItemToOCR = {
            "fromAddress": [
                path,
                path,
                ...
            ],
            "toAddress": [
                path,
                path,
            ],
            ...
        }

        for each image in ListItemToOCR:
            run OCR
            get result
            save result to output_obj
        
        output_obj = 
        [
                {
                    "fromAddress": "text",
                    "toAddress": "text",
                    "invoiceCode": "text",
                    "totalPrice": "text"
                }
                ...
        ]
        """
        for im_r in self.root_image_list:
            ob_item = Object()
            for key, value in self.ListItemToOCR.items():
                for cl in self.classes:
                    if cl == key:
                        for im in value:
                            if im_r in str(im):
                                image = cv2.imread(str(im))
                                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                                image = cv2.resize(image, None, fx=1.5, fy=1.5,
                                                interpolation=cv2.INTER_CUBIC)
                                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                gray = cv2.threshold(
                                    gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                                gray = cv2.medianBlur(gray, 3)
                                # get result
                                text = pytesseract.image_to_string(gray, lang='vie')
                                setattr(ob_item, cl, text)
            self.output_obj.append(Object(
                im = im_r,
                val = ob_item.__dict__
            ).__dict__)
        ## save as json
        print(self.output_obj)
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(self.output_obj, f, ensure_ascii=False, indent=4)
            
    


        return self.output_obj

            
        


    def printOutputOCR(self) -> None:
        for item in self.output_obj:
            print(item.__dict__)
