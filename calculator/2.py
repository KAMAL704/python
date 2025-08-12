import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("400x500")
root.resizable(0, 0)

# Entry widget
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

# Button layout
btns = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

# Button frame
frame = tk.Frame(root)
frame.pack()

for row in btns:
    btn_row = tk.Frame(frame)
    btn_row.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(btn_row, text=btn_text, font='Arial 18', relief=tk.RAISED, border=3)
        btn.pack(side='left', expand=True, fill='both')
        btn.bind("<Button-1>", click)

root.mainloop()
