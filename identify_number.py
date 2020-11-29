from tkinter import *
import random

num = random.randint(0, 100)


def check(event):
    counter = []
    user = int(ent1.get())
    print(num)

    cntr = sum(counter)
    if 0 < user < 100:
        if user == num:
            label2["text"] = "Congratulations, you guessed the number conceived!"
            label3["text"] = str(cntr)
        elif user < num:
            label2["text"] = "The number entered is less than conceived"
            counter.append(1)
        elif user > num:
            label2["text"] = "The number entered is greater than conceived"
            counter.append(1)
    else:
        label2["text"] = "Enter the number from 0 to 100"


root = Tk()

label_title = Label(root, font=20, text="Identify number").grid(row=0, column=1)
label1 = Label(root, font=18, text="Guess the number from 0 to 100").grid(row=1, column=1)

label2 = Label(root, font=20)
label3 = Label(root, font=18)

label2.grid(row=4, column=1, padx=1, pady=1)
label3.grid(row=5, column=1)

ent1 = Entry(root)
ent1.grid(row=2, column=1)

btn1 = Button(root, text='Check')
btn1.grid(row=3, column=1)

btn1.bind('<Button-1>', check)

root.mainloop()
