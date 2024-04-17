import PySimpleGUI as sg

label1 = sg.Text("Enter feet")
label2 = sg.Text("Enter inches")

text_input_feet = sg.Input()
text_input_inches = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor", [[label1, text_input_feet],
                                 [label2, text_input_inches],
                                 [button]])

window.read()
window.close()