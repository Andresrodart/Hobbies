#!/usr/bin/env python3
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import zipfile
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilenames(title='Choose a file')
print(list(filename))
fantasy_zip = zipfile.ZipFile('./archive.zip', 'w')
for s in list(filename):
    fantasy_zip.write(s, os.path.basename(s))
fantasy_zip.close()
