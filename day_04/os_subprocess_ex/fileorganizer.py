import os
import os.path
import shutil

os.chdir(r"complete_path_to_mydir")
files = os.listdir()
exts = set([os.path.splitext(file)[1][1:] for file in files])

for ext in exts:
	os.mkdir(ext)

for file in files:
	src = file # data1.txt
	destfolder = os.path.splitext(file)[1][1:]
	finaldest = os.path.join(destfolder, src) # txt/data1.txt
	shutil.move(src, finaldest)
