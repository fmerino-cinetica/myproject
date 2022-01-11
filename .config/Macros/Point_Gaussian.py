#### import the simple module from the paraview
from paraview.simple import *
import numpy as np

radio = float(input('radio'))
maxV = 10 #float(input('maxV'))
ndiv = 5 #float(input('nDiv'))

#Cambiar partículas a Point Gaussian

particulas_ = GetActiveSource()

renderView1 = GetActiveViewOrCreate('RenderView')
layout1 = GetLayout()
particulas_Display = GetDisplayProperties(particulas_, view=renderView1)
particulas_Display.SetRepresentationType('Point Gaussian')
particulas_Display.GaussianRadius = radio

#Cambiar color de leyenda a Rainbow Uniform
ColorBy(particulas_Display, ('POINTS', 'v', 'Magnitude'))
particulas_Display.RescaleTransferFunctionToDataRange(True, False)
particulas_Display.SetScalarBarVisibility(renderView1, True)
vLUT = GetColorTransferFunction('v')

vLUT.ApplyPreset('Blue to Red Rainbow', True)

#Ajustar Leyenda
vLUTColorBar = GetScalarBar(vLUT, renderView1)
vLUTColorBar.AutoOrient = 0
vLUTColorBar.WindowLocation = 'AnyLocation'
vLUTColorBar.AutomaticLabelFormat = 0
vLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
vLUTColorBar.TitleFontSize = 12
vLUTColorBar.LabelFontSize = 12
vLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
vLUTColorBar.LabelFormat = '%-#6.1f'
vLUTColorBar.RangeLabelFormat = '%-#6.1f'
vLUTColorBar.Position = [0.035, 0.58]
vLUTColorBar.HorizontalTitle = 1
vLUTColorBar.Title = 'Velocidad [m/s]'
vLUTColorBar.ComponentTitle = ''
vLUTColorBar.CustomLabels = np.linspace(0, maxV, ndiv)	
vLUTColorBar.ScalarBarLength = 0.35
vLUT.RescaleTransferFunction(0.0, maxV)


renderView1.CameraParallelProjection = 1
