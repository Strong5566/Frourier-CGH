from __future__ import division
import sys
from PIL import Image
# from numpy import *
from pyfftw.interfaces import numpy_fft
import numpy as np
import itertools as itt

im = Image.open(sys.argv[1]).convert("L")
img=np.array(im).astype(np.uint8)
w, h=im.size
newarray = np.zeros((h,w))
# newarray = np.zeros((h,w/2))
# w2 = int(w/2 - w%2)

for i in range(h):
	for j in range(w):
		# newarray[i][j] = img[i][j*2]
		ww = j/2
		hh = i/2
		newarray[i][j] = img[hh][ww]
		
newarray = newarray.astype(np.uint8)
outimg = Image.fromstring("L", (newarray.shape[1], newarray.shape[0]), newarray.tostring())
outimg.save(sys.argv[2])

