"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Mercado, John Andhrie M.]
Date: [09-26-2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
built a Python script that automatically organizes 
a messy folder by sorting files into separate 
subdirectories based on their file extensions

============================================
KEY VOCABULARY
============================================
- os module: A built in Python tool used to interact with your operating system
- shutil module: A Python tool used for file operations like moving, 
copying, or deleting files and folders.
- file path: : The exact address pointing to a file or folder on your computer.
- directory: A folder that holds files and other subfolders.


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

target_dir = "./messy_folder"

for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)
    
    if os.path.isfile(file_path):
        ext = filename.split(".")[-1].lower()
        ext_folder = os.path.join(target_dir, ext)
        
        os.makedirs(ext_folder, exist_ok=True)
        
        shutil.move(file_path, os.path.join(ext_folder, filename))

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Trying to move a file into a folder that didn't exist yet. At first, 
my script crashed because shutil.move couldn't find the destination 
directory. I learned to use os.makedirs(..., exist_ok=True) 
first to automatically create the folder if it's missing.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
It connects to my previous expense tracker project. 
Instead of manually organizing downloaded receipt PDF 
into separate folders, an automation script like this 
could instantly sort them for you in seconds.
"""
