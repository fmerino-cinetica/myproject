from paraview.simple import *

mallas = paraview.simple.active_objects.get_selected_sources()
opacity = 0.2#float(input('opacidad'))

for malla in mallas:

	SetActiveSource(malla)
	renderView1 = GetActiveViewOrCreate('RenderView')
	layout1 = GetLayout()
	mallaDisplay = GetDisplayProperties(malla, view=renderView1)
	ColorBy(mallaDisplay, None)

	sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')
#	sTLSolidLabelingPWF = GetOpacityTransferFunction('STLSolidLabeling')

	HideScalarBarIfNotNeeded(sTLSolidLabelingLUT, renderView1)
	mallaDisplay.Opacity = opacity
	
renderView1.CameraParallelProjection = 1
