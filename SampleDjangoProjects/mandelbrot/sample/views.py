from django.db.models.fields import NullBooleanField
from django.shortcuts import render

from .models import Sample
from PIL import Image
import multiprocessing
import mandelbrot
import time


# Create your views here.
#app = Flask(__name__)

def show_mandebrot_image(request):
    input_data = Sample.objects.get(id=2)
    start = time.perf_counter()


    p1=multiprocessing.Process(target=creteMandelbrotImage,
               args=[input_data.Minimumreal,input_data.Minimumimag,input_data.Maximumreal,
                     input_data.Maximumimag,input_data.MaxInteration,input_data.xaxis,input_data.yaxis,0,5000,0,5000,'image1'])    

    p2=multiprocessing.Process(target=creteMandelbrotImage,
                    args=[input_data.Minimumreal,input_data.Minimumimag,input_data.Maximumreal,
                     input_data.Maximumimag,input_data.MaxInteration,input_data.xaxis,input_data.yaxis,0,5000,5001,10000,'image2'])

    p3=multiprocessing.Process(target=creteMandelbrotImage,
                     args=[input_data.Minimumreal,input_data.Minimumimag,input_data.Maximumreal,
                     input_data.Maximumimag,input_data.MaxInteration,input_data.xaxis,input_data.yaxis,5001,10000,0,5000,'image3'])

    p4=multiprocessing.Process(target=creteMandelbrotImage,
                    args=[input_data.Minimumreal,input_data.Minimumimag,input_data.Maximumreal,
                     input_data.Maximumimag,input_data.MaxInteration,input_data.xaxis,input_data.yaxis,5001,10000,5001,10000,'image4'])


    if __name__ == '__main__':
        print('in the main')

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()



    finish = time.perf_counter()

    print("Time taken in seconds",{round(finish-start,2)})

    if finish:
        context = {
        'output_data' : finish
    }
        return render(request,"sample/index.html",context)

def creteMandelbrotImage(min_c_re,min_c_im,max_c_re,max_c_im,max_n,xaxis,yaxis,inputXmin,inputXmax,inputYmin,inputYmax,img):
    # drawing area

    xa = min_c_re
    xb = max_c_re
    ya = min_c_im
    yb = max_c_im
    
    # max iterations allowed
    maxIt = max_n
        
    # image size
   
    imgx = xaxis
    imgy = yaxis

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

