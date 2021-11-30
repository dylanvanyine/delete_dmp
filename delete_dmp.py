import os
from tkinter import Tk,filedialog,messagebox
import time

Tk().withdraw()
folder=filedialog.askdirectory(title='Select a folder to delete dmp')

choice = messagebox.askquestion(title='Continue?',message='All dmp files inside will be deleted.\nContinue?')

if choice == 'yes':
    walk = os.walk(folder)

    start = time.time()
    i=0
    j=0

    for path,folders,files in walk:
        for file in files:
            root,ext = os.path.splitext(file)
            i+=1
            if ext == '.dmp':
                j+=1
                os.remove(os.path.join(path,file))
            else:
                continue

    end = time.time()
    elapsed = round(end-start,1)
    print(f'\n{i} files checked.')
    print(f'{j} files deleted.')
    print(f'{elapsed} seconds elapsed.')
    input('\nPress Enter to finish.')
else:
    print(f'No files deleted')
    input('\nPress Enter to finish.')

