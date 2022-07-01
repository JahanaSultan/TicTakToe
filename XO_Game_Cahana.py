# TIC TAC TOE GAME


from tkinter import *
from tkinter import messagebox
import random


bgClick=True
count=0
win=False
arr=[]

def tictac():

    window2.destroy()
    def rematch(a):
        global count,win
        if a:
            count=0
            win=False
            window.destroy()
            main()
        else:
            window.destroy()

    def checkForWin():
        global win
        if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
            
            
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            win=True
            rematch(answer)
        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif count==9 and win==False:
            answer=messagebox.askyesno(title='Confirmation',
                          message='Draw. Rematch?')
            rematch(answer)
        



    def btnClick(button):
      global bgClick,count
      if button["text"] =="" and bgClick==True:
          count+=1
          button["text"]="X"
          bgClick=False
          checkForWin()
      elif button["text"]=="" and bgClick==False:
           count+=1
           button["text"]="O"
           bgClick=True
           checkForWin()


    window=Tk()
    window.title=("Two player")


    b1=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b1))
    b1.grid(row=2,column=0)
    b2=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b2))
    b2.grid(row=2,column=1)
    b3=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b3))
    b3.grid(row=2,column=2)
    b4=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b4))
    b4.grid(row=3,column=0)
    b5=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b5))
    b5.grid(row=3,column=1)
    b6=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b6))
    b6.grid(row=3,column=2)
    b7=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b7))
    b7.grid(row=4,column=0)
    b8=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b8))
    b8.grid(row=4,column=1)
    b9=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b9))
    b9.grid(row=4,column=2)

    window.mainloop()

def tictac1():
    window1.destroy()
    def rematch(a):
        global count,win,arr,bgClick
        if a:
            count=0
            win=False
            arr=[]
            bgClick=True
            window.destroy()
            main()
        else:
            window.destroy()

    def checkForWin():
        global win
        if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
            
            
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            win=True
            rematch(answer)
        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif count==9 and win==False:
            answer=messagebox.askyesno(title='Confirmation',
                          message='Draw. Rematch?')
            rematch(answer)
        



    def btnClick(button):
      global bgClick,count,arr
      if button["text"] =="" and bgClick==True:
          count+=1
          button["text"]="X"
          bgClick=False
          arr=[]
          checkForWin()
      rndm([b1,b2,b3,b4,b5,b6,b7,b8,b9,])



    def rndm(l):
        global bgClick,arr,count
        
        for i in l:
            if i["text"]=="":
                arr.append(i)
        if bgClick==False:
            count+=1 
            arr[random.randint(0,len(arr)-1)]["text"]="O"
            bgClick=True
            checkForWin()
            

    
    window=Tk()
    window.title("Intermediate")


    b1=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b1))
    b1.grid(row=2,column=0)
    b2=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b2))
    b2.grid(row=2,column=1)
    b3=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b3))
    b3.grid(row=2,column=2)
    b4=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b4))
    b4.grid(row=3,column=0)
    b5=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b5))
    b5.grid(row=3,column=1)
    b6=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b6))
    b6.grid(row=3,column=2)
    b7=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b7))
    b7.grid(row=4,column=0)
    b8=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b8))
    b8.grid(row=4,column=1)
    b9=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b9))
    b9.grid(row=4,column=2)



    window.mainloop()

def tictac2():
    window1.destroy()
    def rematch(a):
        global count,win,arr,bgClick
        if a:
            count=0
            win=False
            arr=[]
            bgClick=True
            window.destroy()
            main()
        else:
            window.destroy()

    def checkForWin():
        global win
        if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
            
            
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            win=True
            rematch(answer)
        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win X. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            win=True
            answer=messagebox.askyesno(title='Confirmation',
                          message='Win O. Rematch?')
            rematch(answer)
        elif count>=9 and win==False:
            answer=messagebox.askyesno(title='Confirmation',
                          message='Draw. Rematch?')
            rematch(answer)
        



    def btnClick(button):
      global bgClick,count,arr
      arr=[]
      if button["text"] =="" and bgClick==True:
          count+=1
          button["text"]="X"
          arr=[]
          bgClick=False
  
      checkForWin()
      minimax([b1,b2,b3,b4,b5,b6,b7,b8,b9,])



    def minimax(l):
        global bgClick,arr,count

