import tkinter as tk
import sys
import time

def typing_effect(message,delay=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def on_yes():
    root.destroy()
    typing_effect("I always knew you like me?")

def on_no_or_cancel():
    root.destroy()
    time.sleep(0.5)
    create_popup()

def create_popup():
    global root
    root = tk.Tk()
    root.title("Do you like me?")
    root.geometry("320x150")
    root.resizable(False, False)

    label = tk.Label(root, text="Do you like me?", font="Arial 12")
    label.pack(pady=20)

    yes_btn = tk.Button(root, text="Yes", bg="Green", fg="WHite", width=10, command=on_yes)
    yes_btn.pack(side="left", padx=15, pady=10, expand=True)

    no_btn = tk.Button(root, text="No", bg="Red", fg="White",width=10, command=on_no_or_cancel)
    no_btn.pack(side="left", padx=15, pady=10, expand=True)

    cancel_btn = tk.Button(root, text="Cancel", bg="Grey", fg="White",width=10, command=on_no_or_cancel)
    cancel_btn.pack(side="left", padx=15, pady=10, expand=True)

    root.mainloop()

create_popup()