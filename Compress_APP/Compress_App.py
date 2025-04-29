import FreeSimpleGUI as Sg


label1 = Sg.Text("Choose a file/files to compress: ")
label2 = Sg.Text("Choose a place where you want to save it: ")

input_text1 = Sg.Input()
input_text2 = Sg.Input()

choose_button1 = Sg.FilesBrowse('Choose', key='files')
choose_button2 = Sg.FolderBrowse('Choose', key='folder')

compress_button = Sg.Button('Compress')


window = Sg.Window('Compressor', layout=[[label1, input_text1, choose_button1],
                                         [label2, input_text2, choose_button2],
                                         [compress_button]])

window.read()