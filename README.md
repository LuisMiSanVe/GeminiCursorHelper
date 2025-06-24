> [See in spanish/Ver en español](https://github.com/LuisMiSanVe/GeminiCursorHelper/blob/main/README.es.md)
# 🖱️ Gemini Cursor Helper
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![image](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://aistudio.google.com/app/apikey)

AI Assistant that helps you localize and open programs using text input or voice.

## 📝 Technology Explanation
The program makes a screenshot of your current screen and sends it to Gemini with a [prompt](https://github.com/LuisMiSanVe/GeminiCursorHelper/blob/main/GeminiCursorHelper.py#L78) for it to identify the location of your request and (if checked) try to open it.

It is recommended to use the program with a plain background, where the program icons can be seen easily.

Currently, it uses `Gemini Flash 2.5`, the most recent and advanced version of the model, even so, it will often make mistakes, hopefully it gets sharper in newer versions.

> [!IMPORTANT]
> Be aware that Gemini AI doesn't actually know the programs installed in your device and can make mistakes, so enable the *checkbox* to let Gemini try to open only if you make sure nothing unexpected can happen.

## 📋 Prerequisites
You'll need two things to use this program: Gemini API KEY and the required Python libraries installed.

Obtain your Gemini API Key by visiting [Google AI Studio](https://aistudio.google.com/app/apikey). Ensure you are logged into your Google account, then press the blue button that says 'Create API key' and follow the steps to set up your Google Cloud Project and retrieve your API key. **Make sure to save it in a safe place**.  
Google allows free use of this API without adding billing information, but there are some limitations.

In Google AI Studio, you can monitor the AI's usage by clicking 'View usage data' in the 'Plan' column where your projects are displayed. I recommend monitoring the 'Quota and system limits' tab and sorting by 'actual usage percentage,' as it provides further more detailed information.

Then, download or clone the Python script and run this command on the same folder:
```
python pip install pystray pillow speechrecognition google-generativeai pyaudio pyautogui
```
Or if it fails or you have a different Python version:
```
py -m pip install pystray pillow speechrecognition google-generativeai pyaudio pyautogui
```

## 💻 Technologies Used
- Programming Language: [Python](https://www.python.org/)
- Libraries:
  - [tkinter](https://docs.python.org/es/3.13/library/tkinter.html)
  - [pystray](https://pypi.org/project/pystray/)
  - [PIL](https://pypi.org/project/pillow/)
  - [io](https://docs.python.org/3/library/io.html)
  - [threading](https://docs.python.org/3/library/threading.html)
  - [speech_recognition](https://pypi.org/project/SpeechRecognition/)
  - [google.generativeai](https://pypi.org/project/google-generativeai/)
  - [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
  - [re](https://docs.python.org/es/3.13/library/re.html)
- Other:
  - [Gemini API Key](https://aistudio.google.com/app/apikey)
- Recommended IDE: [VS Code](https://code.visualstudio.com/)
