import tkinter as tk 

root = tk.Tk()
root.title("Simple GUI with Frames")
root.geometry("300x300")

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP,pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM,pady=10)

label = tk.Label(top_frame,text= "Hello ,Tkinter with Framed!")
label.pack()

button=tk.Button(bottom_frame,text="Click Me",command=lambda:label.config(text="Button Clicked!"))
button.pack()

root.mainloop()