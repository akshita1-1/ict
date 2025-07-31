import tkinter as tk
def on_button_click():
    label.config(text="Button Clicked")
    
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x300")

label = tk.Label(root,text="Hello , Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me" , command= on_button_click)
button.pack(pady=20)

root.mainloop()