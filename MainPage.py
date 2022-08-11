import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBooks import *
from ViewBooks import *
from issueBook import *
from ReturnBooks import *

def main():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # background Color
    Canvas1 = Canvas(root)
    Canvas1.config(bg="darksalmon")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="darksalmon", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n Lambton Library", bg='gold', fg='black',
                        font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Issue Book ", bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

    root.mainloop()


if __name__ == "__main__":
    main()