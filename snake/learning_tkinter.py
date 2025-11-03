# Learning Tkinter
import tkinter as tk

root = tk.Tk()
root.title("My first tkinter app")
root.geometry("1000x500")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

def button_clicked():
    label.config(text=f'Button was clicked!')


# Clickable button
button = tk.Button(root, text='Click Me', command=button_clicked)
button.pack(pady=10)

# Additional labels
label1 = tk.Label(root, text="Row 0, Column 0")
label1.pack(pady=5)

label2 = tk.Label(root, text="Row 0, Column 1")
label2.pack(pady=5)

root.mainloop()

