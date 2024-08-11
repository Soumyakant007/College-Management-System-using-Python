from tkinter import*
import tkinter.messagebox  
import random
import Std_info_BackEnd
from tkinter import ttk
import Main_Menu
import Library_Frontend
import Fee_Frontend             
import Search_Page
import Marksheet_Frontend
def information():
                     def StudentRec(event):
                            try: 
                                   global selected_tuple
                                   
                                   index = listbox.curselection()[0]
                                   selected_tuple = listbox.get(index)

                                   Entry_name.delete(0, END)
                                   Entry_name.insert(END, selected_tuple[1])
                                   Entry_fname.delete(0, END)
                                   Entry_fname.insert(END, selected_tuple[2])
                                   Entry_mname.delete(0, END)
                                   Entry_mname.insert(END, selected_tuple[3])
                                   Entry_address.delete(0, END)
                                   Entry_address.insert(END, selected_tuple[4])
                                   Entry_mobno.delete(0, END)
                                   Entry_mobno.insert(END, selected_tuple[5])
                                   Entry_emailID.delete(0, END)
                                   Entry_emailID.insert(END, selected_tuple[6])
                                   Entry_dob.delete(0, END)
                                   Entry_dob.insert(END, selected_tuple[7])
                                   Entry_gender.delete(0, END)
                                   Entry_gender.insert(END, selected_tuple[8])
                            except IndexError:
                                   pass


                     def Add():
                            if(len(name.get()) != 0):
                               Std_info_BackEnd.insert(name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), gender.get())
                               print("Done")
                               listbox.delete(0, END)
                               listbox.insert(END, (name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), gender.get()))

                     def Display():
                               listbox.delete(0, END)
                               for row in Std_info_BackEnd.view():
                                      listbox.insert(END, row, str(' '))


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                            if Exit > 0:
                                   master.destroy()
                                   return 
                            

                     def Reset():
                            name.set('')
                            fname.set('')
                            mname.set('')
                            address.set('')
                            mobno.set('')
                            email.set('')
                            dob.set('')
                            gender.set('')
                            listbox.delete(0, END)

                     

                     def Delete():
                            if(len(name.get()) != 0):
                               Std_info_BackEnd.delete(selected_tuple[0])
                               Reset()
                               Display()


                     def Search():
                            listbox.delete(0, END)
                            for row in Std_info_BackEnd.search(name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(),gender.get()):
                                   listbox.insert(END, row, str(' '))
                                   

                     def Update():
                            if(len(name.get()) != 0):
                               Std_info_BackEnd.delete(selected_tuple[0])
                            if(len(name.get()) != 0):
                               Std_info_BackEnd.insert(name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                                       gender.get())

                               listbox.delete(0, END)
                               listbox.insert(END, (name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                                       gender.get()))
                     def home():
                         Main_Menu.menu()

                     def library():
                         Library_Frontend.library()

                     def fee():
                         Fee_Frontend.fee()

                     def mark():
                        Marksheet_Frontend.marksheet()

                     def search():
                         Search_Page.main()

                     def close():
                        master.destory()

                     master = Tk()
                     master.title('Student Information')
                     master.geometry('1350x750')
                     master.config(bg = 'navajowhite')
                     master.resizable(0,0)

                     menubar = Menu(master)
                     homemenu = Menu(menubar, tearoff=0)
                     homemenu.add_command(label="Home",command=home)
                     homemenu.add_separator()

                     librarymenu=Menu(menubar,tearoff=0)
                     librarymenu.add_command(label="Library",command=library)
                     librarymenu.add_separator()

                     feemenu=Menu(menubar,tearoff=0)
                     feemenu.add_command(label="Fee",command=fee)
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

                     menubar.add_cascade(label="Home", menu=homemenu)
                     menubar.add_cascade(label="Library",menu=librarymenu)
                     menubar.add_cascade(label="Fee",menu=feemenu)
                     menubar.add_cascade(label="Mark",menu=markmenu)
                     menubar.add_cascade(label="Search",menu=searchmenu)
                     menubar.add_cascade(label="Close",menu=closemenu)
                     master.config(menu=menubar)
                     
              #========================================================Variables=====================================================================
                     name = StringVar()
                     fname = StringVar()
                     mname = StringVar()
                     address = StringVar()
                     mobno = StringVar()
                     email = StringVar()
                     dob = StringVar()
                     gender = StringVar()
                     


               #==========================================================Functions====================================================================
                     
                     


                     #============================================================Frames=====================================================================

                     Main_Frame = LabelFrame(master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'navajowhite',bd = 15, relief = 'ridge')
                     Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                     Frame_1 = LabelFrame(Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT INFORMATION ')
                     Frame_1.grid(row = 1, column = 0, padx = 10)

                     Frame_2 = LabelFrame(Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT DATABASE')
                     Frame_2.grid(row = 1, column = 1, padx = 5)                  
                     
                     Frame_3 = LabelFrame(master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                               bg = 'navajowhite', relief = 'ridge', bd = 13)
                     Frame_3.grid(row = 2, column = 0, pady = 10)


                     
                     #========================================================Labels of Frame_1========================================================
                     Label_name = Label(Frame_1, text = 'Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     Label_fname = Label(Frame_1, text = 'Father Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_fname.grid(row = 1, column = 0, sticky = W, padx = 20)
                     Label_mname = Label(Frame_1, text = 'Mother Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_mname.grid(row = 2, column = 0, sticky = W, padx = 20)
                     Label_address = Label(Frame_1, text = 'Address', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                     Label_mobno = Label(Frame_1, text = 'Mobile Number', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20)
                     Label_emailID = Label(Frame_1, text = 'Email ID', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20)
                     Label_dob = Label(Frame_1, text = 'Date of Birth', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_dob.grid(row = 6, column = 0, sticky = W, padx = 20)
                     Label_gender = Label(Frame_1, text = 'Gender', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     Label_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)


                     #========================================================Entries of Frame_1========================================================
                     Entry_name = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = name)
                     Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                     Entry_fname = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = fname)
                     Entry_fname.grid(row = 1, column = 1, padx = 10, pady = 5)
                     Entry_mname = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = mname)
                     Entry_mname.grid(row = 2, column = 1, padx = 10, pady = 5)
                     Entry_address = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = address)
                     Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                     Entry_mobno = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = mobno)
                     Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
                     Entry_emailID = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = email)
                     Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
                     Entry_dob = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = dob)
                     Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 5)
                     Entry_gender = ttk.Combobox(Frame_1, values = (' ','Male','Female','Others'),\
                                                      font = ('arial',17,'bold'), textvariable = gender, width = 19)
                     Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)




                     #========================================================Buttons of Frame_3=========================================================
                     btnSave = Button(Frame_3, text = 'SAVE', font = ('arial',17,'bold'), width = 8, command = Add)
                     btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     btnDisplay = Button(Frame_3, text = 'DISPLAY', font = ('arial',17,'bold'), width = 8, command = Display)
                     btnDisplay.grid(row = 0, column = 1, padx = 10, pady = 10)
                     btnReset = Button(Frame_3, text = 'RESET', font = ('arial',17,'bold'), width = 8, command = Reset)
                     btnReset.grid(row = 0, column = 2, padx = 10, pady = 10)
                     btnUpdate = Button(Frame_3, text = 'UPDATE', font = ('arial',17,'bold'), width = 8, command = Update)
                     btnUpdate.grid(row = 0, column = 3, padx = 10, pady = 10)
                     btnDelete = Button(Frame_3, text = 'DELETE', font = ('arial',17,'bold'), width = 8, command = Delete)
                     btnDelete.grid(row = 0, column = 4, padx = 10, pady = 10)
                     btnSearch = Button(Frame_3, text = 'SEARCH', font = ('arial',17,'bold'), width = 8, command = Search )
                     btnSearch.grid(row = 0, column = 5, padx = 10, pady = 10)
                     btnExit = Button(Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
                     btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)



                     #===============================================List Box and scrollbar========================================================
                     scrollbar = Scrollbar(Frame_2)
                     scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                     listbox = Listbox(Frame_2, width = 75, height = 20 , font = ('arial',12,'bold'))
                     listbox.bind('<<ListboxSelect>>', StudentRec)
                     listbox.grid(row = 0, column = 0)
                     scrollbar.config(command = listbox.yview)
if __name__=='__main__':
       information()
