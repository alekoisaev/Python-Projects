from tkinter import *

def check(event):
    dge1 = int(dge_ent.get())

    if tve_ent.get() == '12':
        if dge1 < 22:
            show["text"] = "მშვილდოსანი"
        else:
            show["text"] = "თხის რქა"
    elif tve_ent.get() == '1':
        if dge1 < 21:
            show["text"] = "თხის რქა"
        else:
            show["text"] = "მერწყული"
    elif tve_ent.get() == '2':
        if dge1 < 20:
            show["text"] = "მერწყული"
        else:
            show["text"] = "თევზები"
    elif tve_ent.get() == '3':
        if dge1 < 21:
            show["text"] = "თევზები"
        else:
            show["text"] = "ვერძი"
    elif tve_ent.get() == '4':
        if dge1 < 21:
            show["text"] = "ვერძი"
        else:
            show["text"] = "კურო"
    elif tve_ent.get() == '5':
        if dge1 < 22:
            show["text"] = "კურო"
        else:
            show["text"] = "ტყუპები"
    elif tve_ent.get() == '6':
        if dge1 < 22:
            show["text"] = "ტყუპები"
        else:
            show["text"] = "კირჩხიბი"
    elif tve_ent.get() == '7':
        if dge1 < 24:
            show["text"] = "კირჩხიბი"
        else:
            show["text"] = "ლომი"
    elif tve_ent.get() == '8':
        if dge1 < 24:
            show["text"] = "ლომი"
        else:
            show["text"] = "ქალწული"
    elif tve_ent.get() == '9':
        if dge1 < 24:
            show["text"] = "ქალწული"
        else:
            show["text"] = "მორიელი"
    elif tve_ent.get() == '10':
        if dge1 < 24:
            show["text"] = "მორიელი"
        else:
            show["text"] = "მშვილდოსანი"
    elif tve_ent.get() == '11':
        if dge1 < 23:
            show["text"] = "მშვილდოსანი"
        else:
            show["text"] = "თხის რქა"
    else:
        show["text"] = "შეიყვანეთ 1-12 მდე (თვე) "



root = Tk()

name = Label(root, text="სახელი და გვარი", font=25)
name_ent = Entry(root)

dge = Label(root, text="დღე", font=25)
dge_ent = Entry(root)

tve = Label(root, text="თვე", font=25)
tve_ent = Entry(root)

weli = Label(root, text="წელი", font=25)
weli_ent = Entry(root)

show = Label(root)

btn1 = Button(root, text="გამოთვლა")

name.grid(row=0, column=0)
name_ent.grid(row=0, column=1)
dge.grid(row=1, column=0)
dge_ent.grid(row=1, column=1)
tve.grid(row=2, column=0)
tve_ent.grid(row=2, column=1)
weli.grid(row=3, column=0)
weli_ent.grid(row=3, column=1)
show.grid(row=5, column=1)
#show1.grid(row=5, column=0)

btn1.grid(row=4, column=1)
btn1.bind("<Button-1>", check)

root.mainloop()
