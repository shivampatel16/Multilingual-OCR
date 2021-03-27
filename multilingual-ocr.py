import pdf2image          # To convert a PDF to a sequnce of PIL image objects.
from PIL import Image     # To convert PIL image objects into png or jpg file formats   
import os 
import pytesseract
import subprocess

###
# Step 1 - Converting PDF to Images
###

resolution = 200
pdf_path = "input.pdf"

# Update the path to poppler
pil_images = pdf2image.convert_from_path(pdf_path, dpi=resolution, poppler_path= r'C:/path/to/poppler-xx/bin')

###
# Step 2 - Convert a sequnce of PIL image objects to required image format and store the images at the required location
###

# Update the path to current working directory
os.chdir("C:/Users/path/to/current_working_directory/")
new_folder_name = "input" + "_images"
subprocess.call("mkdir " + new_folder_name, shell = True)

index=1
for image in pil_images:
    print("Converting page", index)
    image.save("input_images/" + "page_" + str(index) + ".PNG")
    index += 1

###
# Step 3 - Extracting text from images
###	

total_pages = index - 1
text = ""

#Update the language (in the 'lang' attribute) as required. Ex: "lang = 'guj'" for Gujarati
for i in range(total_pages):
    print("Extracting text from page", i + 1)
    im = Image.open("input_images/page_" + str(i + 1) + ".PNG")
    text = text + pytesseract.image_to_string(im, lang = 'hin')

# Store unformatted text (broken sentences of a paragraph as they appear in the PDF) to a text file. 
with open("output_unformatted.txt", "w", encoding="utf-8") as myfile:
    myfile.write(text)

###
# Step 4 - Formatting extracted text. Combines segments of a paragraph (broken sentences) in the unformatted text into a single paragraph.
###		

edited_text = ""

for i in range(len(text)):
    if text[i] == "\n" and text[i+1] != "\n" and text[i-1] != "\n":
        edited_text = edited_text + " "
    else:
        edited_text = edited_text + text[i]
        
# Store formatted text to a text file
with open("output_formatted.txt", "w", encoding="utf-8") as myfile:
    myfile.write(edited_text)