from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sqlite3
import Main_Menu

def create_db():
    conn = sqlite3.connect("credentials.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def register_user(username, password):
    conn = sqlite3.connect("credentials.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password))
    conn.commit()
    conn.close()


def check_user(username, password):
    conn = sqlite3.connect("credentials.db")
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user


def main():
    def Login():
        u = (Username.get())
        p = (Password.get())
        if check_user(u, p):
            tkinter.messagebox.showinfo("Login", "Login Successful")
            Main_Menu.menu()
        else:
            tkinter.messagebox.askyesno("Login", "Error: Wrong Username or Password")
            Username.set("")
            Password.set("")

    def Reset():
        Username.set("")
        Password.set("")
        text_Username.focus()

    def Exit():
        if tkinter.messagebox.askokcancel("Login", "Confirm if you want to Exit"):
            master.destroy()

    def Register():
        reg_window = Toplevel(master)
        reg_window.title("Register")
        reg_window.geometry('400x300')
        reg_window.config(bg='lightskyblue')

        reg_username = StringVar()
        reg_password = StringVar()

        Label(reg_window, text="Register", font=('arial', 20, 'bold'), bg='lightskyblue').pack(pady=20)
        Label(reg_window, text="Username", font=('arial', 15), bg='lightskyblue').pack(pady=5)
        Entry(reg_window, textvariable=reg_username, font=('arial', 15)).pack(pady=5)
        Label(reg_window, text="Password", font=('arial', 15), bg='lightskyblue').pack(pady=5)
        Entry(reg_window, textvariable=reg_password, font=('arial', 15), show='*').pack(pady=5)
        Button(reg_window, text="Register", font=('arial', 15), command=lambda: register(reg_username.get(), reg_password.get())).pack(pady=20)

    def register(username, password):
        if username and password:
            try:
                register_user(username, password)
                tkinter.messagebox.showinfo("Register", "Registration Successful")
            except sqlite3.IntegrityError:
                tkinter.messagebox.showerror("Register", "Username already exists")
        else:
            tkinter.messagebox.showerror("Register", "All fields are required")

    master = Tk()
    master.title("Login Window")
    master.geometry('1350x750')
    master.config(bg='lightskyblue')
    frame = Frame(master, bg='lightskyblue')
    frame.pack()

    Username = StringVar()
    Password = StringVar()

    Lbl_Title = Label(frame, text='Login Menu', font=('arial', 55, 'bold'), bg='lightskyblue', fg='Black')
    Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

    Login_Frame_1 = LabelFrame(frame, width=1350, height=600, relief='ridge', bg='lightskyblue', bd=15,
                               font=('arial', 20, 'bold'))
    Login_Frame_1.grid(row=1, column=0)
    Login_Frame_2 = LabelFrame(frame, width=1000, height=600, relief='ridge', bg='lightskyblue', bd=15,
                               font=('arial', 20, 'bold'))
    Login_Frame_2.grid(row=2, column=0)

    Label_Username = Label(Login_Frame_1, text='Username', font=('arial', 20, 'bold'), bg='lightskyblue', bd=20)
    Label_Username.grid(row=0, column=0)
    text_Username = Entry(Login_Frame_1, font=('arial', 20, 'bold'), textvariable=Username)
    text_Username.grid(row=0, column=1, padx=50)

    Label_Password = Label(Login_Frame_1, text='Password', font=('arial', 20, 'bold'), bg='lightskyblue', bd=20)
    Label_Password.grid(row=1, column=0)
    text_Password = Entry(Login_Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=Password)
    text_Password.grid(row=1, column=1)

    btnLogin = Button(Login_Frame_2, text='Login', width=10, font=('arial', 15, 'bold'), command=Login)
    btnLogin.grid(row=3, column=0, padx=8, pady=20)

    btnReset = Button(Login_Frame_2, text='Reset', width=10, font=('arial', 15, 'bold'), command=Reset)
    btnReset.grid(row=3, column=1, padx=8, pady=20)

    btnExit = Button(Login_Frame_2, text='Exit', width=10, font=('arial', 15, 'bold'), command=Exit)
    btnExit.grid(row=3, column=2, padx=8, pady=20)

    btnRegister = Button(Login_Frame_2, text='Register', width=10, font=('arial', 15, 'bold'), command=Register)
    btnRegister.grid(row=3, column=3, padx=8, pady=20)

    master.mainloop()


if __name__ == '__main__':
    create_db()
    main()
    
