from paraview.simple import *

Sources = paraview.simple.active_objects.get_selected_sources()
animationScene1 = GetAnimationScene()

for source in Sources:

	SetActiveSource(source)
	ExtendFileSeries(source)
	
animationScene1.GoToLast()
	
