import PySimpleGUI as sg
import zip_extractor as ze

sg.theme("Black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination directory: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

layout=[[label1, input1, choose_button1],
        [label2, input2, choose_button2],
        [extract_button, output_label]]

window = sg.Window("Archive Extractor",
                   layout=layout,
                   font=("Helvetica", 24))

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values['archive']
    dest_dir = values['folder']

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Extract":
        ze.extract_archive(archivepath, dest_dir)
        window['output'].update(value="File extraction complete")


window.close()