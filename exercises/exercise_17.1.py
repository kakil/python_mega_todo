import PySimpleGUI as sg

enter_feet_label = sg.Text("Enter feet: ")
enter_inches_label = sg.Text("Enter inches")
feet_input = sg.Input(key="feet")
inches_input = sg.Input(key="inches")
convert_button = sg.Button("Convert")
answer_label = sg.Text(key="answer", text_color="white")

window = sg.Window("Converter", layout=[[enter_feet_label, feet_input],
                                        [enter_inches_label, inches_input],
                                        [convert_button, answer_label]],
                                            font=('Helvetica', 24))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            print(f"Feet: {feet}, Inches: {inches}")

            feet_to_inches = feet * 12
            total_inches = feet_to_inches + inches
            meters = str(total_inches * 0.0254)
            window["answer"].update(value=meters)
        case sg.WIN_CLOSED:
            exit()