import tkinter
import csv
from tkinter import font
root=tkinter.Tk()
root.geometry('400x400')
f1=font.Font(family='Arial',size=12)
f2=font.Font(family='Arial',size=4)
frames=[]
radio_buttons=[]
SCORE=0

def SUBMIT():
	fp.pack_forget()
	frames[0].pack()
	count(10,0)
def next(index):
	for f in frames:
		f.pack_forget()
	frames[index].pack()
def s():
    global SCORE
    SCORE = 0
    timer.pack_forget()
    for i in range(10):
        if e[i].get() == questions[i][2]:
            SCORE += 1
    e1.set(f'{nentry.get()} : {SCORE}')
    for f in frames:
        f.pack_forget()
    score.pack()
    file=open('quiz.txt','a')
    wr=csv.writer(file)
    wr.writerow([f'{nentry.get()}',f'{SCORE}'])
    file.close()
def count(m,si):
	if m!=0 or si!=0:
		if si==0:
			si=59
			m-=1
			timer.config(text=f'THE TIME LEFT IS:[{m}:59]')
		else:
				si-=1
				timer.config(text=f'THE TIME LEFT IS:[{m}:{si}]')
		root.after(1000,count,m,si)
	else:
		timer.config(text='TIME IS OUT')
		s()
questions = [
    ("What is the capital of India?", ["Mumbai", "Delhi", "Chennai", "Kolkata"], "Delhi"),
    ("Which is the largest planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
    ("Who wrote Ramayana?", ["Valmiki", "Tulsidas", "Kalidas", "Vyas"], "Valmiki"),
    ("Which gas do plants absorb?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "Carbon Dioxide"),
    ("Python is a ____?", ["Snake", "Programming Language", "Fruit", "Dance"], "Programming Language"),
    ("Speed = ?", ["Distance/Time", "Time/Distance", "Force/Mass", "Work/Time"], "Distance/Time"),
    ("Sun rises in the?", ["West", "North", "East", "South"], "East"),
    ("Water boils at?", ["90°C", "50°C", "100°C", "150°C"], "100°C"),
    ("Who is the father of Computers?", ["Newton", "Einstein", "Charles Babbage", "Tesla"], "Charles Babbage"),
]
e=[tkinter.StringVar() for i in range(10)]
timer=tkinter.Label(root,text=' ')
timer.pack()
for k in range(10):
	frame=tkinter.Frame(root)
	frames.append(frame)
	if k>0 and k<9:
		tkinter.Label(frames[k],text=questions[k][0],font=f2).pack()
		for _ in range(4):
		  rb = tkinter.Radiobutton(frames[k], text=questions[k][1][_],variable=e[k], value=questions[k][1][_], font=('Arial', 4))
		  rb.pack(anchor="w", padx=20)
		  radio_buttons.append(rb)
		tkinter.Button(frames[k],text='PREVIOUS',command=lambda idx=k:next(idx-1),font=f2).pack()
		tkinter.Button(frames[k],text='NEXT',command=lambda idx=k:next(idx+1),font=f2).pack()
		tkinter.Button(frames[k],text='SUBMIT',command=s).pack()
	elif k==0:
		tkinter.Label(frames[k],text=questions[k][0],font=f2).pack()
		for _ in range(4):
		  rb = tkinter.Radiobutton(frames[k], text=questions[k][1][_],variable=e[k], value=questions[k][1][_], font=('Arial', 4))
		  rb.pack(anchor="w", padx=20)
		  radio_buttons.append(rb)
		tkinter.Button(frames[k],text='NEXT',command=lambda idx=k:next(idx+1),font=f2).pack()
		tkinter.Button(frames[k],text='SUBMIT',command=s,font=f2).pack()
	else:
		tkinter.Label(frames[k],text=questions[k][0],font=f2).pack()
		for _ in range(4):
		  rb = tkinter.Radiobutton(frames[k], text=questions[k][1][_],variable=e[k], value=questions[k][1][_], font=('Arial', 4))
		  rb.pack(anchor="w", padx=20)
		  radio_buttons.append(rb)
		tkinter.Button(frames[k],text='PREVIOUS',command=lambda idx=k:next(idx-1),font=f2).pack()
		tkinter.Button(frames[k],text='SUBMIT',command=s,font=f2).pack()	
e1=tkinter.StringVar()
fp=tkinter.Frame(root)
name=tkinter.Label(fp,text='NAME',font=f1)
name.pack()
nentry=tkinter.Entry(fp)
nentry.pack()
tkinter.Button(fp,text='SUBMIT',font=f2,command=SUBMIT).pack()
fp.pack()
score=tkinter.Frame(root)
tkinter.Label(score,textvariable=e1).pack()
root.mainloop()
