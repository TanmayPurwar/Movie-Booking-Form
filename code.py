from tkinter import *

window = Tk()

window.title("question5")
window.geometry('500x300')
lbl1=Label(window,text="Movie Booking ID")#Movie Booking ID
lbl1.place(x=0,y=0)
tbox1 = Text(window)
tbox1.place(x=100, y=0,height=20,width=150)
lbl2=Label(window,text="Person Name:")#Person Name:
lbl2.place(x=0,y=25)
tbox2 = Text(window)
tbox2.place(x=100, y=25,height=20,width=150)
lbl3=Label(window,text="Movie Name:")#Movie Name:
lbl3.place(x=0,y=50)
tbox3 = Text(window)
tbox3.place(x=100, y=50,height=20,width=150)
lbl3=Label(window,text="Class")#Class
lbl3.place(x=30,y=80)
lbl4=Label(window,text="No. of Tickets")#No. of Tickets
lbl4.place(x=0,y=120)
radio=Radiobutton(window,text="A",value=1)
radio.place(x=150,y=80)
radio2=Radiobutton(window,text="B",value=2)
radio2.place(x=200,y=80)
lbl5=Label(window,text="Time of Show")#Time of Show
lbl5.place(x=250,y=80)
clas=Checkbutton(text="7.15pm")
clas.place(x=340,y=80)
clas2=Checkbutton(text="9am")
clas2.place(x=410,y=80)
slider = Scale (window, from_=0, to=20, orient=HORIZONTAL)
slider.place(x=120, y=110)
button1 = Button(window, text="Insert")
button1.place(x=20, y=170, height=30, width=50)
button2 = Button(window, text="Delete")
button2.place(x=20, y=200, height=30, width=50)
button3 = Button(window, text="Update")
button3.place(x=150, y=170, height=30, width=50)
button4 = Button(window, text="Select")
button4.place(x=150, y=200, height=30, width=50)
window.mainloop()
