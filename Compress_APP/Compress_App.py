import FreeSimpleGUI as Sg
import zipfile, pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)




label1 = Sg.Text("Choose a file/files to compress: ")
label2 = Sg.Text("Choose a place where you want to save it: ")

input_text1 = Sg.Input()
input_text2 = Sg.Input()

choose_button1 = Sg.FilesBrowse('Choose', key='files')
choose_button2 = Sg.FolderBrowse('Choose', key='folder')

compress_button = Sg.Button('Compress')
output_label = Sg.Text(key='output')


window = Sg.Window('Compressor', layout=[[label1, input_text1, choose_button1],
                                         [label2, input_text2, choose_button2],
                                         [compress_button, output_label]])

while True:
    events, values = window.read()
    filepaths = values['files'].split(';')
    folder = values['folder']
    match events:
        case 'Compress':
            make_archive(filepaths, folder)
            window['output'].update(value='Compression completed!')
        case Sg.WIN_CLOSED:
            break