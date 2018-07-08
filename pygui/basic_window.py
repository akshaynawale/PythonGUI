#!/env/usr/bin python3

from tkinter import Tk, Label, Button

class MyFirstGUI():
    def __init__(self, master):
        self.master = master
        master.title("A simple Layout")

        self.label_list: List[Label] = []

        self.label = Label(master, text="This is our first GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()


    def greet(self):
        new_label = Label(self.master, text="tu mala dabala ;(")
        new_label.pack()
        self.label_list.append(new_label)
        print("Greetings na Bhau")

def main():
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
