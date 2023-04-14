# This is my Invoice OCR project, also my first project about Computer Vision
To extract the information from the invoice, I use the following steps:
1. Read the image
2. Preprocess the image
3. Extract the text from the image
4. Extract the information from the text
5. Save the information to json file
---
To run the project, you need to install the following packages using requirements.txt file:
```bash
conda install --yes --file requirements.txt
```
---
To run the project, you need to run the following command:
```bash
python main.py
```
---
To train the model, you need to run the following steps:
1. Download the pretrained weight from [here](https://drive.google.com/drive/folders/10EuvYr2NM3NsNZVjfpdiw_TUzRUyayzb?usp=share_link)
2. Copy and paste the weight to the project folder './YOLO/yolov5/weight'
3. Run the following command:
```bash
cd YOLO/yolov5
python train.py --img 416 --batch 16 --epochs 150 --data {dataset.location}/data.yaml --weights {weight.name}.pt --cache
```
for example:
```bash
python train.py --img 640 --batch 20 --epochs 200 --data custom_data.yaml --weights best.pt --cache
```
---
If you have any questions, please contact me via email: [duypnt23@gmail.com](mailto: duypnt23@gmail.com)

Thanks for reading!