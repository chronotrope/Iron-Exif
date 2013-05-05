__author__ = "Ruben Robles"

"""This Python module will be used to interacte with the exiftools.exe windows executable.  It will be used to pass arguments as Python functions
		
		exif.startExif('_DSC0688.JPG','_DSC0688edited.JPG',1)
		C:\Users\ruben\Documents\SharpDevelop Projects\Iron-Exif\Iron-Exif
		>>> import ExifCommands as exif
Usage example:
>>> import clr
>>> s1 = exif.ExifCommands('_DSC0688.JPG','_DSC0688edited.JPG',1)
>>> myargs = s1.startExif()
>>> myargs
'/c exiftool.exe -tagsfromfile _DSC0688.JPG -all:all _DSC0688edited.JPG'
>>> p = Process()
>>> p.StartInfo.UseShellExecute = True
>>> p.StartInfo.FileName = 'CMD.exe'
>>> p.StartInfo.Arguments = myargs
>>> p.Start()
True
>>>
		
		"""


from System.Diagnostics import Process
import sys
sys.path.append("C:\Program Files\IronPython 2.7\Lib")
import os
		



class ExifCommands:
	
	def __init__(self, exifParam1, exifParam2=None, exifSwitch):
		
		##self.exifParam1 = os.getcwd()+'\\'+exifParam1
		##self.exifParam2 = os.getcwd()+'\\'+exifParam2
		self.exifParam1 = exifParam1
		self.exifParam2 = exifParam2
		
		self.exifSwitch = exifSwitch
		self.myTools = {1:"/c exiftool.exe -tagsfromfile "+ self.exifParam1 + " -all:all " + self.exifParam2, 2:"/c exiftool.exe "+ self.exifParam1 + " > " + " rgrmyexifoutpu2t.txt"}
		self.mySwitch = self.myTools[self.exifSwitch]
	
	def printCWD(self):
		print os.getcwd()
		
	def startExif(self):		
		
		return self.mySwitch
    	
    	