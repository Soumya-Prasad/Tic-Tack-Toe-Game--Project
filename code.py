from tkinter import*
import tkinter.messagebox
window=Tk()
window.title("Tic Tac Toe")
p1=StringVar()
p2=StringVar()
label=Label(window,text="Player 1:",font=("Times 20 bold"),bg="white",fg="black",width=8,height=1,bd=4).grid(row=1,column=0)
label=Label(window,text="Player 2:",font=("Times 20 bold"),bg="white",fg="black",width=8,height=1,bd=4).grid(row=2,column=0)
player1=Entry(window,textvariable=p1,bd=5).grid(row=1,column=1,columnspan=8)
player2=Entry(window,textvariable=p2,bd=5).grid(row=2,column=1,columnspan=8)
bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def checker(buttons):
    global bclick,flag,player2_name,player1_name,playerb,pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
     tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
   
buttons=StringVar()
global button1,button2,button3,button4,button5,button6,button7,button8,button9
button1=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button1))
button2=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button2))
button3=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button3))
button4=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button4))
button5=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button5))
button6=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button6))
button7=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button7))
button8=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button8))
button9=Button(window,text=" ",font=("Times 20 bold"),fg="white",bg="grey",height=4,width=8,command=lambda:checker(button9))
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
button7.grid(row=5, column=0)
button8.grid(row=5, column=1)
button9.grid(row=5, column=2)
window.mainloop()