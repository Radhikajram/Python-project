
from PIL import Image
import multiprocessing
import time

#Initial the input variable



def mandel(min_c_re,min_c_im,max_c_re,max_c_im,max_n,xaxis,yaxis,inputXmin,inputXmax,inputYmin,inputYmax,img):


        xa = min_c_re
        xb = max_c_re
        ya = min_c_im
        yb = max_c_im
        
        # max iterations allowed

        maxIt =  max_n
        
      
        # image size
        imgx = xaxis
        imgy = yaxis


        #Create Image
        image = Image.new("RGB", (imgx, imgy))

        #loop the actual pixel range with x and y axis

        for y in range(inputYmin,inputYmax):
            zy = y * (yb - ya) / (imgy - 1)  + ya
            for x in range(inputXmin,inputXmax):
                zx = x * (xb - xa) / (imgx - 1)  + xa
              
                # covert to complex number by multiplying it wih 1j (a+bi)
                z = zx + zy * 1j
                c = z
                
                for i in range(maxIt):

                    # if the resultant value reached the range greater than 2(Not Mandelbrot).
                    if abs(z) > 2.0: break
                    z = z * z + c
                    image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

        #save the portion of subpicture through parallel processing
        image.save(img + '.png')
        
#
# mandelbort function gets invoked through multiprocessing.

if __name__ == '__main__':

        #get the input datas from console
        min_c_re = float(input("Enter minimum range of real  numbers:\n"))
        min_c_im = float(input("Enter minimum range of imaginary  numbers:\n"))
        max_c_re = float(input("Enter maximum range of real  numbers:\n"))
        max_c_im = float(input("Enter maximum range of imaginary  numbers:\n"))
        max_n = int(input("Enter maximum limit of number to generate the Mandelbrot:\n"))
        xaxis = int(input("Enter pixel range of the picture for x-axis:\n"))
        yaxis = int(input("Enter pixel range of the picture for y-axis:\n"))


        exitValue = input("Enter 'quit' to stop the input process\n")

        p1=multiprocessing.Process(target=mandel,args=[min_c_re,min_c_im,max_c_re,max_c_im,max_n,xaxis,yaxis,0,5000,0,5000,'image5'])
        p2=multiprocessing.Process(target=mandel,args=[min_c_re,min_c_im,max_c_re,max_c_im,max_n,xaxis,yaxis,0,5000,5001,10000,'image6'])
        p3=multiprocessing.Process(target=mandel,args=[min_c_re,min_c_im,max_c_re,max_c_im,max_n,xaxis,yaxis,5001,10000,0,5000,'image7'])
        p4=multiprocessing.Process(target=mandel,args=[min_c_re,min_c_im,max_c_re,max_c_im,max_n,xaxis,yaxis,5001,10000,5001,10000,'image8'])


        if(exitValue=='quit'):
            print("start timer for processing")

            start = time.perf_counter()

            # start the multiprocessing-

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

