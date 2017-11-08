# requirements
# * mogrify
# * PIL
	
import subprocess
import re
import pathlib
import os
from PIL import Image

path = "/home/ssamtsu/ssamtsu_django/media/classified/"
types = "JPG|PNG|JPEG"	# IGNORECASE
convert_to = 768
minimum_height = 768	# if greater than this value -> convert

os.chdir(path)
dir = pathlib.Path()
for file in dir.iterdir():
    print(file)
    if bool(re.findall(types+"$", str(file), re.IGNORECASE)):
        im = Image.open(str(dir.cwd()) + '/' + str(file))
        height = im.size[1]

        if height > minimum_height:
            sp = subprocess.Popen( "mogrify -resize x" + convert_to + " " + str(file), stdin=subprocess.PIPE, shell=True )
            sp.communicate(b"input data\n")
