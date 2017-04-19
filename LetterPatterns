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
                print(row)
                i = 0;
                continue
            #retrieve the pattern and collapse into one row
            if i < 9:
                pattern = pattern+row
                i+=1
    return pattern

def put_letters (filename, pattern, letter_id, letter):
       
    f = open(filename+str("_out.txt"),"ab")
    writer = csv.writer(f)
    writer.writerow(pattern+list([letter_id,str("'")+letter+str("'")]))
    f.close()
    
def main():
    out_dir = "C:/EDUCATION/NWU/490 - Deep Learning/Week 4"
    filename = "ABCD"
    letters = list(['A','B','X'])
    os.chdir(out_dir)
    
    for letter in letters:
        letter_id = ord(letter) - ord('A') 
        pattern = get_letters(str(filename)+str(".csv"),[letter])
        put_letters(filename,pattern, letter_id, letter)
    
if __name__ == "__main__": main()
