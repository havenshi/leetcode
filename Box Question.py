import random
class Box(object):
    def __init__(self):
        self.lock = False
        self.open = False
        self.correctColor = None
        self.blue = False
        self.red = False
        self.button = None
    def pressButton(self, button):
        self.button = button
        if button == "Blue":
            self.blue = True
            self.lock = True
            self.correctColor = "Red"
        else:
            self.red = True
            self.lock = True
            self.correctColor = "Blue"
    def returnButton(self):
        return self.button
    def setButton(self, correctColor):
        self.correctColor = correctColor
        self.lock = False
    def openBox(self):
        if self.lock == False:
            self.open = True
    def printButton(self):
        if self.blue and self.red:
           return " pressed both buttons Blue and Red!"
        elif self.blue:
            return " pressed any button Blue."
        else:
            return " pressed any button Red."
    def printCorrectButton(self):
        return "pressed the correct button " + self.correctColor + "."
    def printOpen(self):
        return " opened the box."

class Human(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.box = None
    def change(self, box):
        self.box = box
        if box.open:
            self.alive = True
        else:
            self.alive = False

class areTheyAlive(object):
    def printMessage(self, human1, human2):
        if human1.box.blue and human1.box.red and human2.box.blue and human2.box.red:
            print "Both of " + human1.name + " and " + human2.name + " are alive!"
        else:
            if human1.alive:
                print human1.name + " is alive."
            else:
                print human1.name + " is dead..."
            if human2.alive:
                print human2.name + " is alive."
            else:
                print human2.name + " is dead..."

class Solution(object):
    def __init__(self):
        self.lock = False
        self.correct = None
    def operateBox(self):
        haruto = Human("Haruto")
        aoi = Human("Aoi")
        buttons = ["Blue", "Red"]
        zhoumu = 0
        while zhoumu < 3:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            print "In zhoumu " + str(zhoumu) + ":"
            if zhoumu == 0:
                Haruto_Box = Box()
                button = buttons[random.randint(0, 1)]
                Haruto_Box.pressButton(button)
                print haruto.name + Haruto_Box.printButton()
                haruto.change(Haruto_Box)
                Aoi_Box = Box()
                Aoi_Box.setButton(Haruto_Box.correctColor)
                print aoi.name + " " + Aoi_Box.printCorrectButton()
                Aoi_Box.openBox()
                print aoi.name + Aoi_Box.printOpen()
                aoi.change(Aoi_Box)
            if zhoumu == 1:
                Aoi_Box = Box()
                button = buttons[random.randint(0, 1)]
                Aoi_Box.pressButton(button)
                print aoi.name + Aoi_Box.printButton()
                aoi.change(Aoi_Box)
                aoi.box.blue = True
                aoi.box.red = True
                Haruto_Box = Box()
                Haruto_Box.setButton(Aoi_Box.correctColor)
                print haruto.name + " " + Haruto_Box.printCorrectButton()
                Haruto_Box.openBox()
                print haruto.name + Haruto_Box.printOpen()
                haruto.change(Haruto_Box)
                print aoi.name + aoi.box.printButton()
                areTheyAlive().printMessage(haruto, aoi)
                zhoumu += 1
                continue
            if zhoumu == 2:
                haruto.box.blue = True
                haruto.box.red = True
                print haruto.name + haruto.box.printButton()
            areTheyAlive().printMessage(haruto, aoi)
            zhoumu += 1

if __name__ == "__main__":
    answer=Solution()
    answer.operateBox()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# In zhoumu 0:
# Haruto pressed any button Blue.
# Aoi pressed the correct button Red.
# Aoi opened the box.
# Haruto is dead...
# Aoi is alive.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# In zhoumu 1:
# Aoi pressed any button Red.
# Haruto pressed the correct button Blue.
# Haruto opened the box.
# Aoi pressed both buttons Blue and Red!
# Haruto is alive.
# Aoi is dead...
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# In zhoumu 2:
# Haruto pressed both buttons Blue and Red!
# Both of Haruto and Aoi are alive!