import os
import imageio

myfile = os.listdir('arsalan')
images = []
for i in range(len(myfile)):
    image = imageio.imread('arsalan/' + myfile[i])
    images.append(image)

imageio.mimsave('Arsalan.gif' , images)