import MySQLdb
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from Connection import *



class Book:

    class AllBookList():
    #defining function to create a window for books list
        def view():

            root = Tk()
            root.title("View All Book")
            root.minsize(width=400, height=400)
            root.geometry("600x500")

            Canvas1 = Canvas(root)
            Canvas1.config(bg="#88ccee")
            Canvas1.pack(expand=True, fill=BOTH)

            # Using frame( ) to create headframe
            headingFrame1 = Frame(root, bg="pink", bd=2)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

            # creating label to provide heading
            headingLabel = Label(headingFrame1, text="Books in the Library", bg='black', fg='white', font=('ArialBold', 15))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            labelFrame = Frame(root, bg='black')
            labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
            y = 0.25

             #creating frame to display the column headings
            Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('Book_Id', 'Title', 'Author', 'Status'), bg='black', fg='white').place(
                relx=0.02, rely=0.1)
            Label(labelFrame, text="----------------------------------------------------------------------------------", bg='black',
                  fg='white').place(relx=0.05, rely=0.2)

            #Connecting to the database
            try:
                my_database = Connection.getConn()
                cur = my_database.cursor()
                bookTable = "books"
                getBooks =  "select * from " + bookTable  #getting data from database
                cur.execute(getBooks)

                #Using For to get the display the stored data in database
                for i in cur:
                    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                        relx=0.02, rely=y)
                    y += 0.1

            except MySQLdb.Error as ex:
                print(ex,"Plase Try Again")

            #Closing database connection
            finally:
                Connection.closeConn(my_database)

            #creating Quit button
            quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
            quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

            root.mainloop()


    class AddNewBook():
        #defining function to add new book in the list
        def bookRegister():
            book_id = bookInfo1.get()
            title = bookInfo2.get()
            author = bookInfo3.get()
            status = bookInfo4.get()
          #to connect to the server
            con = Connection.getConn()

            #using try to add new book
            try:
                Insert_Query_6080 = """insert into books (
                book_id, book_title, book_author, book_status)
                VALUES('"""+book_id+"""', '"""+title+"""','"""+author+"""', '"""+status+"""')"""
                cur = con.cursor()
                cur.execute(Insert_Query_6080)

                con.commit()

                #if addition of new book succeed this message will popup
                messagebox.showinfo('Success', "Book added successfully")

            #if there is any error
            except MySQLdb.Error as ex:
                print(ex)
                messagebox.showinfo("Error", "Can't add data into Database")

            finally:
                Connection.closeConn(con)

            print(book_id)
            print(title)
            print(author)
            print(status)

            root.destroy()

        #defining addBook () method
        def addBook():
            global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

          #desiging window for new book information
            root = Tk()
            root.title("Add New Book In System")
            root.minsize(width=400, height=400)
            root.geometry("600x500")

            # Enter Table Names here
            books = "books"  # Book Table

            Canvas1 = Canvas(root)

            Canvas1.config(bg="#cc6677")
            Canvas1.pack(expand=True, fill=BOTH)

            #Using frame( ) to create headframe
            headingFrame1 = Frame(root, bg='skyblue', bd=2)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

            # creating label to provide heading
            headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('CourierBold', 20))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            labelFrame = Frame(root, bg='black')
            labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

            #label to enter book id
            lb1 = Label(labelFrame, text="Enter Book ID : ", bg='black', fg='white')
            lb1.place(relx=0.05, rely=0.2, relheight=0.15)

            bookInfo1 = Entry(labelFrame)
            bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.15)

            # label to enter title
            lb2 = Label(labelFrame, text="Title of the book: ", bg='black', fg='white')
            lb2.place(relx=0.05, rely=0.35, relheight=0.1)

            bookInfo2 = Entry(labelFrame)
            bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.15)

            #  label to enter Book Author
            lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
            lb3.place(relx=0.05, rely=0.50, relheight=0.15)

            bookInfo3 = Entry(labelFrame)
            bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.15)

            #  label to enter Book Status
            lb4 = Label(labelFrame, text="Status: \n (Avail/issued) ", bg='black', fg='white')
            lb4.place(relx=0.05, rely=0.65, relheight=0.15)

            bookInfo4 = Entry(labelFrame)
            bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.15)

            # creating Submit Button
            SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=Book.AddNewBook.bookRegister)
            SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

            #creating Quit Button
            quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
            quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

            root.mainloop()


    class BookDelete():
        #table name
        books = "books"  # Book Table

        #creating deleteBook() function to delete the book from the record
        def deleteBook():

            my_database = Connection.getConn()
            cur = my_database.cursor()
            book_id = bookInfo1.get()
            #deleting data from the database by refering the book id
            deleteSql = "delete from " +  Book.BookDelete.books + " where book_id = '" + book_id + "'"

           #using try and catch to handle exception
            try:
                cur.execute(deleteSql)
                my_database.commit()
                messagebox.showinfo('Success', "Book Record Deleted Successfully")
            except MySQLdb.Error as ex:
                print(ex)
                messagebox.showinfo("Error", "Plase Check Book ID")

            #Closing database connection
            finally:
                Connection.closeConn(my_database)
            print(book_id)

            bookInfo1.delete(0, END)
            root.destroy()

        #creating delete() method
        def delete():
            global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

        #Creting new window
            root = Tk()
            root.title("Delete Book From Library")
            root.minsize(width=400, height=400)
            root.geometry("600x500")

            Canvas1 = Canvas(root)

            Canvas1.config(bg="indianred")
            Canvas1.pack(expand=True, fill=BOTH)
            # Using frame( ) to create headframe
            headingFrame1 = Frame(root, bg="#FFBB00", bd=2)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
            # creating label to provide heading
            headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('ArialBold', 25))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            labelFrame = Frame(root, bg='black')
            labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

            # creating label Book ID to Delete
            lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('bold', 14))
            lb2.place(relx=0.05, rely=0.5)
            #text box to enter the book id
            bookInfo1 = Entry(labelFrame)
            bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.15)

            # Submit Button
            SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=Book.BookDelete.deleteBook)
            SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
             #quit button
            quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
            quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

            root.mainloop()


    class IssueBooks():

        # Enter Table Names here
        global books_issued
        books_issued = "book_issued"
        global books
        books = "books"

        # List To store all Book IDs
        allbook_id= []

        #defining the method issue() to issue the book from the book list
        def issue():
            global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status
        #using get() to get the information from the database table
            book_id = inf1.get()
            issueto = inf2.get()

            issueBtn.destroy()
            labelFrame.destroy()
            lb1.destroy()
            inf1.destroy()
            inf2.destroy()

            extractbook_id = "select book_id from " + books
            #connecting to database by calling connection method
            con = Connection.getConn()
            cur = con.cursor()

            #using try-except to handle any exception
            try:
                cur.execute(extractbook_id)
                for i in cur:
                    Book.IssueBooks.allbook_id.append(i[0])
                 #using if to check the book availability
                if book_id in Book.IssueBooks.allbook_id:
                    checkAvail = "select book_status from " + books + " where book_id = '" + book_id + "'"
                    cur.execute(checkAvail)
                    for i in cur :
                        checkAvail = i[0]

                    if checkAvail.lower() == 'available':
                        status = True
                    else:
                        status = False

                else:
                    messagebox.showinfo("Error", "Book ID not present")
            except MySQLdb.Error as ex:
                print(ex,"error")

            finally:
                Connection.closeConn(con)

            #inserting value into database table
            issueSql = "insert into " + books_issued + " values ('" + book_id + "','" + issueto + "')"
            show = "select * from " + books_issued

            updateStatus = "update " + books + " set book_status = 'issued' where book_id = '" + book_id+ "'"

            con = Connection.getConn()
            cur = con.cursor()
            # using try- except to handle any exception
            try:
                if book_id in Book.IssueBooks.allbook_id and status == True:
                    cur.execute(issueSql)
                    con.commit()
                    cur.execute(updateStatus)
                    con.commit()
                    messagebox.showinfo('Success', "Book Issued Successfully")
                    root.destroy()
                else:
                    Book.IssueBooks.allbook_id.clear()
                    messagebox.showinfo('Message', "Book Already Issued")
                    root.destroy()
                    return
            except MySQLdb.Error as ex:
                print(ex,"error")
                messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

            print(book_id)
            print(issueto)

            Book.IssueBooks.allbook_id.clear()

        #defining the issueBook () method
        def issueBook():
            global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

        #creating new window
            root = Tk()
            root.title("Issue Book")
            root.minsize(width=400, height=400)
            root.geometry("600x500")

            Canvas1 = Canvas(root)
            Canvas1.config(bg="#888888")
            Canvas1.pack(expand=True, fill=BOTH)

            # Using frame( ) to create headframe
            headingFrame1 = Frame(root, bg="#FFBB00", bd=2)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

            # creating label to provide heading
            headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('ArialBold', 25))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            labelFrame = Frame(root, bg='black')
            labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

            #label for  Book ID
            lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white',font=('bold',12))
            lb1.place(relx=0.05, rely=0.2)

            #text box for book id
            inf1 = Entry(labelFrame)
            inf1.place(relx=0.3, rely=0.2, relwidth=0.62,relheight=0.1)

            # label forIssued To Student name
            lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white',font=('bold',12))
            lb2.place(relx=0.05, rely=0.4)
            # text box for  Student name
            inf2 = Entry(labelFrame)
            inf2.place(relx=0.3, rely=0.4, relwidth=0.62,relheight=0.1)

            # Issue Button
            issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=Book.IssueBooks.issue)
            issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

           #quit button to close the window
            quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
            quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

            root.mainloop()


    class BookReturn():
        # Enter Table Names here
        book_issued = "book_issued"  # Issue Table

        books = "books"  # Book Table
        
        allBid = []  # List To store all Book IDs

        #using returnn() mwthod to get the book informationn and connnecting to addBook connection
        def returnn():
            global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status
            #using get() to get the book information

            book_id = bookInfo1.get()
            con = Connection.getConn()
            cur = con.cursor()

            extractbooks_id = "select book_id from " + Book.BookReturn.book_issued #getting all the data from book_issued table
            # using try- except to handle any exception
            try:
                cur.execute(extractbooks_id)

                for i in cur:
                    Book.BookReturn.allBid.append(i[0])
                # using if to check the book availability
                if book_id in Book.BookReturn.allBid:
                    checkAvail = "select book_status from " + Book.BookReturn.books + " where book_id = '" + book_id + "'"
                    cur.execute(checkAvail)

                    for i in cur:
                        checkAvail  = i[0]

                    if checkAvail  == 'issued':
                        status = True
                    else:
                        status = False

                else:
                    messagebox.showinfo("Error", "Book ID not present")
              #if there is any error
            except MySQLdb.Error as ex:
                print(ex,"error")
                messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

           
            #removing data from book_issued table in the databse
            issueSql = "delete from " + Book.BookReturn.book_issued + " where book_id = '" + book_id + "'"

            print(book_id in Book.BookReturn.allBid)
            print(status)
            #to update the books table
            updateStatus = "update " + Book.BookReturn.books + " set book_status = 'Available' where book_id = '" + book_id + "'"
            #to excute the data enter
            try:
                if book_id in Book.BookReturn.allBid and status == True:
                    cur.execute(issueSql)
                    con.commit()
                    cur.execute(updateStatus)
                    con.commit()
                    messagebox.showinfo('Success', "Book Returned Successfully")
                else:
                    Book.BookReturn.allBid.clear()
                    messagebox.showinfo('Message', "Please check the book ID")
                    root.destroy()
                    return

            except MySQLdb.Error as ex:
                print(ex,"error")
                messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

            #Closing database connection
            finally:
                Connection.closeConn(con)

            Book.BookReturn.allBid.clear()
            root.destroy()
            Connection.closeConn(con)

        #defining the returnBook method
        def returnBook():
            global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1
        #creating new window
            root = Tk()
            root.title("Return Book")
            root.minsize(width=400, height=400)
            root.geometry("600x500")

            Canvas1 = Canvas(root)

            Canvas1.config(bg="lightgreen")
            Canvas1.pack(expand=True, fill=BOTH)
            # Using frame( ) to create headframe
            headingFrame1 = Frame(root, bg="#FFBB00", bd=2)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
            # creating label to provide heading
            headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('ArialBold', 25))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            labelFrame = Frame(root, bg='black')
            labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

            # label for Book ID to Delete
            lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white',font=('bold',12))
            lb1.place(relx=0.05, rely=0.5)
            #text box to enter book id
            bookInfo1 = Entry(labelFrame)
            bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62,relheight=0.1)

            # Submit Button
            SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=Book.BookReturn.returnn)
            SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

            #quit button
            quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
            quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

            root.mainloop()


    class BarGraph():

        #Connecting to the database
        def graph():
            db_connection = Connection.getConn()
            db_cursor = db_connection.cursor()
            db_cursor.execute('SELECT book_status FROM books')

            a = 0
            b= 0
            total = 0
            # count total, available and issued book
            for i in db_cursor:
                if (i[0].lower() == 'available'):
                    a = a+1
                    total = total + 1
                elif ( i[0].lower() == 'issued'):
                    b = b+1
                    total = total + 1
            #to set the color of the title
            figure = plt.figure()
            ax = figure.add_subplot()
            ax.title.set_color('red')

            #data value for graph
            x = [1, 2, 3]
            y = [total, a, b]
            lable = ['Total', 'Available', 'Issued']

            #plotting the bar graph
            graph = plt.bar(x,y, tick_label = lable, color =['yellowgreen', 'lightcoral', 'skyblue'])

            # write graph height in top
            for bar in graph:
                y_values = bar.get_height()
                plt.text(bar.get_x()+bar.get_width()/2.0, y_values, int(y_values), va = 'bottom')

            #adding labels and title in the bar graph
            plt.xlabel("Books")
            plt.ylabel("Number of books")
            plt.title("Books in the library ")

            plt.show()

            Connection.closeConn(db_connection)


    class PieChart():

        def piegraph():
            db_connection = Connection.getConn()
            db_cursor = db_connection.cursor()  
            db_cursor.execute('SELECT book_status FROM books')

            a = 0
            b= 0
            total = 0

            # count total, available and issued book
            for i in db_cursor:

                if (i[0].lower() == 'available'):
                    a = a+1
                    total = total + 1

                elif ( i[0].lower() == 'issued'):
                    b = b+1
                    total = total + 1


            value = [a, b]
            lable = ['Available', 'Issued']

            plt.pie(value,  labels = lable,  autopct ='%1.1f%%', startangle = 140)

            plt.title('% of Available and Issued Book')
            plt.show()
            Connection.closeConn(db_connection)