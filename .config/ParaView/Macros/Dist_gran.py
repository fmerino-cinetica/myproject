from paraview.simple import *

import numpy as np

gran = np.genfromtxt('granulometria.liggghts', dtype=None, encoding="utf-8", delimiter='\t', skip_header=1, usecols=(1, 3))
radios = [gran[2][1], gran[4][1], gran[6][1]]

paraview.simple._DisableFirstRenderCameraReset()

particulas_ = GetActiveSource()

renderView1 = GetActiveViewOrCreate('RenderView')
SetActiveSource(particulas_)
Hide(particulas_, renderView1)

for i in radios:
    threshold1 = Threshold(registrationName='Threshold1', Input=particulas_)
    threshold1.Scalars = ['POINTS', 'radius']
    threshold1.LowerThreshold = 0.98*i/2000
    threshold1.UpperThreshold = 1.02*i/2000
    threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')
    threshold1Display.SetRepresentationType('Point Gaussian')
    threshold1Display.GaussianRadius = i/2000
    ColorBy(threshold1Display, ('POINTS', 'v', 'Magnitude'))

renderView1.CameraParallelProjection = 1

