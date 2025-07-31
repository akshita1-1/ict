import tkinter as tk 

root = tk.Tk()
root.geometry("500x200")

label1 =tk.Label(root, text='Label 1',bg="pink")
label1.grid(row=0 , column=0)

label2 =tk.Label(root, text='Label 2',bg="purple")
label2.grid(row=1 , column=1)



root.mainloop()