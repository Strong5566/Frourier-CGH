from __future__ import division
import sys
from PIL import Image
# from numpy import *
from pyfftw.interfaces import numpy_fft
import numpy
import time

start = time.time()

level=200
cir=50

im = Image.open(sys.argv[1]).convert("L")
w, h=im.size
img1=numpy.double(numpy.array(im))
theta=numpy_fft.fftshift(img1)

# theta=theta/255
theta=theta/theta.max()
rand_the=numpy.random.rand(h,w)*2*numpy.pi*1j

kinoform=numpy.exp(rand_the)
for it in range(cir):
    kino_FT=numpy_fft.fft2(kinoform)
    ang_exp=numpy.exp(1j*numpy.angle(kino_FT))
    kino_FT=numpy.abs(kino_FT)
    # kino_iFT = numpy_fft.ifft2(kino_FT)
    g=kino_FT.sum()/theta.sum()
    correct=numpy.abs(2*g*theta)-kino_FT

    ang_exp=numpy.multiply(correct, ang_exp)
    FT=(numpy_fft.ifft2(ang_exp))
    ang_num=numpy.round((numpy.angle(FT)/2/numpy.pi)*level)
    kinoform=numpy.exp(1j*ang_num*2*numpy.pi/level)

CGH=((ang_num/level)*255).astype(numpy.uint8)

img2 = Image.fromstring("L", (CGH.shape[1], CGH.shape[0]), CGH.tostring())

img2.save(sys.argv[2])

end = time.time()
waste = start - end
print "waste "+str(waste)

kino_iFT=numpy_fft.ifft2(kinoform)
ikino=numpy_fft.fftshift(numpy.abs(numpy.power(kino_iFT, 2)))
ikino_num=ikino/ikino.max()

# print imgt
iCGH=(ikino_num*255).astype(numpy.uint8)
# iCGHe = iCGH.transpose(Image.FLIP_LEFT_RIGHT)
# print iCGH
# err = iCGH - imgt
# print err

# pn = ((imgt)**2).sum()/((iCGHe)**2).sum()
# rmse = ((imgt)**2 - pn*(iCGHe)**2).sum() / (768*1024)
# rmse = sqrt(rmse)
# print "mc100 is "+str(rmse)

img3 = Image.fromstring("L", (iCGH.shape[1], iCGH.shape[0]), iCGH.tostring())
img3.save(sys.argv[3])

