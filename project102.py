Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from_dir="/Users/cs/Downloads"
to_dir= "/Users/cs/Documents/Document_Files"
list_of_files=os.listdir(from_dir)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list_of_files=os.listdir(from_dir)
NameError: name 'os' is not defined
import os
import shutil
from_dir="/Users/cs/Downloads"
to_dir= "/Users/cs/Documents/Document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
['839f5aa2-a5f7-4989-8e5c-7feb91fca60c.pdf', 'SA-1 English Answer Key (1).pdf', 'Answer sheet E.V.S (1).pdf', '.DS_Store', 'SA-1 English Answer Key.pdf', '.localized', 'IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf', '$RECYCLE.BIN', 'Olympiad circular.docx', 'SHP Module 1_Take home message.pdf', 'pro-84', 'github.com', 'desktop.ini', 'SA-1 (Answerkey)class1.pdf', 'SA-1 Mathematics (Answer Key).pdf']
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension== "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+ "Document_File"
        path3 = to_dir+'/'+ "Document_File"+'/'+file_name
        print("path1",path1)
        print("path3",path3)
    if os.path.exists(path2):
        print("Moving"+file_name+ ".....")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("Moving"+file_name+ ".....")
        shutil.move(path1,path3)

839f5aa2-a5f7-4989-8e5c-7feb91fca60c
.pdf
path1 /Users/cs/Downloads/839f5aa2-a5f7-4989-8e5c-7feb91fca60c.pdf
path3 /Users/cs/Documents/Document_Files/Document_File/839f5aa2-a5f7-4989-8e5c-7feb91fca60c.pdf
Moving839f5aa2-a5f7-4989-8e5c-7feb91fca60c.pdf.....
'/Users/cs/Documents/Document_Files/Document_File/839f5aa2-a5f7-4989-8e5c-7feb91fca60c.pdf'
SA-1 English Answer Key (1)
.pdf
path1 /Users/cs/Downloads/SA-1 English Answer Key (1).pdf
path3 /Users/cs/Documents/Document_Files/Document_File/SA-1 English Answer Key (1).pdf
MovingSA-1 English Answer Key (1).pdf.....
'/Users/cs/Documents/Document_Files/Document_File/SA-1 English Answer Key (1).pdf'
Answer sheet E.V.S (1)
.pdf
path1 /Users/cs/Downloads/Answer sheet E.V.S (1).pdf
path3 /Users/cs/Documents/Document_Files/Document_File/Answer sheet E.V.S (1).pdf
MovingAnswer sheet E.V.S (1).pdf.....
'/Users/cs/Documents/Document_Files/Document_File/Answer sheet E.V.S (1).pdf'
.DS_Store

SA-1 English Answer Key
.pdf
path1 /Users/cs/Downloads/SA-1 English Answer Key.pdf
path3 /Users/cs/Documents/Document_Files/Document_File/SA-1 English Answer Key.pdf
MovingSA-1 English Answer Key.pdf.....
'/Users/cs/Documents/Document_Files/Document_File/SA-1 English Answer Key.pdf'
.localized

IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23
.pdf
path1 /Users/cs/Downloads/IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf
path3 /Users/cs/Documents/Document_Files/Document_File/IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf
MovingIT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf.....
'/Users/cs/Documents/Document_Files/Document_File/IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf'
$RECYCLE
.BIN
Moving$RECYCLE.BIN.....
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/shutil.py", line 805, in move
    os.rename(src, real_dst)
FileNotFoundError: [Errno 2] No such file or directory: '/Users/cs/Downloads/IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf' -> '/Users/cs/Documents/Document_Files/Document_File/IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#9>", line 15, in <module>
    shutil.move(path1,path3)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/shutil.py", line 825, in move
    copy_function(src, real_dst)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/shutil.py", line 434, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/shutil.py", line 254, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/cs/Downloads/IT- CLASS 1- SUMMATIVE ASSESSMENT-2022-23.pdf'
