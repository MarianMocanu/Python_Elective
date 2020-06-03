import csv
import requests, json
import urllib.request

url = 'https://link.springer.com/book/10.1007%2Fb99417'
r = urllib.request.urlopen(url)

print(r.read())

# # with open('file.pdf', 'wb') as f:
# #     f.write(r.content)


# with open("springer.csv", encoding="utf8") as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     for row in csv_reader:
#         if row[2] == "Computer Science":
#             print(row)
