import os
from os import linesep
import googletrans

os.chdir(os.path.dirname(os.path.abspath(__file__)))

translator =googletrans.Translator()

read_file_path=r"translate_autosave_txt\thanks_en.txt"
write_file_path=r"translate_autosave_txt\thanks_kor.txt"

with open(read_file_path,'r') as f:
    readlineS=f.readlines()

for lines in readlineS:
    result1=translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path,'a',encoding='UTF8') as f :
        f.write(result1.text+'\n')