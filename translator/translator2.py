import os
from os import linesep
import googletrans

os.chdir(os.path.dirname(os.path.abspath(__file__)))

translator = googletrans.Translator()

read_file_path=r"./영어파일.txt"
###경로를 직접 줘도 되고, cd로 줘도 됨
###read_file_path = r"C:\Users\0\Desktop\python 2.19\python40-main\9.translator\영어파일.txt"

with open(read_file_path,'r') as f :
    readLines=f.readlines()

for lines in readLines:
    result1=translator.translate(lines,dest='ko')
    print(result1.text)