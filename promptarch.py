import csv
import random
from csv import DictReader
import numpy as np
import pandas as pd


with open('types1.csv') as a1:
    reader = csv.reader(a1)
    chosen_row1 = random.choice(list(reader))
# print (chosen_row1)

with open('style1.csv') as b1:
    reader = csv.reader(b1)
    chosen_row2 = random.choice(list(reader))
# print (chosen_row2)

with open('preps1.csv') as c1:
    reader = csv.reader(c1)
    chosen_row3 = random.choice(list(reader))
# print (chosen_row3)

with open('biome1.csv') as d1:
    reader = csv.reader(d1)
    chosen_row4 = random.choice(list(reader))
# print (chosen_row4)

with open('archlist1.csv') as e1:
    reader = csv.reader(e1)
    chosen_row5 = random.choice(list(reader))
# print (chosen_row5)

with open('colors1.csv') as f1:
    reader = csv.reader(f1)
    chosen_row6 = random.choice(list(reader))
# print (chosen_row6)

with open('formmod1.csv') as g1:
    reader = csv.reader(g1)
    chosen_row7 = random.choice(list(reader))
# print (chosen_row7)

with open('materials1.csv') as h1:
    reader = csv.reader(h1)
    chosen_row8 = random.choice(list(reader))
# print (chosen_row8)

with open('actions1.csv') as i1:
    reader = csv.reader(i1)
    chosen_row9 = random.choice(list(reader))
# print (chosen_row9)

with open('storeys1.csv') as j1:
    reader = csv.reader(j1)
    chosen_row10 = random.choice(list(reader))
# print (chosen_row10)

def csv_writer(data, path):

    with open(path, "w", newline='' ) as csv_file:
        writer = csv.writer(csv_file, delimiter='&')
        for line in data:
            writer.writerow(line)

data = [chosen_row10, chosen_row1, chosen_row2, chosen_row5, chosen_row9, chosen_row7, chosen_row3, chosen_row4, chosen_row6, chosen_row8]

csv_writer(data, "transform1.csv")

pd.read_csv('transform1.csv', header=None).T.to_csv('transform2.csv', header=False, index=False)

text = open("transform2.csv", "r")
text = ''.join([i for i in text]) \
    .replace("&", " ")
x = open("transform3.csv","w")
x.writelines(text)
x.close()

text = open("transform3.csv", "r")
text = ''.join([i for i in text]) \
    .replace(",", " ")
x = open("prompt.csv","w")
x.writelines(text)
x.close()


# input_file = open('transposed.csv', 'r')
# output_file = open('fixedfinal.csv', 'w')

# data = csv.reader(input_file)
# writer = csv.writer(output_file)# dialect='excel')
# specials = '&'

# for line in data:
#     line = str(line)
#     new_line = str.replace(line,specials,'')
#     writer.writerow(new_line.split(' '))

# input_file.close()
# output_file.close()