import tkinter as tk
import pystray
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import io
import threading
import speech_recognition as sr
import google.generativeai as genai
import pyautogui
import re

# Gemini config
genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-2.5-flash')

# Icon creation
image = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

cx, cy = 32 // 2, 32 // 2
radius = 32 * 0.45

points = [
    (cx, cy - radius),
    (cx + radius, cy),
    (cx, cy + radius),
    (cx - radius, cy),
]

center_color = (100, 180, 255, 255)
edge_color = (170, 130, 255, 255)

for i in range(20, 0, -1):
    r = radius * (i / 20)
    alpha = int(255 * (i / 20))
    color = (
        int(center_color[0] * (i / 20) + edge_color[0] * (1 - i / 20)),
        int(center_color[1] * (i / 20) + edge_color[1] * (1 - i / 20)),
        int(center_color[2] * (i / 20) + edge_color[2] * (1 - i / 20)),
        alpha
    )

    draw.polygon([
        (cx, cy - r),
        (cx + r, cy),
        (cx, cy + r),
        (cx - r, cy),
    ], fill=color)

# GUI build
def show_window():
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
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, "I couldn't understand what you said.")
                return ""
            except sr.RequestError:
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, "Voice recognition service is unavailable.")
                return ""

    def send():
        user_input = entry.get()

        screenshot = ImageGrab.grab()
        buffer = io.BytesIO()
        screenshot.save(buffer, format='PNG')
        image_bytes = buffer.getvalue()

        response = model.generate_content([
        {"text": "The image represents my current Desktop, which has a resolution of " + str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()) + ", please analyze the image and provide only the correct coordenates where the cursor should be placed in this format (XxY) in order to fulfill the following request: " + user_input},
            {
                "inline_data": {
                    "mime_type": "image/png",
                    "data": image_bytes
                }
            }
        ])

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, response.text)

        pattern = r'^\d+x\d+$'
        if (bool(re.match(pattern, response.text))):
            pyautogui.moveTo(int(response.text.split("x")[0]), int(response.text.split("x")[1]), duration=0.5)
            if (var_check):
                pyautogui.doubleClick()

    def talk():
        text_talk= recognize_voice()
        entry.delete(0, tk.END)
        entry.insert(0, text_talk)
        if (text_talk != ""):
            send()

    window = tk.Tk()
    window.iconphoto(False, ImageTk.PhotoImage(image))
    window.title("Gemini Cursor Helper")
    window.geometry("600x150")
    window.resizable(False, False)

    frame_superior = tk.Frame(window, padx=10, pady=10)
    frame_superior.pack(fill=tk.X)

    entry = tk.Entry(frame_superior, width=40)
    entry.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill=tk.X)

    btn_send = tk.Button(frame_superior, text="Send", width=10, command=send)
    btn_send.pack(side=tk.LEFT, padx=(0, 5))

    btn_talk = tk.Button(frame_superior, text="Talk", width=10, command=talk)
    btn_talk.pack(side=tk.LEFT)

    frame_checkbox = tk.Frame(window, padx=10)
    frame_checkbox.pack(fill=tk.X)

    var_check = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame_checkbox, text="Let Gemini try to open the program automatically", variable=var_check)
    checkbox.pack(anchor='w')

    output_text = tk.Text(window, wrap=tk.WORD, height=10, padx=10, pady=10)
    output_text.pack(fill=tk.BOTH, expand=True)

    window.mainloop()

# System Tray Icon Creation
def create_icon():
    def open(_=None):
        threading.Thread(target=show_window).start()

    def exit(_=None):
        icon.stop()

    icon = pystray.Icon("gemini_chat", image, menu=pystray.Menu(
        pystray.MenuItem("Open Chat", open),
        pystray.MenuItem("Exit", exit)
    ))
    icon.run()

threading.Thread(target=create_icon).start()
