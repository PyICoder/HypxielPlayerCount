import PySimpleGUI as sg
from requests import get


def main():
    font_size = "20"
    form_rows = [[sg.Text(size=(5,1),font="Courier  " + font_size, key='text', justification="left")],
                 [sg.Button("Refresh", font="Courier 12")]]
    window = sg.Window('Hypixel Player Count', form_rows, auto_size_buttons=False, text_justification="center")
    key = sg.popup_get_text("Enter your api key")
    if key is None:
        exit()
    count = 0
    while True:
        count += 1
        print(count)
        button, values = window.read(timeout=10)
        if values is None:
            break
        if (count % 1000 == 0) or button == "Refresh" or count == 1:
            data = get(f"https://api.hypixel.net/playercount?key={key}").json()
            if data["success"] is False:
                cause = data["cause"]
                key = sg.popup_get_text(f"{cause} | Enter a correct api key")
                if key is None:
                    exit()
                continue
                # This is the code that reads and updates your window

            window['text'].update(data["playerCount"])
        else:
            continue

    window.close()


main()
