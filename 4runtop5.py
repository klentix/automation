from collections import defaultdict
import csv

f = csv.reader(open('cast.csv','r',encoding = 'utf-8'))
writer = csv.writer(open('main_cast.csv','w'))



# count all the emails before we write anything out
names = defaultdict(int)
for row in f:
    names[row[0]] += 1
sort_order = sorted(names.items(), key=lambda item: item[1], reverse=True)[0:5]
print(sort_order)
# now write the file
for i in sort_order:
    writer.writerow(i)





