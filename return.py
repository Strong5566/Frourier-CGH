#IDFT image

from __future__ import division
import sys
from PIL import Image
import numpy
from pyfftw.interfaces import numpy_fft
#import numpy.fft as numpy_fft
import time

height = 768
width = 1024
PX,PY = 19e-6, 19e-6
WL = 532e-9
z = 0.4
# f = file("the.txt", 'w')
im=Image.open(sys.argv[1]).convert("L")
theta=numpy.double(numpy.array(im))
# for i in theta:
	# f.write(str(i)+"\n")
# print theta.max()
# f.close
# f = file("the_as.txt", 'w')

theta=numpy.array(im).astype(numpy.int8).astype(numpy.float64)


# for i in theta:
	# f.write(str(i)+"\n")

# print len(theta)

# print i
# theta=numpy.double(theta)

# theta=numpy_fft.fftshift(theta)

# print theta.max()
# print theta.min()
theta=theta/255.0

# print theta
kinoform=numpy.exp(1j*theta*2*numpy.pi)
# print kinoform
# for j in range(len(kinoform)):
	# for i in range(len(kinoform[j])):
		# kinoform[j][i] = kinoform[j][i]*numpy.exp(1j*((PX*(i - width/2))**2+(PY*(j - height/2))**2)*numpy.pi/WL/z)


# for i in kinoform:
	# f.write(str(i)+"\n")


kfFT=numpy_fft.ifft2(kinoform)

#print kfFT
kfFT=numpy_fft.fftshift(numpy.abs(numpy.power(kfFT, 2)))
kfFT=kfFT/kfFT.max()
# print kfFT.min()

o2=(kfFT*255).astype(numpy.uint8)
# o2 = 255 - o2
# print o2.min()
# for i in o2:
	# for j in i:
		# if j > 50:
			# print j
	# f.write(str(i)+"\n")
om2 = Image.fromstring("L", (o2.shape[1], o2.shape[0]), o2.tostring())

om2.save(sys.argv[2])
# f.close()