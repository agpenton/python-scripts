import os


workfol = input ("Enter the folder to scan: ")

totalSize = []

for filename in os.listdir(input ('workfol'):
    totalSize = totalSize + os.path.getsize(os.path.join('workfol', filename))
    print(totalSize)