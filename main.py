import tkinter as tk
from tkinter import ttk
# from PIL import ImageTk

bgColor = "#3d6466"

ui = tk.Tk() # Initalize User Interface
ui.title("Hangman Game") # Setting Title Name of User Interface
xAxis = ui.winfo_screenwidth() // 2 # Getting X Axis of Screen
yAxis = int(ui.winfo_screenheight() * 0.1) # Getting Y Axis of Screen
ui.geometry('500x600+' + str(xAxis) + '+' + str(yAxis)) # User Interface Size

frame = tk.Frame(ui, width = 500, height = 600, bg = bgColor) # Initalize Frame
frame.grid(row = 0 ,column = 0) # Adding Frame
frame.pack_propagate(False)

# Adding an Image
# img = ImageTk.PhotoImage(file = "assets/Add File Name") 
# img_widget = tk.Label(frame, image = img, bg = bgColor)
# img_widget.image = img
# img_widget.pack()

tk.Label(frame, text = "Welcome To The Hangman Game", bg = bgColor, fg = "white").pack()

tk.Button(
        frame, 
        text = "Guess", 
        bg = bgColor, 
        fg = "white", 
        cursor = "hand2", 
        activebackground = "#badee2",
        activeforeground = "black").pack()

# Keeps the GUI running 
ui.mainloop()