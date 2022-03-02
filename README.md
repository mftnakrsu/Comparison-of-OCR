# Optical Character Recognition

OCR (Optical Character Recognition) is a technology that enables the conversion of document types such as scanned paper documents, PDF files or pictures taken with a digital camera into editable and searchable data. OCR creates words from letters and sentences from words by selecting and separating letters from images.

![robot](https://user-images.githubusercontent.com/57320216/156442638-c681624f-a8cd-45ed-a4cc-8a626d295f46.jpg)


## Requirements

    pip install -r requirements.txt
    
## Usage

    python main.py
    
 ## Results
 ![kerasocr1](https://user-images.githubusercontent.com/57320216/156442703-ff06fce6-174a-4859-9d45-b32b4187b1d5.png)
![kerasocr2](https://user-images.githubusercontent.com/57320216/156442709-cea41264-e369-48a3-92b0-afa752c313fb.png)
![kerasocr3](https://user-images.githubusercontent.com/57320216/156442712-c05cbf58-0c9b-41fa-bd7b-c42704194527.png)

 
 ## Conclusion
 
 - It seems that pytesseract is not very good at detecting text in the entire image and converting str. Instead, text should be detected first with text detection and the texts have to given OCR engines.
 
 - While keras_ocr is good in terms of accuracy but it is costly in terms of time. Also if you’re using CPU, time might be an issue for you.
Keras-OCR is image specific OCR tool. If text is inside the image and their fonts and colors are unorganized.

- Easy-OCR is lightweight model which is giving a good performance for receipt or PDF conversion. It is giving more accurate results with organized texts like PDF files, receipts, bills. Easy OCR also performs well on noisy images.

- Pytesseract is performing well for high-resolution images. Certain morphological operations such as dilation, erosion, OTSU binarization can help increase pytesseract performance.
    

- All these results can be further improved by performing specific image operations. OCR Prediction is not only dependent on the model and also on a lot of other factors like clarity, grey scale of the image, hyper parameter, weight age given, etc.
 
    
 ## Source
 https://github.com/faustomorales/keras-ocr  
 https://github.com/JaidedAI/EasyOCR  
 https://pypi.org/project/pytesseract/  
