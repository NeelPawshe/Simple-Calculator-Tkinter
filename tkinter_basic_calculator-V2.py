from tkinter import *

root = Tk()
root.title("simple calculator")
root.configure(bg="#2E2E2E") # #2E2E2E (a dark charcoal grey)for the root window

# Define colors and fonts
Font = ("Arial", 16, "bold")
Button_bg = "#4E4E4E" # #4E4E4E (a lighter shade of grey)
Button_fg = "White" 
Operator_bg = "#FF9500" # #FF9500 (orange) for operators
Clear_bg = "#D4D4D2" # #D4D4D2 (light grey) for Clear button
clear_fg = "Black" 
Equal_fg = "#FF9500" # #FF9500 (orange)
Equal_bg = "White" 
Entry_fg = "#A9A9A9" #  #A9A9A9 (a light grey)
Entry_bg = "Black" 


e = Entry(root, width = 20, borderwidth = 5, font=("Arial", 24), bg = Entry_bg, fg = Entry_fg, justify = "right" )                             
e.grid(row = 0, column = 0, columnspan = 4,  padx = 10, pady=10)

def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_decimal():
    current = e.get()
    if "." not in current:
        e.insert(END, ".")
    
def button_clear():
    e.delete(0, END)

def button_operator(operator_type):
    try:
        first_number = e.get()
        global f_num
        global math_op
        math_op = operator_type
        f_num = float(first_number)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "ERROR")

def button_equal():
    try:
        second_number = e.get()
        e.delete(0, END)
        s_num = float(second_number)
                       
        if math_op == "addition":
            e.insert(0, f_num + s_num)
            
        elif math_op == "subtraction":
            e.insert(0, f_num - s_num)
            
        elif math_op == "multiplication":
             e.insert(0, f_num * s_num)
                
        if math_op == "division":
            if s_num == 0:
                e.insert(0, "Error: Div by 0")
            else:
                e.insert(0, f_num / s_num)
    except (ValueError, NameError ):
        e.delete(0, END)
        e.insert(0, "ERROR")
         
button_1 = Button(root, text="1", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=lambda: button_click(0))
button_decimal = Button(root, text=".", padx=43, pady=20, font=Font, bg=Button_bg, fg=Button_fg, command=button_decimal)

button_add = Button(root, text="+", padx=47, pady=20, font=Font, bg=Operator_bg, fg=Button_fg, command=lambda: button_operator("addition"))
button_subtract = Button(root, text="-", padx=50, pady=20, font=Font, bg=Operator_bg, fg=Button_fg, command=lambda: button_operator("subtraction"))
button_multiply = Button(root, text="×", padx=40, pady=20, font=Font, bg=Operator_bg, fg=Button_fg, command=lambda: button_operator("multiplication"))
button_divide = Button(root, text="÷", padx=47, pady=20, font=Font, bg=Operator_bg, fg=Button_fg, command=lambda: button_operator("division"))

button_equal = Button(root, text="=", padx=47, pady=60, font=Font, bg=Equal_bg, fg=Equal_fg, command=button_equal)
button_clear = Button(root, text="C", padx=93, pady=20, font=Font, bg=Clear_bg, fg=clear_fg, command=button_clear)

button_clear.grid(row=1, column=0, columnspan=2)
button_divide.grid(row=1, column=3)
button_multiply.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equal.grid(row=4, column=3, columnspan=2, rowspan=2)

button_0.grid(row=5, column=0)
button_decimal.grid(row=5, column=2)

root.mainloop()
