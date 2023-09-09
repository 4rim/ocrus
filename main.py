from textblob import TextBlob
import pytesseract
# import argparse
import cv2
from pathlib import Path
import glob
import sys
import os
import timeit
import threading 
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

data_lock = threading.Lock()

def is_path_valid(path_name):
    if not os.path.exists(path_name):
        sys.exit(f'''Path does not exist! Please create one with the
        command: touch {path_name} for files, or: mkdir {path_name} for
        directories.''')

def empty_file(file_name):
    if not os.path.getsize(file_name) == 0:
        file = open(file_name, 'w')
        file.close

def do_ocr(file_name):
    img_file = os.fspath(file_name)
    image = cv2.imread(img_file)
    wrapped = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(wrapped, config = "-l rus")
    
    os.chdir('../')

    with open(output, "a") as output_file, data_lock:
        sys.stdout = output_file
        print(text)
    
    os.chdir(image_path)

start_time = timeit.default_timer()
temp = sys.stdout

# instantiate Pool objects in code
pool = ThreadPool()

# setup: do all files/paths exist?
output = Path("output.txt").resolve()
is_path_valid(output)
empty_file(output)

image_path = Path("images").resolve()
is_path_valid(image_path)

os.chdir(image_path)

# creates a list of all image files w extension .png
file_list = glob.glob("*.png")

pool.map(do_ocr, file_list)
pool.close()
pool.join()

stop_time = timeit.default_timer()

sys.stdout = temp
print("All done! Time: ", stop_time - start_time)
