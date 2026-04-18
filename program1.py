# By Nolan Nelsen
# Written on 4/17/2026
# Program #1: Favorite Saying

import tkinter as tk

def main():
    # The main window
    window = tk.Tk()
    window.title("My Favorite Saying")
    window.geometry("400x400")

    # Label with favorite saying
    message = "Jesus is Lord."
    label = tk.Label(window, text=message, font=("Serif", 20), wraplength=350, justify="center")

    label.pack(expand=True)

    window.mainloop()

main()
