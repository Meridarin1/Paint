from tkinter import *
from Paint import Paint


def main():

    root = Tk()
    root.geometry("800x800+300+100")

    Paint(root)

    root.mainloop()

main()


