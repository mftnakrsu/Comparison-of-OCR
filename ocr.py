import cv2
import os
import keras_ocr
import numpy as np
import pytesseract
import easyocr
import matplotlib.pyplot as plt

class OCR():
    
    def __init__(self,image_folder):
        
        self.image_folder= image_folder
        self.images = self.load_images_from_folder()
        self.pipeline = self._keras_model_load()
        self.text_reader=self._easyocr_model_load()

    def load_images_from_folder(self):
        images = []
        for filename in os.listdir(self.image_folder):
            img = cv2.imread(os.path.join(self.image_folder,filename))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

            if gray is not None:
                images.append(gray)
        return images

    def _keras_model_load(self):
        pipeline = keras_ocr.pipeline.Pipeline()
        return pipeline

    def keras_ocr_works(self,visualization=True):
        images = [keras_ocr.tools.read(img) for img in self.load_images_from_folder()]
        prediction_groups = self.pipeline.recognize(images) # prediction
        
        if visualization:
            fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
            for ax, image, predictions in zip(axs, images, prediction_groups):
                #print(predictions)
                keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
                
                
    def _easyocr_model_load(self):
        text_reader = easyocr.Reader(['tr','en']) #Initialzing the ocr
        return text_reader

    def easyocr_model_works(self,visualization=True):
        for i in range(len(self.images)):
            results = self.text_reader.readtext(self.images[i] )
            for (bbox, text, prob) in results:
                print(text)
            if visualization:
                plt.imshow(self.images[i])
                plt.title("{} Image".format(str(i)));
                plt.show()

    def pytesseract_model_works(self,visualization=True):
    
        tesseract_preds = []
        for img in self.images:
            tesseract_preds.append(pytesseract.image_to_string(img))

        for i in range(len(self.images)):
            print(tesseract_preds[i])

            if visualization:
                plt.imshow(self.images[i])
                plt.title("{} Image".format(str(i)));
                plt.show()