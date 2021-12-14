
from PIL import Image
import time


def mandel(inputXmin,inputXmax,inputYmin,inputYmax,img):

        xa = -1
        xb = 2
        ya = -1.5
        yb = 1.5
        
        # max iterations allowed
        #maxIt = 1024
        maxIt = 100
        
        # image size
        
        imgx =1000
        imgy = 1000
        image = Image.new("RGB", (imgx, imgy))
        for y in range(inputYmin,inputYmax):
            zy = y * (yb - ya) / (imgy - 1)  + ya
            for x in range(inputXmin,inputXmax):
                zx = x * (xb - xa) / (imgx - 1)  + xa
              
                z = zx + zy * 1j
              
                c = z
                for i in range(maxIt):
                    if abs(z) > 2.0: break
                    z = z * z + c
                image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
        image.save(img + '.png')

start = time.perf_counter()

#sequential execute the Mandelbrot function

mandel(0,500,0,500,'image1')
mandel(0,500,501,1000,'image2')
mandel(501,1000,0,500,'image3')
mandel(501,1000,501,1000,'image4')

finish = time.perf_counter()

print("Time taken in seconds",{round(finish-start,2)})