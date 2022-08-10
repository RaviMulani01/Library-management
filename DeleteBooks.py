import mysql.connector
from tkinter import *
import MySQLdb
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

my_database = mysql.connector.connect(
    host='127.0.0.1',
   user='root', password='root',
    port = '3307',
   database='pythonproject',
)
cur = my_database.cursor()
# Enter Table Names here

books = "books"  # Book Table


def deleteBook():
    book_id = bookInfo1.get()

    deleteSql = "delete from " +  books + " where book_id = '" + book_id + "'"
  
    try:
        cur.execute(deleteSql)
        my_database.commit()
     
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except MySQLdb.Error as ex:
        print(ex)
        messagebox.showinfo("Error", "Plase Check Book ID")
  

    print(book_id)

    bookInfo1.delete(0, END)
    root.destroy()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()