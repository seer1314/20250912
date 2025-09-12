import tkinter as tk
win = tk.Tk()
win.title('Tkinter GUI')#標題
win.geometry('400x200')#視窗大小

#win.minsize(width='400',height='200')#視窗限制最小
#win.maxsize(width='1024',height='768')#視窗限制最大

#win.resizable(width=True,height=False)#設定視窗長寬調節鎖定
#win.iconbitmap(file='')#圖標改變
win.config(background="skyblue")#視窗底改色
win.attributes('-alpha',0.9)#視窗透明度
win.attributes('-topmost',True)#至頂



#Buttom
def say_hi():
    print('Tkiner matters')

def ok():
    t = en.get()
    lb.config(text=t)
    
btn = tk.Button(text="CLICK ME")
btn.config(command=say_hi)
btn.pack()

btn2 = tk.Button(text='Enter')
btn2.config(command=ok)
btn2.pack()

#Label
lb = tk.Label(text='Tkinter Trial')
lb.pack()

#Entry
en = tk.Entry()
en.pack()

#Function
 
win.mainloop()