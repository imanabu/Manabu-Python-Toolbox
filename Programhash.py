import hashlib
import os
serverDir = "c:\\program files\\someprogram"
files = os.listdir(serverDir)
for f in files :
    found = 0
    f = f.lower()
    if (f.find('.exe') > 0) :
        found = 1
    if (f.find('.dll') > 0) :
        found = 1
    if (found) :
        print f  + ": " + hashlib.md5(f).hexdigest()

    
