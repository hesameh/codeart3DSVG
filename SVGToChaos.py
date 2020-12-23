import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure(figsize=(7.04,7.04), dpi=100)
ax = fig.gca(projection='3d', proj_type = 'ortho')

from svgpathtools import svg2paths,disvg
paths, attributes = svg2paths('flo.svg')


x=[]
y=[]
z=[]
for k, v in enumerate(paths):
#    print(k, v)
    for dd in enumerate(v):
        x=[]
        y=[]
        z=[]
        x.append(dd[1].start.real)
        y.append(dd[1].start.imag)
        z.append(np.random.rand()*1000)
        x.append(dd[1].end.real)
        y.append(dd[1].end.imag)
        z.append(np.random.rand()*1000)
         
        print(dd[1].start.real,dd[1].start.imag,dd[1].end.real,dd[1].end.imag)
        ax.plot(x,y,z)
        
Fignum=0

plt.axis('off')
for angle in range(270, 360):
    ax.view_init(30, angle)
    
    plt.draw()
    plt.pause(.001)
    filename = 'TL\\chao%03d.png'%(Fignum,)
    fig.savefig(filename, dpi=fig.dpi)
    Fignum+=1

for angle in range(30,91):
    ax.view_init(angle,0)
    plt.draw()
    plt.pause(.001)        
    filename = 'TL\\chao%03d.png'%(Fignum,)
    fig.savefig(filename, dpi=fig.dpi)
    Fignum+=1    

for angle in range(30,91):
    ax.view_init(90,0)
    plt.draw()
    plt.pause(.001)        
    filename = 'TL\\chao%03d.png'%(Fignum,)
    fig.savefig(filename, dpi=fig.dpi)
    Fignum+=1        
	

## Make video from png files
import os
import imageio

png_dir = 'TL/'
images = []
for file_name in os.listdir(png_dir):
    print(file_name)
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('movie10.mp4',images, fps=20)	