import tkinter as tk
from tkinter import PhotoImage 
root=tk.Tk()
icon = tk.PhotoImage(file="C:\\Users\\Akshita\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-10-23 175713.png")
root.iconphoto(True,icon)
root.geometry("500x200")

root.mainloop()