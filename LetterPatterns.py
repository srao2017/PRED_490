# -*- coding: utf-8 -*-
# We will randomly define initial values for connection weights, and also randomly select
#   which training data that we will use for a given run.

import os
import csv

def get_letters (filename, letter):
    pattern = []
    i = 10
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            #find the letter
            if row[0] in letter:
                print(row[0])
                i = 0;
                continue
            #retrieve the pattern and collapse into one row
            if i < 9:
                pattern = pattern+row
                i+=1
    return pattern

def put_letters (f, pattern, letter_id, letter):

    writer = csv.writer(f)
    writer.writerow(pattern+list([letter_id,str("'")+letter+str("'")]))

def main():
    out_dir = "C:/EDUCATION/NWU/490 - Deep Learning/Week 4/Create Letter Patterns"
    filename = "ABCD"
    letters = list(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    os.chdir(out_dir)
    f = open(filename+str("_out.txt"),"wb")
    
    for letter in letters:
        letter_id = ord(letter) - ord('A') 
        pattern = get_letters(str(filename)+str(".csv"),[letter])
        put_letters(f,pattern, letter_id, letter)
        
    f.close()
if __name__ == "__main__": main()
