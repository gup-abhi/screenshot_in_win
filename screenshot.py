# importing tkinter
import tkinter as tk
# importing pyautogui
import pyautogui

# creating a window
win = tk.Tk()
# giving title to the window
win.title("Take Screenshot")
# specifying the szie of the window
win.geometry("150x50")

# creating function to get the screenshot of the screen
def takescreenshot():
    # claaing screenshot function from pyautogui to take screenshot and store it in a variable
    screenshot = pyautogui.screenshot()
    # saving the screenshot with the following name
    screenshot.save('screenshot.png')

# creating button to take screenshot by calling our function
button = tk.Button(win, text = 'Capture Screenshot', command = takescreenshot)
button.grid(row = 2, column = 2, padx = 10, pady = 10)

# creating window loop
win.mainloop()