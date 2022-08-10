import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import MySQLdb

# Add your own database name and password here to reflect in the code
def getConnection():
    my_database = mysql.connector.connect(
        host='127.0.0.1',
        user='root', password='root',
        port = '3307',
        database='pythonproject',
    )
    return my_database

def closeConn(conn):
    conn.close()



# Enter Table Names here
book_issued = "book_issued"  # Issue Table
books = "books"  # Book Table

allBid = []  # List To store all Book IDs


def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    book_id = bookInfo1.get()
    con = getConnection()
    cur = con.cursor()
    extractbooks_id = "select book_id from " + book_issued
    try:
        cur.execute(extractbooks_id)
     
        for i in cur:
            allBid.append(i[0])

        if book_id in allBid:
            checkAvail = "select book_status from " + books + " where book_id = '" + book_id + "'"
            cur.execute(checkAvail)
           
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
            
    except MySQLdb.Error as ex:
        print(ex,"error")
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    issueSql = "delete from " + book_issued + " where book_id = '" + book_id + "'"

    print(book_id in allBid)
    print(status)
    updateStatus = "update " + books + " set book_status = 'avail' where book_id = '" + book_id + "'"
    try:
        if book_id in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return

    except MySQLdb.Error as ex:
        print(ex,"error")
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()
    closeConn(con)


def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
