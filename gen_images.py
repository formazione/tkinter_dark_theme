

import os
import re

svgAmalgameFile = os.path.join(os.path.dirname(__file__), 'azure dark', 'assets', 'azure.svg')
styleTclScript = os.path.join(os.path.dirname(__file__), 'azure dark', 'azure dark.tcl')
imageDir = os.path.join(os.path.dirname(__file__), 'azure dark', 'images')

def osSystem(cmd):
	rc = os.system(cmd)
	print('rc:', rc, cmd)
	return rc

def getImageNames():
	with open(styleTclScript) as f:
		return set(re.findall('[$]I\(([^\)]*)\)', f.read()))

def main(inkscapeCmd = 'inkscape'):
	if not os.path.isdir(imageDir): os.makedirs(imageDir)
	for imgName in getImageNames():
		osSystem(inkscapeCmd + ' --file="{1}" --export-id="{0}" --export-png="{2}{0}.png"'.format(imgName, svgAmalgameFile, imageDir + os.sep))

if '__main__' == __name__:
	main()

