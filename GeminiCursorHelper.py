import tkinter as tk
import pystray
from PIL import Image, ImageDraw
import threading
import speech_recognition as sr
import google.generativeai as genai

genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-2.0-flash')

def recognize_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en-US')
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            return "I couldn't understand what you said."
        except sr.RequestError:
            return "Voice recognition service is unavailable."

def show_window():
    def send():
        user_input = entry.get()
        respuesta = model.generate_content(user_input).text
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, respuesta)

    def talk():
        text_talk= recognize_voice()
        entry.delete(0, tk.END)
        entry.insert(0, text_talk)
        send()

    window = tk.Tk()
    window.title("Chat Gemini AI")
    window.geometry("400x300")

    entry = tk.Entry(window, width=40)
    entry.pack(pady=10)

    btn_send = tk.Button(window, text="Send", command=send)
    btn_send.pack()

    btn_talk = tk.Button(window, text="Talk", command=talk)
    btn_talk.pack()

    output_text = tk.Text(window, wrap=tk.WORD)
    output_text.pack(pady=10, expand=True, fill='both')

    window.mainloop()

def create_icon():
    def open(_=None):
        threading.Thread(target=show_window).start()

    def exit(_=None):
        icon.stop()

    image = Image.new('RGB', (64, 64), "black")
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill="cyan")

    icon = pystray.Icon("gemini_chat", image, menu=pystray.Menu(
        pystray.MenuItem("Open Chat", open),
        pystray.MenuItem("Exit", exit)
    ))
    icon.run()

threading.Thread(target=create_icon).start()
