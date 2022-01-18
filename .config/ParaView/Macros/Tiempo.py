# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

scale = float(input('scale'))

# find source
particulas_ = FindSource('particulas_*')

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(Input=particulas_)

# Properties modified on annotateTimeFilter1
annotateTimeFilter1.Format = 'Tiempo: {time:.2f} [s]'
annotateTimeFilter1.Scale = scale
annotateTimeFilter1.Shift = scale

renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1)

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.WindowLocation = 'Upper Right Corner'

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontSize = 23

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.Color = [0.0, 0.0, 0.0]
