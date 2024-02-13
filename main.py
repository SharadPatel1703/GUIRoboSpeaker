import tkinter as tk
import pyttsx3 as pytxt

def on_speak_button_click():
    speech = entry.get()
    engine.say(speech)
    engine.runAndWait()


window = tk.Tk()
window.title("Robotic Speaker 1.1 - Sharad Patel")

window.configure(background='lightgreen')

label = tk.Label(window, text="Write below your text to make it speak")
label.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(pady=10)

speak_button = tk.Button(window, text="Speak", command=on_speak_button_click)
speak_button.pack(pady=10)

engine = pytxt.init()

window.mainloop()
