from tkinter import *
from Book import *


class Main:

    #main() method for GUI
    def main():
        root = Tk()
        root.title("Library Management")
        root.minsize(width=500,height=500)
        root.geometry("800x600")

        # setting the background Color
        Canvas1 = Canvas(root)
        Canvas1.config(bg="darksalmon")
        Canvas1.pack(expand=True, fill=BOTH)

        #Using frame( ) to create headframe
        headingFrame1 = Frame(root, bg="darksalmon", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

        #creating label to provide heading
        headingLabel = Label(headingFrame1, text="Welcome to \n Lambton Library", fg='black',
                            font=('CourierBold', 25))

        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)  # to set the positioning of label

        #creating buttons and using place() to set the positioning of buttons on the plot
        btn1 = Button(root, text="Book List", bg='black', fg='white',font=('bold', 15) , command=Book.AllBookList.view)
        btn1.place(relx=0.15, rely=0.3, relwidth=0.45, relheight=0.09)

        btn2 = Button(root, text="Add  New  Book", bg='black', fg='white' ,font=('bold', 15),command=Book.AddNewBook.addBook)
        btn2.place(relx=0.45, rely=0.4, relwidth=0.45, relheight=0.09)

        btn3 = Button(root, text="Delete  Book", bg='black', fg='white',font=('bold', 15), command=Book.BookDelete.delete)
        btn3.place(relx=0.15, rely=0.5, relwidth=0.45, relheight=0.09)

        btn4 = Button(root, text="Issue Book ", bg='black', fg='white',font=('bold', 15), command=Book.IssueBooks.issueBook)
        btn4.place(relx=0.45, rely=0.6, relwidth=0.45, relheight=0.09)

        btn5 = Button(root, text="Return Book", bg='black', fg='white',font=('bold', 15), command=Book.BookReturn.returnBook)
        btn5.place(relx=0.15, rely=0.7, relwidth=0.45, relheight=0.09)

        btn6 = Button(root, text="Graph 1", bg='black', fg='white',font=('bold', 15), command=Book.BarGraph.graph)
        btn6.place(relx=0.45, rely=0.8, relwidth=0.45, relheight=0.09)

        btn7 = Button(root, text="Graph 2", bg='black', fg='white',font=('bold', 15), command=Book.PieChart.piegraph)
        btn7.place(relx=0.15, rely=0.9, relwidth=0.45, relheight=0.09)
        
        root.mainloop() 
        

if __name__ == "__main__":
    Main.main()
