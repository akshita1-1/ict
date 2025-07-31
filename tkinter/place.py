import tkinter as tk 

root = tk.Tk()
root.geometry("500x200")

label1 =tk.Label(root, text='Label 1',bg="pink")
label1.place(x=50 , y=50)

label2 =tk.Label(root, text='Label 2',bg="purple")
label2.place(x=150 , y=150)



root.mainloop()