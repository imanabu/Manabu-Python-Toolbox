# Example to collect files from Directory then compute the hash
# then print the hex digest of the file along with the file name
# It is written for Windows program files but can be used for
# any directory.
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

    
