from tkinter import *
from obliczenia import *
def dodawanie():
    points = str(Obliczenia.dodawanie())
    text.config(text="Punkty śmieszności: " + points)
def odejmowanie():
    points = str(Obliczenia.odejmowanie())
    text.config(text="Punkty śmieszności: " + points)

#Tkinter window
window = Tk()
window.title("Punkty śmieszności")
window.minsize(640, 70)
window.maxsize(640, 70)


start_sum = str(Obliczenia.suma())

textFrame = Frame(window)
textFrame.pack(side = TOP)

text = Label(textFrame, text="Punkty śmieszności: "+ start_sum, font=("Arial",14,"italic"))
button1 = Button(textFrame, text="Śmieszny żart (+1)", command=dodawanie, bg="green", font=("Arial",12))
button2 = Button(textFrame, text="Nieśmieszny żart(-1)", command=odejmowanie, bg="red", font=("Arial",12))

text.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)

#close Tkinter window
window.mainloop()
