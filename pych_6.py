import zipfile
import re
import os


default_number = "90052"
ourZip = "channel.zip"
pattern = re.compile("Next nothing is (\d+)")
comments = []

file = zipfile.ZipFile(ourZip, 'r')

while True:
    content = file.read(default_number+'.txt').decode('UTF-8')
    print(content)
    comments.append(file.getinfo(default_number+'.txt').comment.decode('UTF-8'))
    hit = pattern.search(content)
    if hit == None:
        break
    default_number = hit.group(1)

print("".join(comments))
