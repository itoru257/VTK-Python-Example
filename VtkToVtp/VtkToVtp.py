import vtk

# read file
input_filename = "input.vtk"
reader = vtk.vtkPolyDataReader()
reader.SetFileName( input_filename )

# write file
output_filename = "output.vtp"
writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName( output_filename )
writer.SetInputConnection( reader.GetOutputPort() )
writer.SetDataModeToAscii()
writer.Write()
