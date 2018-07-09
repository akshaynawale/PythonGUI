#!/usr/bin/env python3

from tkinter import Tk, Label, Button, expand

class MainWindow():
    """
    Main window class
    """
    def __init__(self, root_win):
        self.root_win = root_win
        self.label = Label(self.root_win, text = "This is the label")
        self.label.pack(expand)

    
def main():
    """
    main logic goes here...
    """
    root_window = Tk()
    MainWindow(root_window)
    root_window.mainloop()

if __name__ == "__main__":
    main()
