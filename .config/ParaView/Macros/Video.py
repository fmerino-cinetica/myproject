#### import the simple module from the paraview
from paraview.simple import *
import os

name=input('nombre del archivo')
cwd = os.getcwd()
path = os.path.join(cwd, 'videos')
tini=int(input('ingresar frame inicial'))
tend=int(input('ingresar frame final'))

try:
    os.mkdir(path)
except:
    pass

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1420, 794]

# get layout
layout1 = GetLayout()

# save screenshot
SaveAnimation('./videos/'+name+'.png', renderView1, ImageResolution=[1920, 1080],
    OverrideColorPalette='WhiteBackground',
    FontScaling='Do not scale fonts',
    FrameWindow=[tini, tend], 
    # PNG options
    CompressionLevel='0')
