import vtk

# read file
filename = "bun_zipper.ply"
reader = vtk.vtkPLYReader()
reader.SetFileName(filename)

# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# assign actor to the renderer
ren.AddActor(actor)
ren.SetBackground(0.2, 0.2, 0.5)
renWin.SetSize(750, 750) 

# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
