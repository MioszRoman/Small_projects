import FreeSimpleGUI as Sg


label1 = Sg.Text("Choose a file/files to compress: ")
label2 = Sg.Text("Choose a place where you want to save it: ")

input_text1 = Sg.Input()
input_text2 = Sg.Input()


window = Sg.Window('Compressor', layout=[[label1, input_text1],[label2, input_text2]])

window.read()