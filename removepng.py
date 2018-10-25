#Removes non-background images from the Windows Spotlight Img Directory. Helps to clean things up before renaming all the files. 
import imghdr
import os
files = os.listdir()
i = 0
while i < len(files):
	x = imghdr.what(files[i])
	print(x)
	if x == 'png':
		print("This is a PNG, so into the trash it goes.")
		os.remove(files[i])
	else:
		print("This is either a JPG or something else, so its cool")
	i +=1