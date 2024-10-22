from tkinter import *
from tkinter import messagebox

'''Write a python to determine grade of the student
A: score>=90
B:score>=80 and score<90
C:score>=70 and score<80
D:score>=60 and score<70
E:score<60'''

win= Tk()

win.title("tkinter Module")
win.geometry("400x500")

def checkGrade():
    score = int(e1.get())
    printstatement = "The grade of student is"
    if score>=90:
        messagebox.showinfo(printstatement,f"Grade:A")
    elif (score>=80 and score<90):
        messagebox.showinfo(printstatement,"Grade:B")
    elif score>=70 and score<80:
        messagebox.showinfo(printstatement,"Grade:C")
    elif score>=60 and score<70:
        messagebox.showinfo(printstatement,"Grade:D")
    else:
        messagebox.showinfo(printstatement,"Grade:E")

l1=Label(win, text="Please Enter the grade of student")
l1.grid(row=0, column=0)
e1 = Entry(win)
e1.grid(row=1, column=0)
b1=Button(win, text="Check", command=checkGrade)
b1.grid(row=2, column=0)



'''write a python program to calculate a discount for a customer  based on  the purchased amount
using tkinter
conditions:
purchase>=$500: 20% discount
purchase>=200 and <$500: 10% discount
purchase<$200: NO Discount
input: text box in tkinter window
purchase=int(e1.get())
if():
  dis=0.2
elif():
    dis=0.1
else:
  "no discount"
amout_to_be_paid=
# print("total amout to be paid",)'''


def checkDiscount():
    purchase = int(e2.get())
    dis = 0
    if (purchase>=500):
        dis = 0.2
    elif (purchase>=200 and purchase<500):
        dis = 0.1
    else:
        dis = 0

    messagebox.showinfo("Discount calculator", f"Discount is {dis*100}%")
    messagebox.showinfo("Discount calculator",f"Total amount to be paid is {(purchase-(purchase*dis))}")

l2=Label(win, text="Discount calculator")
l2.grid(row=3,column=0)
l3 = Label(win, text="Please Enter the Purchased Amount")
l3.grid(row=4,column=0)
e2 = Entry(win)
e2.grid(row=5, column=0)

b2=Button(win, text="Check Discount", command=checkDiscount)
b2.grid(row=6, column=0)


win.mainloop()