import FreeSimpleGUI as Sg


label1 = Sg.Text("Enter a feet: ")
input1 = Sg.InputText(tooltip="Enter feet", key="feet")

label2 = Sg.Text("Enter inches: ")
input2 = Sg.InputText(tooltip="Enter inches", key="inches")

convert_button = Sg.Button("Convert")
exit_button = Sg.Button("Exit")
output_label = Sg.Text(key="output")