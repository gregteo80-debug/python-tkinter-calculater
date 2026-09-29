import tkinter as tk

first_num = None
second_num  = None
res = None
op = None
w = tk.Tk()
w.geometry("600x600")
w.title("Calculater")
w.config(bg="#120303")
w.resizable(False,False)

enter = tk.Entry(w,width=50,font=30,fg="red")
enter.grid(row=0,column=0,columnspan=7,padx=30,pady=25)
def number1():
    enter.insert(tk.END,"1")

button1 = tk.Button(w,text="1",width=15,command=number1)

button1.grid(row=1,column=0,columnspan=1)
def number2():
    enter.insert(tk.END,"2")

button2 = tk.Button(w,text="2",width=15,command=number2)

button2.grid(row=1,column=1,columnspan=1)

def number3():
    enter.insert(tk.END,"3")

button3 = tk.Button(w,text="3",width=15,command=number3)

button3.grid(columnspan=1,row=1,column=2)

def number4():
    enter.insert(tk.END,"4")

button4 = tk.Button(w,text="4",width=15,command=number4)

button4.grid(row=1,column=3,columnspan=1)

def number5():
    enter.insert(tk.END,"5")

button5 = tk.Button(w,text="5",width=15,command=number5)

button5.grid(columnspan=1,row=2,column=0,pady=15)

def number6():
    enter.insert(tk.END,"6")

button6 = tk.Button(w,text="6",width=15,command=number6)

button6.grid(columnspan=1,row=2,column=1,pady=15)

def number7():
    enter.insert(tk.END,"7")

button7 = tk.Button(w,text="7",width=15,command=number7)

button7.grid(columnspan=1,row=2,column=2,pady=15)
def number8():
    enter.insert(tk.END,"8")

button8 = tk.Button(w,text="8",width=15,command=number8)

button8.grid(columnspan=1,row=2,column=3,pady=15)


def number9():
    enter.insert(tk.END,"9")

button9 = tk.Button(w,text="9",width=15,command=number9)

button9.grid(columnspan=1,row=3,column=0)

def number0():
    enter.insert(tk.END,"0")

button0 = tk.Button(w,text="0",width=15,command=number0)

button0.grid(columnspan=1,row=3,column=1)

def clear():
    enter.delete(0,tk.END)

button_clear = tk.Button(w,text="C",width=15,command=clear,bg="#A16363")

button_clear.grid(columnspan=1,row=3,column=2)

def eqauls():
    global first_num
    global second_num
    global op
    global res

    second_num = enter.get()

    if op == "+":
        try:
            res = int(first_num) + int(second_num)
        except ValueError:
            enter.delete(0,tk.END)
            enter.insert(tk.END,"Error №2...Value...")

    if op == "-":
        try:
            res = int(first_num) - int(second_num)
        except ValueError:
            enter.delete(0,tk.END)
            enter.insert(tk.END,"Error №2...Value...")

    if op == "*":
        try:
            res = int(first_num) * int(second_num)
        except ValueError:
            enter.delete(0,tk.END)
            enter.insert(tk.END,"Error №2...Value...")

    if op == "/":
        if int(second_num)  != 0:
            try:    
                res = int(first_num) / int(second_num)
                        
                
            except ValueError:
                enter.delete(0,tk.END)
                enter.insert(tk.END,"Error №2...Value...")
                        
        else:
            enter.delete(0,tk.END)
            enter.insert(tk.END,"Error №3...divededByZero...")
        
        

    if first_num == None or second_num == None or res == None:
        enter.delete(0,tk.END)
        enter.insert(tk.END,"Error №1...")
    else:
        enter.delete(0,tk.END)
        enter.insert(tk.END,res)


buttoneqauls = tk.Button(w,text="=",width=15,command=eqauls,bg="#820d0d")

buttoneqauls.grid(columnspan=1,row=3,column=3)

def plus():
    global op
    global first_num
    op = "+"
    first_num = enter.get()
    enter.delete(0,tk.END)

def mins():
    global op
    global first_num
    op = "-"
    first_num = enter.get()
    enter.delete(0,tk.END)

def times():
    global op
    global first_num
    op = "*"
    first_num = enter.get()
    enter.delete(0,tk.END)
def divided():
    global op
    global first_num
    op = "/"
    first_num = enter.get()
    enter.delete(0,tk.END)



buttonplaus = tk.Button(w,text="+" ,width=15,command=plus)

buttonplaus.grid(columnspan=1,row=4,column=0,pady=15)

buttonmines = tk.Button(w,text="-",width=15,command=mins)

buttonmines.grid(columnspan=1,row=4,column=1,pady=15)

buttontimes = tk.Button(w,text="*",width=15,command=times)

buttontimes.grid(columnspan=1,row=4,column=2)

buttondevided = tk.Button(w,text="/",width=15,command=divided)

buttondevided.grid(columnspan=1,row=4,column=3)



w.mainloop()

          



          





        
     
        
     



