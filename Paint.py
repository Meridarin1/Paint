from tkinter import *
from tkinter.colorchooser import *
from PIL import Image, ImageTk

class Paint:

    drawing_tool = "oval"
    left_but = "up"
    x_pos, y_pos = None, None
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None
    color_picked = 'black'

    def __init__(self, root):
        drawing_area = Canvas(root)


        toolbar = Frame(root, relief=RAISED)

        pencil_img = Image.open("pencil.png")
        oval_img = Image.open("oval.png")
        arc_img = Image.open("arc.png")
        rectangle_img = Image.open("rectangle.png")
        line_img = Image.open("line.png")

        pencil_icon = ImageTk.PhotoImage(pencil_img)
        oval_icon = ImageTk.PhotoImage(oval_img)
        arc_icon = ImageTk.PhotoImage(arc_img)
        rectangle_icon = ImageTk.PhotoImage(rectangle_img)
        line_icon = ImageTk.PhotoImage(line_img)

        pencil_button = Button(toolbar, image=pencil_icon, command=lambda : self.set_drawing_tool('pencil'))
        oval_button = Button(toolbar, image=oval_icon, command=lambda: self.set_drawing_tool('oval'))
        arc_button = Button(toolbar, image=arc_icon, command=lambda: self.set_drawing_tool('arc'))
        line_button = Button(toolbar, image=line_icon, command=lambda: self.set_drawing_tool('line'))
        rectangle_button = Button(toolbar, image=rectangle_icon, command=lambda: self.set_drawing_tool('rectangle'))

        pencil_button.image = pencil_icon
        oval_button.image = oval_icon
        arc_button.image = arc_icon
        line_button.image = line_icon
        rectangle_button.image = rectangle_icon

        pencil_button.pack(side=LEFT)
        oval_button.pack(side=LEFT)
        arc_button.pack(side=LEFT)
        line_button.pack(side=LEFT)
        rectangle_button.pack(side=LEFT)

        toolbar.pack(side=TOP)
        drawing_area.pack(expand=True, fill=BOTH)
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
        self.function_dict = {'pencil': self.pencil_draw, 'line' : self.line_draw, 'rectangle' : self.rectangle_draw,
                              'arc' : self.arc_draw, 'oval' : self.oval_draw}

    #---------Notice mouse Clicked--------------------------------------
    def left_but_down(self, event):
        self.left_but = "down"

        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    #---------Notice mouse Released--------------------------------------
    def left_but_up(self, event):
        self.left_but = "up"

        self.x_pos = None
        self.y_pos = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        #instead of using alot if else statements I use a dictionary to
        #decide what drawing tool is picked
        self.function_dict[self.drawing_tool](event)

    #---------Track mouse motion-----------------------------------------
    def motion(self, event=None):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)


    #---------Draw pencile line------------------------------------------
    def pencil_draw(self, event=None):

        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE,
                                         fill=self.color_picked)

            self.x_pos = event.x
            self.y_pos = event.y

    #--------Draw line----------------------------------------------------
    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE,
                                     fill=self.color_picked)

    #--------Draw Rectangle-----------------------------------------------
    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                          fill=self.color_picked,
                                          outline=self.color_picked,
                                          width=2)
    #--------Draw Oval---------------------------------------------------
    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):

            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                     fill=self.color_picked,
                                     outline=self.color_picked,
                                     width=2)

    #--------Draw Arc----------------------------------------------------
    def arc_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_arc(coords, start=0, extent=150,
                                    style=ARC, fill=self.color_picked, outline=self.color_picked)

    def set_drawing_tool(self, drawing_tool):
        self.drawing_tool = drawing_tool

    def set_color(self):
        self.color_picked = askcolor()