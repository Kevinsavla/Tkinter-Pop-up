# Tkinter Pop-up

Simple Tkinter desktop apps that show a "Do you like me?" popup with Yes, No, and Cancel buttons. Built with Python's built-in `tkinter` library.

## Features

- **Yes** — Shows a friendly message and closes the app
- **No** — Reopens the popup after a short delay (playful loop)
- **Cancel** — Same as No; reopens the popup

## Requirements

- **Python 3.x** (3.6+)
- **tkinter** — included with most Python installations

No extra packages needed.

## Files

| File | Description |
|------|-------------|
| `Pop-up_message.py` | Uses a hidden main window and a `Toplevel` popup. Yes shows a message box, then exits. |
| `Pop_up_mesaage_2.py` | Recreates the window on No/Cancel. Yes prints a typing-effect message in the terminal. |

## How to Run

Run either script from the project folder:

```bash
python "Pop-up_message.py"
```

or

```bash
python "Pop_up_mesaage_2.py"
```

On Windows you can also double-click the `.py` file if Python is associated with it.

## Differences Between the Two Scripts

- **Pop-up_message.py**: Uses `messagebox.showinfo()` for the "Yes" response and keeps the root window hidden. Cleaner separation between main window and popup.
- **Pop_up_mesaage_2.py**: Uses a typing effect in the console for "Yes" and recreates the Tk window each time you click No or Cancel.

## License

Free to use and modify.
