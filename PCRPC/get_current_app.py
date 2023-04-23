import psutil
import win32process
import win32gui

def GCAR():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    app = psutil.Process(pid[-1]).name()
    app = app.replace(".exe", "")
    app = app.capitalize()
    if app == "Code":
        app = "Visual Studio Code"
    
    return app
