import os


workdir = input ("Enter the folder to scan: ")
totalSize = []

for filename in os.listdir(input ('workdir'):
    totalSize = totalSize + os.path.getsize(os.path.join('workdir', filename))
    print(totalSize)