from tkinter import*

def ClickingTheButton(numbers):
     global operator
     operator+=str(numbers)
     text_Input.set(operator)
def ClickToClear():
    global operator
    operator=""
    text_Input.set("")
def btnEqualInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal,font=('cambria', 25,'bold'), textvariable=text_Input, bd=30,insertwidth=4,
                   bg="powder blue", justify='right').grid(columnspan=4)
btn7 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="7",command=lambda: ClickingTheButton(7)).grid(row=1,column=0)
btn8 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="8",command=lambda: ClickingTheButton(8)).grid(row=1,column=1)
btn9 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="9",command=lambda: ClickingTheButton(9)).grid(row=1,column=2)
Addition = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="+",command=lambda: ClickingTheButton("+")).grid(row=1,column=3)
#========================================================================================
btn4 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="4",command=lambda: ClickingTheButton(4)).grid(row=2,column=0)
btn5 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="5",command=lambda: ClickingTheButton(5)).grid(row=2,column=1)
btn6 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="6",command=lambda: ClickingTheButton(6)).grid(row=2,column=2)
Subtraction = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="-",command=lambda: ClickingTheButton("-")).grid(row=2,column=3)
# ===========================================================================
btn1 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="1",command=lambda: ClickingTheButton(1)).grid(row=3,column=0)
btn2 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="2",command=lambda: ClickingTheButton(2)).grid(row=3,column=1)
btn3 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="3",command=lambda: ClickingTheButton(3)).grid(row=3,column=2)
Multiply = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="*",command=lambda: ClickingTheButton("*")).grid(row=3,column=3)

#========================================================================================
btn0 = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="0",command=lambda: ClickingTheButton(0)).grid(row=4,column=0)
btnClear = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="C",command=lambda:ClickToClear()).grid(row=4,column=1)
btnEqual = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="=",command=btnEqualInput).grid(row=4,column=2)
Divison = Button(cal,padx=16,bd=8, fg="black",font=('cambria', 25,'bold'),
              text="/",command=lambda: ClickingTheButton("/")).grid(row=4,column=3)

cal.mainloop()
