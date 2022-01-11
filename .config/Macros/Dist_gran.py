from paraview.simple import *

paraview.simple._DisableFirstRenderCameraReset()

particulas_ = GetActiveSource()


renderView1 = GetActiveViewOrCreate('RenderView')
SetActiveSource(particulas_)
Hide(particulas_, renderView1)
nDist = int(input('Cantidad de tamaños de partículas: '))

for i in range(nDist):
    radius = float(input('radio particula: '))
    threshold1 = Threshold(Input=particulas_)
    threshold1.Scalars = ['POINTS', 'radius']
    threshold1.ThresholdRange = [0.98*radius, 1.02*radius]
    threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')
    threshold1Display.SetRepresentationType('Point Gaussian')
    threshold1Display.GaussianRadius = radius
    ColorBy(threshold1Display, ('POINTS', 'v', 'Magnitude'))

renderView1.CameraParallelProjection = 1

