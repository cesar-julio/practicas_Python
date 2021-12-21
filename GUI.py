from typing import Text
import PySimpleGUI as sg

sg.theme("Dark")

layout = [[sg.Text('Calcular la Furza', key="T",)],
            [sg.Multiline(size=(13,15), no_scrollbar=True,pad=((5,0),(5,5)),disabled=True, key="_IND_"),sg.Multiline(size=(60,15),pad=((0,5),(5,5)) ,key="MUL")],
            [sg.Button("Tomar texto"), sg.Button("Ejecutar")],
]

lista_linas = []
idx = 0

window = sg.Window("Calculadora de mecánica", layout)
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    if "Ejecutar" in event:
        lista_linas.append("Velocidad:\n")
        window["T"].update(window["MUL"].get())
        window["_IND_"].update(lista_linas[idx])
        idx =idx + 1
window.close()