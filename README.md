# Multilingual-OCR: Extract multilingual text from PDFs  

## Introduction

Multilingual-OCR is an end-to-end text extraction tool which simply inputs a PDF (even large ones!) and outputs a text file with the extracted text, which can be used for further processing. Multilingual-OCR can extract text in multiple languages. 

## Dependencies

1. [pdf2image](https://pypi.org/project/pdf2image/)

   ```pip install pdf2image```

2. [pytesseract](https://pypi.org/project/pytesseract/)

   ```pip install pytesseract```

3. Image (PIL)

   ```pip3 install Image```

4. poppler 
- Install poppler as described [here](https://pypi.org/project/pdf2image/).
- Used for the PDF to Image conversion step.

## Execution

- Select the PDF on which you wish to perform OCR, rename it to ```input.pdf``` and execute ```multilingual-ocr.py``` after updating the necessary paths in it.
- ```multilingual-ocr.py``` is written assuming a Hindi ```input.pdf```. However, for PDFs of other languages, simply update the ```lang``` attribute in ```multilingual-ocr.py```. The language codes for the other languages can be found [here](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc).
- Multilingual-OCR consists of two main steps. The first converts the input PDF to images for all pages in the input PDF. And the second extracts text from the generated images. 
- A sample input PDF in Hindi is given as ```input.pdf```. It is a subset of a larger Hindi PDF file.
- The generated images for ```input.pdf``` are given in ```input_images```. The unformatted and the formatted extracted texts are given in ```output_unformatted.txt``` and ```output_formatted.txt``` respectively.
