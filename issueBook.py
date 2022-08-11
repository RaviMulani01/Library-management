import mysql.connector
import MySQLdb
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox

from AddBook import getConnection

def getConn():
    my_database = mysql.connector.connect(
        host='127.0.0.1',
        user='root', password='root',
        port = '3307',
        database='pythonproject',
    )
    return my_database

def closeConn(con):
    con.close()

# Enter Table Names here
books_issued = "book_issued"
books = "books"

# List To store all Book IDs
allbook_id= []


def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    book_id = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractbook_id = "select book_id from " + books
    con = getConn()
    cur = con.cursor()
    try:
        cur.execute(extractbook_id)
        for i in cur :
            allbook_id.append(i[0])

        if book_id in allbook_id:
            checkAvail = "select book_status from " + books + " where book_id = '" + book_id + "'"
            cur.execute(checkAvail)
            for i in cur :
                check = i[0]

            if check.lower() == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except MySQLdb.Error as ex:
        print(ex,"error")

    finally:
        closeConn(con)

    issueSql = "insert into " + books_issued + " values ('" + book_id + "','" + issueto + "')"
    show = "select * from " + books_issued

    updateStatus = "update " + books + " set book_status = 'issued' where book_id = '" + book_id+ "'"
    
    con = getConn()
    cur = con.cursor()
    try:
        if book_id in allbook_id and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allbook_id.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except MySQLdb.Error as ex:
        print(ex,"error")
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    print(book_id)
    print(issueto)

    allbook_id.clear()


def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Issue Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#888888")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=2)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()