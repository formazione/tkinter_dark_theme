
# coding: utf-8

'''
png image generator using inkscape like call

steps are :
- get used image name in styleTclScript.
- seek in svgAmalgameFile for element-id that is the image name.
- generate the png in imageDir

module members are :
- inkscapeCmd     : inkscape like command
- styleTclScript  : style implemantation script
- svgAmalgameFile : svg file contaning all image elements with id equals to used image names
- imageDir        : outpur image directory
'''

import os
import re

inkscapeCmd = 'inkscape'
styleTclScript = os.path.join(os.path.dirname(__file__), 'azure_dark', 'azure dark.tcl')
svgAmalgameFile = os.path.join(os.path.dirname(__file__), 'azure_dark', 'assets', 'azure.svg')
imageDir = os.path.join(os.path.dirname(__file__), 'azure_dark', 'images')

def osSystem(cmd):
	'''smart system call'''
	rc = os.system(cmd)
	print('rc:', rc, cmd)
	return rc

def getImageNames():
	'''seek for image name pattern "$I(*)" in styleTclScript'''
	with open(styleTclScript) as f:
		return set(re.findall('[$]I\(([^\)]*)\)', f.read()))

def main():
	'''start the png image generation'''
	if not os.path.isdir(imageDir): os.makedirs(imageDir)
	for imgName in getImageNames():
		osSystem(
			inkscapeCmd + ' --file="{1}" --export-id="{0}" --export-png="{2}{0}.png"'.format(
				imgName,
				svgAmalgameFile,
				imageDir + os.sep
			)
		)

if '__main__' == __name__:
	main()

