#### import the simple module from the paraview
from paraview.simple import *
import os

name=input('nombre del archivo')
cwd = os.getcwd()
path = os.path.join(cwd, 'screenshots')

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
SaveScreenshot('./screenshots/'+name+'.jpg', renderView1, ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts',
    OverrideColorPalette='WhiteBackground', 
    # JPEG options
    Progressive=0)