#Finds any background images from Windows Spotlight that are in a JPEG format using imghdr
import os
import imghdr

arr = os.listdir()
i = 0
while i < len(arr):
    x = imghdr.what(arr[i])
    if x == 'jpeg':
        print (arr[i])
        src = arr[i]
        dst = arr[i] + ".jpg"
        print ("Changing file name...")
        os.rename(src, dst)
    else:
        print("Nothing to do with this one")
    i +=1