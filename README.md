Automated method for converting Windows Spotlight lock screen images into JPGs for use within Windows for wallpapers, etc. This was just a 45min coding challenge that will eventually be built out to eliminate the manual steps involved in using it. 

1. Copy files to %appdata%\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
2. Run removepng.py first to remove any of the junk asset files that are stored in a png format. 
3. Run spotlightimg.py to find all of the JPG images and add an extension to them so they are usable from Windows

Future features
===========================
- Single file that can be run from anywhere since the directory is the same on any Win10 install
- Backup files to an 'spotlight_imgs' dir on the desktop and delete/rename files in one swoop
