from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


win=Tk()

win.geometry("300x300")
win.title("CBSE Grading system")

label1=ttk.Label(text="Select Marks")
label1.pack(fill=X, padx=10,pady=10)

# Combobox
marks=IntVar()
combo=ttk.Combobox(win, textvariable=marks)

combo['values']=[m for m in range(0,101)]
combo['state']='readonly'

combo.pack(fill=X,padx=10,pady=10)
def get_grade(event):
    if (marks.get() >=91 and marks.get()<=100):
        grade="A1"
        
    elif (marks.get() >=81 and marks.get()<=90):
        grade="A2"
    elif (marks.get() >=71 and marks.get()<=80):
        grade="B1"
        
    elif (marks.get() >=61 and marks.get()<=70):
        grade="B2"
        
    elif (marks.get()>=51 and marks.get()<60):
        grade="C1"
        
    elif (marks.get() >=41 and marks.get()<=50):
        grade="C2"
        
    elif (marks.get()>=33 and marks.get()<=40):
        grade="D"
        
    elif (marks.get() >=21 and marks.get()<=32):
        grade="E1"
        
    else:
        grade="E2"
        
    showinfo(title="Result",message=f'You secured {grade} grade')
        
    
combo.bind("<<ComboboxSelected>>",get_grade)

win.mainloop()
