pyinstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --icon=favicon.ico Jarvis.py
copy *.jarvis \dist\Jarvis\
copy *.py \dist\Jarvis\