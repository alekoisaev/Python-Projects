from tkinter import *

def check(event):
    e1 = int(ent1.get())
    e2 = int(ent2.get())
    e3 = int(ent3.get())
    e4 = int(ent4.get())
    e5 = int(ent5.get())
    e6 = int(ent6.get())

    x = (e1 + e2 + e3 + e4 + e5 + e6)/6

    if x >= 0 and x <= 100:
        if x >= 91 and x <= 100:
            label2["text"] = "A"
        elif x <= 90 and x >= 81:
            label2["text"] = "B"
        elif x <= 80 and x >= 71:
            label2["text"] = "C"
        elif x <= 70 and x >= 61:
            label2["text"] = "D"
        elif x <= 60 and x >= 51:
            label2["text"] = "E"
        elif x <= 50 and x >= 41:
            label2["text"] = "Fx"
        elif x <= 40 and x >= 0:
            label2["text"] = "F"
    else:
        print("Error !")

root = Tk()

label1 = Label(root, font=20, text="ქულების გამომთვლელი").grid(row=1, column=1)
label2 = Label(root, font=16)
label2.grid(row=9, column=1)

sub1 = Label(root, text="პროგრამირება").grid(row=2, column=0)
sub2 = Label(root, text="მათემატიკა").grid(row=3, column=0)
sub3 = Label(root, text="ფიზიკა").grid(row=4, column=0)
sub4 = Label(root, text="ციფრული ტექნოლოგიები").grid(row=5, column=0)
sub5 = Label(root, text="ეკონომიკა").grid(row=6, column=0)
sub6 = Label(root, text="ბიზნესი").grid(row=7, column=0)

ent1 = Entry(root)
ent1.grid(row=2, column=1)
ent2 = Entry(root)
ent2.grid(row=3, column=1)
ent3 = Entry(root)
ent3.grid(row=4, column=1)
ent4 = Entry(root)
ent4.grid(row=5, column=1)
ent5 = Entry(root)
ent5.grid(row=6, column=1)
ent6 = Entry(root)
ent6.grid(row=7, column=1)

btn1 = Button(root, text='გამოთვლა')
btn1.grid(row=8, column=1)

btn1.bind('<Button-1>', check)

root.mainloop()