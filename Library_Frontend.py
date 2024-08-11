from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import Library_Backend
import Main_Menu
import Std_info_FrontEnd
import Search_Page
import Fee_Frontend
def library():
              
               #================================================Functions======================================================
              def BookRec(event):
                     try:
                            global selected_tuple
                            index = Listbox_2.curselection()[0]
                            selected_tuple = Listbox_2.get(index)

                            Entry_0.delete(0, END)
                            Entry_0.insert(END, selected_tuple[1])  
                            Entry_1.delete(0, END)
                            Entry_1.insert(END, selected_tuple[2])                           
                            Entry_2.delete(0, END)
                            Entry_2.insert(END, selected_tuple[3])
                            Entry_3.delete(0, END)
                            Entry_3.insert(END, selected_tuple[4])
                            Entry_4.delete(0, END)
                            Entry_4.insert(END, selected_tuple[5])
                            Entry_5.delete(0, END)
                            Entry_5.insert(END, selected_tuple[6])
                            Entry_6.delete(0, END)
                            Entry_6.insert(END, selected_tuple[7])
                            Entry_7.delete(0, END)
                            Entry_7.insert(END, selected_tuple[8])
                            Entry_8.delete(0, END)
                            Entry_8.insert(END, selected_tuple[9])
                            Entry_9.delete(0, END)
                            Entry_9.insert(END, selected_tuple[10])
                            Entry_10.delete(0, END)
                            Entry_10.insert(END, selected_tuple[11])
                            Entry_11.delete(0, END)
                            Entry_11.insert(END, selected_tuple[12])
                            Entry_12.delete(0, END)
                            Entry_12.insert(END, selected_tuple[13])
                             

                     except IndexError:
                            pass
              def Insert():
                     if(len(refno.get()) != 0):
                            Library_Backend.insert(Mtype.get(), refno.get(), fname.get(), surname.get()\
                                                   , address.get(), post.get(), mobno.get(), ID.get()\
                                                   , title.get(), author.get(), borrow.get(), due.get()\
                                                   , loan.get())
                            Listbox_2.delete(0, END)
                            Listbox_2.insert(END , (Mtype.get(), refno.get(), fname.get(), surname.get()\
                                                         , address.get(), post.get(), mobno.get(), ID.get()\
                                                         , title.get(), author.get(), borrow.get(), due.get()\
                                                         , loan.get()))
                            

              def Display():
                     Listbox_2.delete(0, END)
                     for row in Library_Backend.view():
                            Listbox_2.insert(END, row, str(' '))  
                                                       
              def Exit():
                     Exit = tkinter.messagebox.askyesno('Library Management System','Confirm if you want to Exit')
                     if Exit > 0:
                            root.destroy()
                            return
                                                                    
              def Reset():
                     Mtype.set('')
                     refno.set('')
                     fname.set('')
                     surname.set('')
                     address.set('')
                     post.set('')
                     mobno.set('')
                     ID.set('')
                     title.set('')
                     author.set('')
                     borrow.set('')
                     due.set('')
                     loan.set('')
                     Display.delete('1.0',END)
                     Listbox_2.delete(0, END)

              def Delete():
                     selected_tuple = Listbox_2.get(index)
                     Library_Backend.delete(selected_tuple[0])
                     Reset()
                     Display()

              def Update():
                     Library_Backend.delete(selected_tuple[0])
                     Library_Backend.insert(Mtype.get(), refno.get(), fname.get(), surname.get()\
                                                  , address.get(), post.get(), mobno.get(), ID.get()\
                                                  , title.get(), author.get(), borrow.get(), due.get()\
                                                  , loan.get())
                     Listbox_2.delete(0, END)
                     Listbox_2.insert(END,(Mtype.get(), refno.get(), fname.get(), surname.get()\
                                                  , address.get(), post.get(), mobno.get(), ID.get()\
                                                  , title.get(), author.get(), borrow.get(), due.get()\
                                                  , loan.get()))

              def Search():
                     Listbox_2.delete(0, END)
                     for row in Library_Backend.search(Mtype.get(), refno.get(), fname.get(), surname.get()\
                                                  , address.get(), post.get(), mobno.get(), ID.get()\
                                                  , title.get(), author.get(), borrow.get(), due.get()\
                                                  , loan.get()):
                            Listbox_2.insert(END, row, str(' '))

              def Details():
                     Display.delete('1.0',END)
                     Display.insert(END, 'Book ID: ' + ID.get() + '\n')
                     Display.insert(END, 'Title: ' + title.get() + '\n')
                     Display.insert(END, 'Author:  ' +  author.get() + '\n')
                     Display.insert(END, 'Edition: ' + edsn.get() + '\n')
                     Display.insert(END, 'Year of Publision: \t' + yop.get() + '\n')
                     Display.insert(END, 'Date Borrowed: ' + borrow.get() + '\n')
                     Display.insert(END, 'Date Due:' + due.get() + '\n')
                     Display.insert(END, 'Days in Loan: ' + loan.get() + '\n')
              def Home():
                    Main_Menu.menu()
              def information():
                    Std_info_FrontEnd.information()
              def fee():
                    Fee_Frontend.fee()
              def mark():
                  Marksheet_Frontend.marksheet()
              def search():
                    Search_Page.main()
              def close():
                    root.destroy()
              root = Tk()
              root.title('Library Management System')
              root.geometry('1350x750')
              root.config(bg = 'navajowhite')
            #_____________________________________Menu________________________
              menubar = Menu(root)
              filemenu = Menu(menubar, tearoff=0)
              filemenu.add_command(label="Home",command=Home)
              filemenu.add_separator()

              infomenu=Menu(menubar,tearoff=0)
              infomenu.add_command(label="Information",command=information)
              infomenu.add_separator()

              feemenu=Menu(menubar,tearoff=0)
              feemenu.add_command(label="fee",command=fee)
              feemenu.add_separator()

              markmenu=Menu(menubar,tearoff=0)
              markmenu.add_command(label="Mark",command=mark)
              markmenu.add_separator()

              searchmenu=Menu(menubar,tearoff=0)
              searchmenu.add_command(label="search",command=search)
              searchmenu.add_separator()

              closemenu=Menu(menubar,tearoff=0)
              closemenu.add_command(label="Close",command=close)
              closemenu.add_separator()

              menubar.add_cascade(label="Home", menu=filemenu)
              menubar.add_cascade(label="Info", menu=infomenu)
              menubar.add_cascade(label="Fee", menu=feemenu)
              menubar.add_cascade(label="Mark", menu=markmenu)
              menubar.add_cascade(label="Search", menu=searchmenu)
              menubar.add_cascade(label="Close", menu=closemenu)
              root.config(menu=menubar)
       #===================================================Variables===================================================
              Mtype = StringVar()
              refno = StringVar()
              fname = StringVar()
              surname = StringVar()
              address = StringVar()
              post = StringVar()
              mobno = StringVar()
              ID = StringVar()
              title = StringVar()
              author = StringVar()
              borrow = StringVar()
              due = StringVar()
              loan = StringVar()
              yop = StringVar()
              edsn = StringVar()
              


      
                             

       #=====================================================Frames=====================================================
              Main_Frame = Frame(root, bg = 'navajowhite')
              Main_Frame.grid()

              Title_Frame_1 = Frame(Main_Frame, width = 1350, bg = 'navajowhite', relief = RIDGE, bd = 15, padx = 20)
              Title_Frame_1.pack(side = TOP)

              lblTitle = Label(Title_Frame_1, font = ('arial',40,'bold'), text = '\tLibrary Management System\t', \
                                    bg = 'navajowhite', padx = 13)
              lblTitle.grid()

              Button_Frame = Frame(Main_Frame, width = 1350, height = 50, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Button_Frame.pack(side = BOTTOM)

              Detail_Frame = Frame(Main_Frame, width = 1350, height = 100, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Detail_Frame.pack(side = BOTTOM)

              Data_Frame = Frame(Main_Frame, width = 1350, height = 400, relief = RIDGE, bd = 15, bg = 'navajowhite')
              Data_Frame.pack(side = BOTTOM)

              Frame_1 = LabelFrame(Data_Frame, width = 800, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                              text = "Library Membership Info:", padx = 20, font = ('arial',15,'bold'))
              Frame_1.pack(side = LEFT, padx = 3)

              Frame_2 = LabelFrame(Data_Frame, width = 550, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                              text = "Book Details:", padx = 20, font = ('arial',15,'bold'))
              Frame_2.pack(side = RIGHT)


       #================================================Labels========================================================
              Label_1 = Label(Frame_1, text = 'Member type', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_1.grid(row = 0, column = 0, sticky = W)
              Label_2 = Label(Frame_1, text = 'Reference No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_2.grid(row = 1, column = 0, sticky = W)
              Label_3 = Label(Frame_1, text = 'First Name', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_3.grid(row = 2, column = 0, sticky = W)
              Label_4 = Label(Frame_1, text = 'Surname', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_4.grid(row = 3, column = 0, sticky = W)
              Label_5 = Label(Frame_1, text = 'Address', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_5.grid(row = 4, column = 0, sticky = W)
              Label_6 = Label(Frame_1, text = 'Post Code', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_6.grid(row = 5, column = 0, sticky = W)
              Label_7 = Label(Frame_1, text = 'Mobile No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_7.grid(row = 6, column = 0, sticky = W)
              Label_8 = Label(Frame_1, text = 'Book ID', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_8.grid(row = 0, column = 2, sticky = W)
              Label_9 = Label(Frame_1, text = 'Book Title', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_9.grid(row = 1, column = 2, sticky = W)
              Label_10 = Label(Frame_1, text = 'Author', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_10.grid(row = 2, column = 2, sticky = W)
              Label_11 = Label(Frame_1, text = 'Date Borrowed', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_11.grid(row = 3, column = 2, sticky = W)
              Label_13 = Label(Frame_1, text = 'Date Due', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_13.grid(row = 4, column = 2, sticky = W)
              Label_13 = Label(Frame_1, text = 'Days in Loan', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              Label_13.grid(row = 5, column = 2, sticky = W)
              


       #================================================Entries========================================================
              Entry_0 = ttk.Combobox(Frame_1, values = (' ','Student','Faculty','Staff Member'), \
                                          font = ('arial',13,'bold'), width = 23, textvariable = Mtype )
              Entry_0.grid(row = 0, column = 1)
              Entry_1 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = refno )
              Entry_1.grid(row = 1, column = 1, padx = 15)
              Entry_2 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = fname)
              Entry_2.grid(row = 2, column = 1, padx = 15)
              Entry_3 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = surname)
              Entry_3.grid(row = 3, column = 1, padx = 15)
              Entry_4 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = address)
              Entry_4.grid(row = 4, column = 1, padx = 15)
              Entry_5 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = post)
              Entry_5.grid(row = 5, column = 1, padx = 15)
              Entry_6 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = mobno)
              Entry_6.grid(row = 6, column = 1, padx = 15)
              Entry_7 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = ID)
              Entry_7.grid(row = 0, column = 4, padx = 15)
              Entry_8 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = title)
              Entry_8.grid(row = 1, column = 4, padx = 15)
              Entry_9 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = author)
              Entry_9.grid(row = 2, column = 4, padx = 15)
              Entry_10 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = borrow)
              Entry_10.grid(row = 3, column = 4, padx = 15)
              Entry_11 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = due)
              Entry_11.grid(row = 4, column = 4, padx = 15)
              Entry_12 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = loan)
              Entry_12.grid(row = 5, column = 4, padx = 15)                                        


       #=============================================Widgets=========================================================
              Display = Text(Frame_2, font = ('arial',13,'bold'), width = 28, height = 11)
              Display.grid(row = 0, column = 2)


              List_of_Books = [' C',' C++',' Java',' Python',' PHP',' Java Script',' My SQL',' Data Structure',' Linux',\
                               ' Operating System',' Web Developement',' Data Science',' Algorithms',' Android', \
                               ' VB.net']


       #===========================================Function for Books Details=========================================
              def SelectedBook(event):
                     value = str(Listbox_1.get(Listbox_1.curselection()))
                     v = value

                     if (v == ' C'):
                            ID.set('ISBN 525341')
                            title.set('Programming using C')
                            author.set('Yashwant Kanetkar')
                            yop.set('2019')
                            edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 14)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('14')
                            due.set(d3)
                            Details()
                     elif (v == ' C++'):
                            ID.set('ISBN 345687')
                            title.set('Programming using C++')
                            author.set('Yashwant Kanetkar')
                            yop.set('2019')
                            edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('10')
                            due.set(d3)
                            Details()
                     elif (v == ' Java'):
                            ID.set('ISBN 643842')
                            title.set('Java Programming')
                            author.set('Joshua Bloch')
                            yop.set('2019')
                            edsn.set('7th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('13')
                            due.set(d3)
                            Details()
                     elif (v == ' Python'):
                            ID.set('ISBN 564524')
                            title.set('Python Programming')
                            author.set('John Zelle')
                            yop.set('2019')
                            edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('13')
                            due.set(d3)
                            Details()
                     elif (v == ' PHP'):
                            ID.set('ISBN 735893')
                            title.set('PHP Programming')
                            author.set('Alan Forbes')
                            yop.set('2019')
                            edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('15')
                            due.set(d3)
                            Details()
                     elif (v == ' Java Script'):
                            ID.set('ISBN 643842')
                            title.set('Java Script Programming')
                            author.set('Jon Duckett.')
                            yop.set('2019')
                            edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('13')
                            due.set(d3)
                            Details()
                     elif (v == ' My SQL'):
                            ID.set('ISBN 649635')
                            title.set('My SQL Programming')
                            author.set('Groff James')
                            yop.set('2019')
                            edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 20)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('20')
                            due.set(d3)
                            Details()
                     elif (v == ' Data Structure'):
                            ID.set('ISBN 531588')
                            title.set('Data Structure')
                            author.set('Karumanchi Narasimha')
                            yop.set('2019')
                            edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 11)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('11')
                            due.set(d3)
                            Details()
                     elif (v == ' Linux'):
                            ID.set('ISBN 356853')
                            title.set('Linux Administration')
                            author.set('SOYINKA')
                            yop.set('2019')
                            edsn.set('1st')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 6)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('6')
                            due.set(d3)
                            Details()
                     elif (v == ' Operating System'):
                            ID.set('ISBN 536453')
                            title.set('OS Concepts ')
                            author.set('Silberschatz Abraham')
                            yop.set('2019')
                            edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 12)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('12')
                            due.set(d3)
                            Details()
                     elif (v == ' Web Developement'):
                            ID.set('ISBN 543548')
                            title.set('Web Developement ')
                            author.set('Paul McFedries')
                            yop.set('2019')
                            edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('15')
                            due.set(d3)
                            Details()
                     elif (v == ' Data Science'):
                            ID.set('ISBN 835764')
                            title.set('Data Science Concept ')
                            author.set('David Stephenson')
                            yop.set('2019')
                            edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('15')
                            due.set(d3)
                            Details()
                     elif (v == ' Algorithms'):
                            ID.set('ISBN 535674')
                            title.set('Basics of Algorithm ')
                            author.set('Karumanchi Narasimha')
                            yop.set('2019')
                            edsn.set('7th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('10')
                            due.set(d3)
                            Details()
                     elif (v == ' Android'):
                            ID.set('ISBN 356452')
                            title.set('Android Programming')
                            author.set('Harwani B. M')
                            yop.set('2019')
                            edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 9)
                            d3 = (d1 + d2)
                            borrow.set(d1)
                            loan.set('9')
                            due.set(d3)
                            Details()
                            
       #===========================================List Box and Scroll Bar==========================================                    
              sb_1 = Scrollbar(Frame_2)
              sb_1.grid(row =0, column = 1, sticky = 'ns')

              Listbox_1 = Listbox(Frame_2, font = ('arial',13,'bold'), width = 20, height = 10)
              Listbox_1.bind('<<ListboxSelect>>', SelectedBook)
              Listbox_1.grid(row = 0, column = 0)
              sb_1.config(command = Listbox_1.yview)

              
              sb_2 = Scrollbar(Detail_Frame)
              sb_2.grid(row = 1, column = 1, sticky = 'ns')

              Listbox_2 = Listbox(Detail_Frame, font = ('arial',13,'bold'), width = 144, height = 11)
              Listbox_2.bind('<<ListboxSelect>>', BookRec)
              Listbox_2.grid(row = 1, column = 0)
              sb_2.config(command = Listbox_2.yview)

              for items in List_of_Books:
                     Listbox_1.insert(END, items)


       #=============================================Buttons=========================================================
              Button_1 = Button(Button_Frame, text = 'SAVE', font = ('arial',15,'bold'), width = 10, command = Insert)
              Button_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              Button_2 = Button(Button_Frame, text = 'DISPLAY', font = ('arial',15,'bold'), width = 10, command = Display)
              Button_2.grid(row = 0, column = 1, padx = 8)
              Button_3 = Button(Button_Frame, text = 'RESET', font = ('arial',15,'bold'), width = 10, command = Reset)
              Button_3.grid(row = 0, column = 2, padx = 8)
              Button_4 = Button(Button_Frame, text = 'UPDATE', font = ('arial',15,'bold'), width = 10, command = Update)
              Button_4.grid(row = 0, column = 3, padx = 8)
              Button_5 = Button(Button_Frame, text = 'SEARCH', font = ('arial',15,'bold'), width = 10, command = Search)
              Button_5.grid(row = 0, column = 4, padx = 8)
              Button_6 = Button(Button_Frame, text = 'DELETE', font = ('arial',15,'bold'), width = 10, command = Delete)
              Button_6.grid(row = 0, column = 5, padx = 8)
              Button_7 = Button(Button_Frame, text = 'EXIT', font = ('arial',15,'bold'), width = 10, command = Exit)
              Button_7.grid(row = 0, column = 6, padx = 8)

              root.mainloop()

if __name__ == '__main__':
       library()
