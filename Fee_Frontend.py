from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import Fee_Backend
import Library_Frontend
import Marksheet_Frontend
import Main_Menu
import Std_info_FrontEnd
import Search_Page
def fee():

                # ==================================================Functions=================================================
        def Tuple(event):
            try:
                global st
                index = list.curselection()[0]
                st = list.get(index)

                recpt_entry.delete(0, END)
                recpt_entry.insert(END, st[1])
                name_entry.delete(0, END)
                name_entry.insert(END, st[2])
                admsn_entry.delete(0, END)
                admsn_entry.insert(END, st[3])
                Date_entry.delete(0, END)
                Date_entry.insert(END, st[4])
                branch_entry.delete(0, END)
                branch_entry.insert(END, st[5])
                sem_entry.delete(0, END)
                sem_entry.insert(END, st[6])
                total_entry.delete(0, END)
                total_entry.insert(END, st[7])
                paid_entry.delete(0, END)
                paid_entry.insert(END, st[8])
                due_entry.delete(0, END)
                due_entry.insert(END, st[9])
            except IndexError:
                pass
        def calculate_due():
            try:
                x1 = total.get()
                x2 = paid.get()
                x3 = x1 - x2
                due.set(x3)
            except TclError:
                due.set(0)

        def Insert():
            if (len(admsn.get()) != 0):
                Fee_Backend.insert(recpt.get(), name.get(), admsn.get(), date.get(),
                                   branch.get(), sem.get(), total.get(), paid.get(),
                                   due.get())
                list.delete(0, END)
                list.insert(END, (recpt.get(), name.get(), admsn.get(), date.get(),
                                       branch.get(), sem.get(), total.get(), paid.get(),
                                       due.get()))

        def View():
            list.delete(0, END)
            for row in Fee_Backend.view():
                list.insert(END, row, str(' '))

        def Reset():
            recpt.set(' ')
            name.set(' ')
            admsn.set(' ')
            #date.set(' ')
            branch.set(' ')
            sem.set(' ')
            paid.set(' ')
            due.set(' ')
            Display.delete('1.0', END)
            list.delete(0, END)

        def Delete():
            Fee_Backend.delete(st[0])
            Reset()
            View()

        def Receipt():
            Display.delete('1.0', END)
            Display.insert(END, '\t\tRECEIPT' + '\n\n')
            Display.insert(
                END, '\tReceipt No.\t     :' + recpt.get() + '\n')
            Display.insert(END, '\tStudent Name  :' +
                                name.get() + '\n')
            Display.insert(END, '\tAdmission No.\t:' +
                                admsn.get() + '\n')
            Display.insert(
                END, '\tDate\t          :' + date.get() + '\n')
            Display.insert(
                END, '\tBranch\t          :' + branch.get() + '\n')
            Display.insert(
                END, '\tSemester \t        :' + sem.get() + '\n\n')

            x1 = (var_1.get())
            x2 = (paid.get())
            x3 = (x1 - x2)

            Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
            Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
            Display.insert(END, '\tBalance\t         :' + str(x3) + '\n')

            due.set(x3)

        def Search():
            list.delete(0, END)
            for row in Fee_Backend.search(recpt.get(), name.get(), admsn.get(), date.get(),
                                          branch.get(), sem.get(), total.get(), paid.get(),
                                          due.get()):
                list.insert(END, row, str(' '))

        def Update():
            Fee_Backend.delete(st[0])
            Insert()

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                master.destroy()
                return

        def home():
            Main_Menu.menu()
        def information():
            Std_info_FrontEnd.information()
        def library():
            Library_Frontend.library()
        def mark():
            Marksheet_Frontend.marksheet()
        def search():
              Search_Page.main()  
        def close():
            master.destroy()
            Main_Menu.menu()
        master =Tk()
        master.title('Fee Report')
        master.geometry('1350x750')
        master.config(bg='Navajo white')
        master.resizable(0,0)
        #___________________________Menu_________________________
        menubar = Menu(master)

        homemenu = Menu(menubar, tearoff=0)
        homemenu.add_command(label="Home",command=home)
        homemenu.add_separator()

        librarymenu=Menu(menubar,tearoff=0)
        librarymenu.add_command(label="Library",command=library)
        librarymenu.add_separator()

        infomenu=Menu(menubar,tearoff=0)
        infomenu.add_command(label="Info",command=information)
        infomenu.add_separator()

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
        menubar.add_cascade(label="Information",menu=infomenu)
        menubar.add_cascade(label="Mark",menu=markmenu)
        menubar.add_cascade(label="Search",menu=searchmenu)
        menubar.add_cascade(label="Close",menu=closemenu)
        master.config(menu=menubar)

        # ==================================================Variables=================================================
        recpt = StringVar()
        name = StringVar()
        admsn = StringVar()
        date = StringVar()
        branch = StringVar()
        sem = StringVar()
        total = DoubleVar()
        paid = DoubleVar()
        due = DoubleVar()


        # ==================================================Frames===================================================
        Main_Frame = Frame(master, bg='Navajo white')
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1350, height=100, bg='Navajo white', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',
                              bg='navajowhite', padx=13)
        lblTitle.grid(padx=400)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,
                           bg='Navajo white', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Informations', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Fee Receipt', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,
                           bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,
                             bg='Navajo white', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        recpt_label = Label(Frame_1, text='Receipt No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        name_label = Label(Frame_1, text='Student Name : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        name_label.grid(row=1, column=0, padx=15, sticky=W)

        admsn_label = Label(Frame_1, text='Admission No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        admsn_label.grid(row=2, column=0, padx=15, sticky=W)

        Date_label = Label(Frame_1, text='Date : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        Date_label.grid(row=3, column=0, padx=15, sticky=W)

        branch_label = Label(Frame_1, text='Branch : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        branch_label.grid(row=4, column=0, padx=15, sticky=W)

        sem_label = Label(Frame_1, text='Semester : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        sem_label.grid(row=5, column=0, padx=15, sticky=W)

        total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        total_label.grid(row=2, column=2, padx=5, sticky=W)

        paid_label = Label(Frame_1, text='PAID AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        paid_label.grid(row=3, column=2, padx=5, sticky=W)

        due_label = Label(Frame_1, text='BALANCE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        due_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        var_1 = DoubleVar(Frame_1, value='36265')
        d1 = datetime.date.today()
        date.set(d1)

        recpt_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=recpt)
        recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=name)
        name_entry.grid(row=1, column=1, padx=15, pady=5)

        admsn_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=admsn)
        admsn_entry.grid(row=2, column=1, padx=15, pady=5)

        Date_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=date)
        Date_entry.grid(row=3, column=1, padx=15, pady=5)

        branch_entry = ttk.Combobox(Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical', 'Civil', 'EE', 'EEE'),
                                         font=('arial', 14), width=19, textvariable=branch)
        branch_entry.grid(row=4, column=1, padx=15, pady=5)

        sem_entry = ttk.Combobox(Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH',
                                                       'SEVENTH', 'EIGHTH'), font=('arial', 14), width=19,
                                      textvariable=sem)
        sem_entry.grid(row=5, column=1, padx=15, pady=5)

        total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=var_1, state='readonly')
        total_entry.grid(row=2, column=3, padx=8, pady=5)

        paid_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=paid)
        paid_entry.grid(row=3, column=3, pady=5)

        due_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=due)
        due_entry.grid(row=4, column=3, pady=7)

        # ==================================================Frame_2=================================================
        Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        Display.grid(row=0, column=0, padx=3)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        list = Listbox(List_Frame, font=(
            'arial', 13, 'bold'), width=140, height=8)
        list.bind('<<ListboxSelect>>', Tuple)
        list.grid(row=0, column=0)
        sb.config(command=list.yview)

        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)
        master.mainloop()

if __name__=='__main__':
    fee()
