import tkinter as tk

# Function to convert Fahrenheit to Celsius
def convert():
    try:
        fahrenheit = float(entry.get())  # Get value from entry
        celsius = (fahrenheit - 32) * 5 / 9
        label_result.config(text=f"{fahrenheit:.2f} °F  =  {celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Please enter a valid number")

root = tk.Tk()
root.geometry('600x400')
root.title("Fahrenheit to Celsius Converter")

# Label
label1 = tk.Label(text='Enter Fahrenheit:', background='skyblue')
label1.place(x=10, y=10)

# Entry for input
entry = tk.Entry(width=20)
entry.place(x=10, y=50)

# Button to convert
button = tk.Button(text='Convert', command=convert)
button.place(x=200, y=47)

# Label to display result
label_result = tk.Label(text='Result', font=('Arial', 12))
label_result.place(x=10, y=100)

root.mainloop()
