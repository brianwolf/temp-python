#!/usr/bin/python

import os

# # traverse root directory, and list directories as dirs and files as files
# for root, dirs, files in os.walk("./logic"):
#     path = root.split(os.sep)
#     print((len(path) - 1) * '---', os.path.basename(root))
#     for file in files:
#         print(len(path) * '---', file)

archivos = []

for root, dirs, files in os.walk("./logic/app/routes"):

    if '__pycache__' in root or not files:
        continue
    
    archivos.extend([
        os.path.join(root, file)
        for file in files
    ])

    # print(root, files, '\n\n')

print(archivos)