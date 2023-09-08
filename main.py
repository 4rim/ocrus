from textblob import TextBlob
import pytesseract
import argparse
import cv2
from pathlib import Path
import glob
import sys
import os
import timeit

start_time = timeit.default_timer()
temp = sys.stdout

# setup: do all files/paths exist?
output = Path("./output.txt")
if not output.is_file():
    sys.exit('''output.txt does not exist! Please create one with the command
             touch output.txt.''')

image_path = Path('./images')

if image_path.exists():
    os.chdir(image_path)
    # creates a list of all files w extension .png
    file_list = glob.glob("*.png")
    for idx, file in enumerate(file_list):
        img_file = os.fspath(file)
        image = cv2.imread(img_file)
        wrapped = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        text = pytesseract.image_to_string(wrapped, config = "-l rus")
        os.chdir("../")
        
        with open(output, "a") as output_file:
            sys.stdout = output_file
            print(text)

        os.chdir(image_path)
else:
    sys.exit=('''Image path doesn't exist! Set one up with the command mkdir
              images.''')

stop_time = timeit.default_timer()

sys.stdout = temp
print("All done! Time: ", stop_time - start_time)

