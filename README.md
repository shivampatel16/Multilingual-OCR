# Multilingual-OCR: Extract multilingual text from PDFs  

## Introduction

Multilingual-OCR is an end-to-end text extraction model which simply inputs a PDF (even large ones!) and outputs a text file with the extracted text, which can be used for further processing. Multilingual-OCR can extract text in multiple languages. 

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
