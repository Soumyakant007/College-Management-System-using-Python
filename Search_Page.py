from tkinter import *  
import random
import Marksheet_Backend
import Marksheet_Frontend
import tkinter.messagebox
import os

              

def main():
              global master
              master =Tk()
              master.title('Search Page')
              master.geometry('700x350')
              master.config(bg = 'navajowhite')
              roll = StringVar()
              frame = LabelFrame(master, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'wheat')
              frame.place(x=50,y=50, width = 600, height = 100)

              label = Label(frame, text = 'Enter Roll Number', font = ('arial',25,'bold'), bg = 'wheat' )
              label.place(x=0,y=0,width=400,height=70)

              entry = Entry(frame, font = ('arial',25,'bold'), textvariable = roll)
              entry.place(x=350,y=20,width=200,height=40)

              
                
              def Search():
                     if(len(roll.get()) != 0):
                           row = Marksheet_Backend.search(int(roll.get()))
                           print(row)
                           Marksheet_Frontend.search_result_marksheet(row)
                     else:
                            tkinter.messagebox.askokcancel('Attention','Please enter valid Roll No.')
                            return

              def new():
                     filename = 'Marksheet_Frontend.py'
                     os.system(filename)
                     os.system('notepad'+filename)
              def Exit():
                  master.destroy()
                  return
              frame2 = LabelFrame(master, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'wheat')
              frame2.place(x=50,y=200, width = 600, height = 100)


              btnSearch = Button(frame2, text = 'SEARCH', width = 15, font = ('arial',15,'bold'), command=Search)
              btnSearch.place(x=10,y=10,width=100,height=50)
              btnNew = Button(frame2, text = 'CREATE NEW', font = ('arial',15,'bold'), command=new)
              btnNew.place(x=220,y=10,width=140,height=50)
              btnexit=Button(frame2,text='EXIT',width=15,font=('arial',15,'bold'),command=Exit)
              btnexit.place(x=450,y=10,width=100,height=50)
              #master.mainloop()



if __name__=='__main__':
      main()
