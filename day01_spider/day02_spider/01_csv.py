import csv

with open('spider.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['123', 'hahahh'])

with open('spider.csv', 'a',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([('156','kajsahudi'),('125','15649')])
