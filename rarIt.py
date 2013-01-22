#! /bin/python

import os
import zipfile

class rarIt:
	def __init__(self):
		self.extension='.jpg'
		self.path='./'
		self.fileList=[]
		fileAndDirectoryList = os.listdir(self.path)
		self.nameOfRarFile=1

		for fileName in fileAndDirectoryList:
			fileName = self.path + '/' + fileName
			if(fileName[-len(self.extension):] == self.extension):
				self.fileList.append(os.path.relpath(fileName))
				self.fileList = sorted(self.fileList)
		# print self.fileList

	def chooseFile(self):
		size = 0
		megaBajt = 1048576
		filesToZip = []
		for file in self.fileList:
			fileSize = os.path.getsize(file) 
			# print 'fileSize: ', fileSize, ' size: ', size, ' maxSize: ', 20*megaBajt
			if size + fileSize < 20 * megaBajt:
				size += fileSize
				filesToZip.append(file)
			else:
				self.addToRar(filesToZip)
				self.nameOfRarFile += 1
				size = 0
				del filesToZip[:]
				filesToZip.append(file)

	def addToRar(self, files):
		# print file
		zipName = 'zdjecia' + str(self.nameOfRarFile) + '.zip'
		compressedFile = zipfile.ZipFile(zipName, "a", zipfile.ZIP_DEFLATED)
		for file in files:
			print file
			compressedFile.write(file)

















def main():
	rar = rarIt()
	rar.chooseFile()


if __name__ == "__main__":
	main()