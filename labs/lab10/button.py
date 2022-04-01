"""
Name: Thomas Scola
button.py
Problem: to form a class called button.py
Certification of Authenticity:
I had the assistance of brooke duvall from the CSL
"""
from graphics import*
class Button:

    def __init__(self, shape, label):
        self.rectangle = shape
        self.text = Text(shape.getCenter(), str(label))

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.text.draw(win)
        self.rectangle.draw(win)

    def undraw(self):
        self.text.undraw()
        self.rectangle.undraw()

    def is_clicked(self, point):
        if point.getX() >= self.rectangle.getP1().getX() and point.getY() <= self.rectangle.getP2().getY() and \
                point.getX() <= self.rectangle.getP2().getX() and point.getY() >= self.rectangle.getP1().getY():
            return True
        return False

    def color_button(self, color):
        self.rectangle.setFill(color)
