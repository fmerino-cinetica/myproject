
from paraview.simple import *
#paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# create a new 'Text'
text1 = Text(registrationName='Text1')

text1.Text = """SDM Mineral Radomiro Tomic
Cuchara de Muestreo - Vista Lateral - 12800 TPH
TecProMin S.A. - CINETICA Ingeniería
"""

# show data in view
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')



# Properties modified on text1Display
text1Display.WindowLocation = 'LowerLeftCorner'

# Properties modified on text1Display
text1Display.Color = [0.0, 0.0, 0.0]
text1Display.FontSize = 22

renderView1.Update()

