# trace generated using paraview version 5.9.0-RC3

#### import the simple module from the paraview
from paraview.simple import *
import math as m
# find source
source = GetActiveSource()
renderView1 = GetActiveViewOrCreate('RenderView')


angulo = float(input('Angulo: '))
ang_rad = m.radians(angulo)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=source)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'id']
clip1.Value = 270483.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-1.780555009841919, -2.0490181148052216, 0.18009495735168457]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [-1.780555009841919, -2.0490181148052216, 0.18009495735168457]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [m.cos(ang_rad), m.sin(ang_rad), 0.0]

Hide(source, renderView1)
Show3DWidgets(proxy=clip1.ClipType)
clip1.Invert = 0
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')
