# By Nolan Nelsen
# Written on 4/17/2026
# Program #2: Information

import tkinter as tk

def show_info():
    name_label.config(text="Name: Nolan Nelsen")
    address_label.config(text="Address: 5094 Rose Avenue, Johnsville, TX")

def main():
    window = tk.Tk()
    window.title("Info Display")
    window.geometry("350x200")

    global name_label
    global address_label

    name_label = tk.Label(window, text="", font=("Serif", 12))
    address_label = tk.Label(window, text="", font=("Serif", 12))

    name_label.pack(pady=5)
    address_label.pack(pady=5)

    show_button = tk.Button(window, text="Show Info", command=show_info)
    quit_button = tk.Button(window, text="Quit", command=window.destroy)

    show_button.pack(pady=10)
    quit_button.pack()

    window.mainloop()

main()