# Qalibiyyet ehtimali varsa qalib gelsin

        if bgClick==False and b1['text'] == 'O' and b2['text'] == 'O' and b3["text"]== "":
            count+=1
            b3["text"]= "O"
            bgClick=True
        elif bgClick==False and b1['text'] == 'O' and b3['text'] == 'O' and b2["text"]== "":
            count+=1
            b2["text"]= "O"
            bgClick=True
        elif bgClick==False and b2['text'] == 'O' and b3['text'] == 'O' and b1["text"]== "":
            count+=1
            b1["text"]= "O"
            bgClick=True
        elif bgClick==False and b4['text'] == 'O' and b5['text'] == 'O' and b6["text"]== "":
            count+=1
            b6['text']= 'O'
            bgClick=True
        elif bgClick==False and b4['text'] == 'O' and b6['text'] == 'O' and b5["text"]== "":
            count+=1
            b5['text'] = 'O'
            bgClick=True
        elif bgClick==False and b5['text'] == 'O' and b6['text'] == 'O' and b4["text"]== "":
            count+=1
            b4['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == 'O' and b6['text'] == 'O' and b9["text"]== "":
            count+=1
            b9['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == 'O' and b9['text'] == 'O' and b6["text"]== "":
            count+=1
            b6['text'] = 'O'
            bgClick=True
        elif bgClick==False and b6['text'] == 'O' and b9['text'] == 'O' and b3["text"]== "":
            count+=1
            b3['text'] = 'O'
            bgClick=True
        elif bgClick==False and b7['text'] == 'O' and b8['text'] == 'O' and b9["text"]== "":
            count+=1
            b9['text'] = 'O'
            bgClick=True
        elif bgClick==False and b7['text'] == 'O' and b9['text'] == 'O' and b8["text"]== "":
            count+=1
            b8['text'] = 'O'
            bgClick=True
        elif bgClick==False and b8['text'] == 'O' and b9['text'] == 'O' and b7["text"]== "":
            count+=1
            b7['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == 'O' and b5['text'] == 'O' and b9["text"]== "":
            count+=1
            b9['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == "O" and b9['text'] == "O" and b5["text"]== "":
            count+=1
            b5['text'] = 'O'
            bgClick=True
        elif bgClick==False and b5['text'] == "O" and b9['text'] == "O" and b1["text"]== "":
            count+=1
            b1['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == "O" and b5['text'] == "O"  and b7["text"]== "":
            count+=1
            b7['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == "O" and b7['text'] == "O" and b5["text"]== "":
            count+=1
            b5['text'] = 'O'
            bgClick=True
        elif bgClick==False and b7['text'] == "O" and b5['text'] == "O" and b3["text"]== "":
            count+=1
            b3['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == "O" and b4['text'] == "O" and b7["text"]== "":
            count+=1
            b7['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == "O" and b7['text'] == "O" and b4["text"]== "":
            count+=1
            b4['text'] = 'O'
            bgClick=True
        elif bgClick==False and b4['text'] == "O" and b7['text'] == "O" and b1["text"]== "":
            count+=1
            b1['text'] = 'O'
            bgClick=True
        elif bgClick==False and b2['text'] == 'O' and b5['text'] == 'O' and b8["text"]== "":
             count+=1
             b8['text'] = 'O'
             bgClick=True
        elif bgClick==False and b5['text'] == 'O' and b8['text'] == 'O' and b2["text"]== "":
             count+=1
             b2['text'] = 'O'
             bgClick=True
        elif bgClick==False and b2['text'] == 'O' and b8['text'] == 'O' and b5["text"]== "":
             count+=1
             b5['text'] = 'O'
             bgClick=True

# Qalib gelmeye qoymasin
         
        elif bgClick==False and b1['text'] == 'X' and b2['text'] == 'X' and b3["text"]== "":
            count+=1
            b3["text"]= "O"
            bgClick=True
        elif bgClick==False and b1['text'] == 'X' and b3['text'] == 'X' and b2["text"]== "":
            count+=1
            b2["text"]= "O"
            bgClick=True
        elif bgClick==False and b2['text'] == 'X' and b3['text'] == 'X' and b1["text"]== "":
            count+=1
            b1["text"]= "O"
            bgClick=True
        elif bgClick==False and b4['text'] == 'X' and b5['text'] == 'X' and b6["text"]== "":
            count+=1
            b6['text']= 'O'
            bgClick=True
        elif bgClick==False and b4['text'] == 'X' and b6['text'] == 'X' and b5["text"]== "":
            count+=1
            b5['text'] = 'O'
            bgClick=True
        elif bgClick==False and b5['text'] == 'X' and b6['text'] == 'X' and b4["text"]== "":
            count+=1
            b4['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == 'X' and b6['text'] == 'X' and b9["text"]== "":
            count+=1
            b9['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == 'X' and b9['text'] == 'X' and b6["text"]== "":
            count+=1
            b6['text'] = 'O'
            bgClick=True
        elif bgClick==False and b6['text'] == 'X' and b9['text'] == 'X' and b3["text"]== "":
            count+=1
            b3['text'] = 'O'
            bgClick=True
        elif bgClick==False and b7['text'] == 'X' and b8['text'] == 'X' and b9["text"]== "":
            count+=1
            b9['text'] = 'O'
            bgClick=True
        elif bgClick==False and b7['text'] == 'X' and b9['text'] == 'X' and b8["text"]== "":
            count+=1
            b8['text'] = 'O'
            bgClick=True
        elif bgClick==False and b8['text'] == 'X' and b9['text'] == 'X' and b7["text"]== "":
            count+=1
            b7['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == 'X' and b5['text'] == 'X' and b9["text"]== "":
            count+=1
            b9['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == 'X' and b9['text'] == 'X' and b5["text"]== "":
            count+=1
            b5['text'] = 'O'
            bgClick=True
        elif bgClick==False and b5['text'] == 'X' and b9['text'] == 'X' and b1["text"]== "":
            count+=1
            b1['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == 'X' and b5['text'] == 'X'  and b7["text"]== "":
            count+=1
            b7['text'] = 'O'
            bgClick=True
        elif bgClick==False and b3['text'] == 'X' and b7['text'] == 'X' and b5["text"]== "":
            count+=1
            b5['text'] = 'O'
            bgClick=True
        elif bgClick==False and b7['text'] == 'X' and b5['text'] == 'X' and b3["text"]== "":
            count+=1
            b3['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == 'X' and b4['text'] == 'X' and b7["text"]== "":
            count+=1
            b7['text'] = 'O'
            bgClick=True
        elif bgClick==False and b1['text'] == 'X' and b7['text'] == 'X' and b4["text"]== "":
            count+=1
            b4['text'] = 'O'
            bgClick=True
        elif bgClick==False and b4['text'] == 'X' and b7['text'] == 'X' and b1["text"]== "":
            count+=1
            b1['text'] = 'O'
            bgClick=True
        elif bgClick==False and b2['text'] == 'X' and b5['text'] == 'X' and b8["text"]== "":
             count+=1
             b8['text'] = 'O'
             bgClick=True
        elif bgClick==False and b5['text'] == 'X' and b8['text'] == 'X' and b2["text"]== "":
             count+=1
             b2['text'] = 'O'
             bgClick=True
        elif bgClick==False and b2['text'] == 'X' and b8['text'] == 'X' and b5["text"]== "":
             count+=1
             b5['text'] = 'O'
             bgClick=True
        else:
             if bgClick==False and b5["text"]=="":
               count+=1
               b5["text"]="O"
               bgClick=True
             elif bgClick==False and b5["text"]=="X" and b1["text"]=="":
               count+=1
               b1["text"]="O"
               bgClick=True
             elif b5["text"]=="X" and b1["text"]=="O" and b9["text"]=="X" and bgClick==False and b7["text"]=="":
                b7["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b1["text"]=="X" and b9["text"]=="X" and bgClick==False and b4["text"]=="":
                b4["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b3["text"]=="X" and b7["text"]=="X" and bgClick==False and b6["text"]=="":
                b6["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b1["text"]=="X" and b8["text"]=="X" and bgClick==False and b6["text"]=="":
                b6["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b7["text"]=="X" and b2["text"]=="X" and bgClick==False and b6["text"]=="":
                b6["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b9["text"]=="X" and b2["text"]=="X" and bgClick==False and b4["text"]=="":
                b4["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b3["text"]=="X" and b8["text"]=="X" and bgClick==False and b4["text"]=="":
                b4["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b1["text"]=="X" and b6["text"]=="X" and bgClick==False and b3["text"]=="":
                b3["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b7["text"]=="X" and b6["text"]=="X" and bgClick==False and b9["text"]=="":
                b9["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b3["text"]=="X" and b4["text"]=="X" and bgClick==False and b1["text"]=="":
                b1["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b4["text"]=="X" and b9["text"]=="X" and bgClick==False and b7["text"]=="":
                b7["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b2["text"]=="X" and b8["text"]=="X" and bgClick==False and b3["text"]=="":
                b3["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="O" and b4["text"]=="X" and b6["text"]=="X" and bgClick==False and b3["text"]=="":
                b3["text"]="O"
                count+=1
                bgClick=True
             elif b5["text"]=="X" and b1["text"]=="":
               count+=1
               b1["text"]="O"
               bgClick=True
             else:
              for i in l:
               if i["text"]=="":
                 arr.append(i)
              if bgClick==False and len(arr)>0:
                count+=1
                arr[random.randint(0,len(arr)-1)]["text"]="O"
                bgClick=True
        checkForWin()
        

    
    window=Tk()
    window.title("Advanced")


    b1=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b1))
    b1.grid(row=2,column=0)
    b2=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b2))
    b2.grid(row=2,column=1)
    b3=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b3))
    b3.grid(row=2,column=2)
    b4=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b4))
    b4.grid(row=3,column=0)
    b5=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b5))
    b5.grid(row=3,column=1)
    b6=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b6))
    b6.grid(row=3,column=2)
    b7=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b7))
    b7.grid(row=4,column=0)
    b8=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b8))
    b8.grid(row=4,column=1)
    b9=Button(window,text="",height=4,width=8, font="Times 25 bold",command=lambda:btnClick(b9))
    b9.grid(row=4,column=2)



    window.mainloop()

def question():
    window2.destroy()
    global window1
    window1=Tk()
    window1.title("TIC TAC TOE")

    y=Label(window1,text="Intermediate Or Advance", font="Times")
    y.grid(row=1, column=1)
    q=Button(window1,text="Intermediate", font="Times",command=tictac1)
    q.grid(row=4,column=0)
    q1=Button(window1,text="Advance", font="Times",command=tictac2)
    q1.grid(row=4,column=2)

def main():
    global window2
    window2=Tk()
    window2.title("TIC TAC TOE")

    yazi=Label(window2,text="Single Player or 2 player:", font="Times")
    yazi.grid(row=1, column=1)
    btn1=Button(window2,text="single player", font="Times",command=question)
    btn1.grid(row=4,column=0)
    btn2=Button(window2,text="2 player", font="Times",command=tictac)
    btn2.grid(row=4,column=2)

main()

window2.mainloop()