from tkinter import *
from tkinter import messagebox

# a1: write  python program using tkinter to
# to check speed of the car and give warning and
# penalty if the speed exceeded.
# business conditions:
# speed_limit=90 kmph
# i. speed<=speed_limit: NO Penalty
# ii. speed<=speed_limit+20: warning
# iii.speed>speed_limit+20: penalty 2000

win= Tk()

win.title("tkinter Module")
win.geometry("400x500")

def checkSpeed():
    speed = int(e1.get())
    speed_limit = 90
    if speed<=speed_limit:
        messagebox.showinfo("RTO Dept","NO Penalty")
    elif speed<=speed_limit + 20:
        messagebox.showinfo("RTO Dept","Warning")
    elif speed>speed_limit + 20:
        messagebox.showinfo("RTO Dept","Penalty 2000 Rs")



l1=Label(win, text="Speed of Car")
l1.grid(row=0, column=0)
e1 = Entry(win)
e1.grid(row=1, column=0)
b1=Button(win, text="Check", command=checkSpeed)
b1.grid(row=2, column=0)

# ----------------------------------------------------------------------------
# Assignment2:
# Write a python program using tkinter for
# withdraw money from the ATM
# business conditions:
# balance=10000
# daily_limit=20000
# i. withdrawal amount <=balance
# ii. withdrawl notes should be multiples of 100
# iii. daily limit should not be exceeded

def bankAccount():
    notes_list = [200,500,2000]
    daily_limit_taken = 0
    note_Value = int(e3.get())
    withdrawal_amount = int(e2.get())
    if withdrawal_amount <= balance:
        if note_Value in notes_list:
            if daily_limit_taken < daily_limit:
                updated_bal = balance - withdrawal_amount
                res_place = Label(win, text=f"Available bal:{updated_bal}", fg="red")
                res_place.grid(row=8, column=0)
                messagebox.showinfo("Transaction Details", "Transaction Successful")
            else:
                res_place = Label(win, text="Day Limit exceeded", fg="red")
                res_place.grid(row=8, column=0)
        else:
            res_place = Label(win, text=f"{note_Value}Rs Notes are Not Available", fg="red")
            res_place.grid(row=8, column=0)
    else:

        res_place = Label(win, text="insufficient funds", fg="red")
        res_place.grid(row=8, column=0)


daily_limit=20000
balance=10000
l2=Label(win, text="ATM")
l2.grid(row=3,column=0)
l3 = Label(win, text="Please Enter the Amount to withdrawal")
l3.grid(row=4,column=0)
e2 = Entry(win)
e2.grid(row=5, column=0)
l4 = Label(win, text="Note Value")
l4.grid(row=4,column=2)
e3 = Entry(win)
e3.grid(row=5, column=2)
l5 = Label(win, text=f"Daily withdrawal Limit is:{daily_limit}",fg="red")
l5.grid(row=7,column=0)

b2=Button(win, text="WithDraw", command=bankAccount)
b2.grid(row=6, column=0)



win.mainloop()