import FreeSimpleGUI as Sg


def convert_to_meters(feet, inches):
    pass


label1 = Sg.Text("Enter a feet: ")
input1 = Sg.InputText(tooltip="Enter feet", key="feet")

label2 = Sg.Text("Enter inches: ")
input2 = Sg.InputText(tooltip="Enter inches", key="inches")

convert_button = Sg.Button("Convert")
exit_button = Sg.Button("Exit")
output_label = Sg.Text(key="output")

window = Sg.Window("Converter", layout=[[label1, input1], [label2, input2],
                                        [convert_button, output_label], [exit_button]])

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values['feet'])
                inches = float(values['inches'])
                result = convert_to_meters(feet, inches)
                window['output'].update(value=result, text_color='green')
            except ValueError:
                Sg.popup("Please insert a values for feet and inches")

        case 'Exit':
            break
        case Sg.WIN_CLOSED:
            break

window.close()