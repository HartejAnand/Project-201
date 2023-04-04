from tkinter import *
window=Tk()

# add widgets here


window.title('interest Calculator')
window.geometry("400x500")
window.configure(bg='#FF0000')

#function for button
   
def calculate():
    r = int(r_entry.get())
    i = int(i_entry.get())
    p = int(p_entry.get())
    ans = (r*p*i)/100
    ans = round(ans, 1)
    name = username.get()
    
    result_label.destroy()

    msg=ans
        
    output_message=Label(result_frame,text=name+": your answer is "+str(ans), bg = "#FFEEEE", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="interest calculation", fg = "black", bg = "#FFEEEE", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "#FFEEEE", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

p_label=Label(window, text="Enter principle", fg = "black", bg = "#FFEEEE", font=("Calibri", 12))
p_label.place(x=20, y=140)

p_entry=Entry(window, text="", bd=2, width=15)
p_entry.place(x=150, y=142)

i_label=Label(window, text="enter time", fg = "black", bg = "#FFEEEE", font=("Calibri", 12))
i_label.place(x=20, y=185)

i_entry=Entry(window, text="", bd=2, width=15)
i_entry.place(x=150, y=187)

r_label=Label(window, text="Enter rate", fg = "black", bg = "#FFEEEE", font=("Calibri", 12))
r_label.place(x=20, y=235)

r_entry=Entry(window, text="", bd=2, width=15)
r_entry.place(x=150, y=237)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "#F0F000",bd=4,command=calculate)
calculate_button.place(x=20,y=300)

result_frame = LabelFrame(window,text="Result", bg = "#FFEEEE", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=350)

result_label=Label(result_frame,text=" ", bg = "#FFEEEE", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()