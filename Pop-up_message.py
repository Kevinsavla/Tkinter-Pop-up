import tkinter as tk
from tkinter import messagebox
import time

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Do you like me?")
    popup.geometry("320x150")
    popup.resizable(False, False)

    label = tk.Label(popup, text="Do you like me?", font="Arial 12")
    label.pack(pady=20)

    #Yes Button
    yes_btn = tk.Button(popup, text="Yes", bg="Green", fg="White", width=10,
                        command=lambda: yes_action(popup))
    yes_btn.pack(side="left", padx=15, pady=10, expand=True)

    # No Button
    no_button = tk.Button(popup, text="No", bg="Red", fg="White", width=10,
                          command=lambda: no_action(popup))
    no_button.pack(side="left", padx=15, pady=10, expand=True)

    # Cancel Button
    cancel_btn = tk.Button(popup, text="Cancel", bg="Grey", fg="White", width=10,
                           command=lambda: cancel_action(popup))
    cancel_btn.pack(side="left", padx=15, pady=10, expand=True)

def yes_action(popup):
    popup.destroy()
    messagebox.showinfo("Message", "I always knew that you like me?")
    root.quit()

def no_action(popup):
    popup.destroy()
    root.after(500, show_popup)   #Reopen after 0.5 sec

def cancel_action(popup):
    popup.destroy()
    root.after(500, show_popup)


root = tk.Tk()
root.withdraw()   # Hide main root window

show_popup()

root.mainloop()

