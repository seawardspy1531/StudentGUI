from tkinter import *
import student as s

win = Tk(className='Student GUI')
win.geometry("500x500")  # 500 by 500 pixels

WelcomeLable = Label(text="Welcome", font="Helvetica 16 bold italic")
WelcomeLable.pack()
welcomelblactive = True


def DestroyWelcome():
    welcomelblactive = False
    WelcomeLable.destroy()


def NewStudent():
    if welcomelblactive == True:
        DestroyWelcome()

    Title = Label(text='New Student', font="Helvetica 16 bold italic")
    Title.pack()

    fname = StringVar(value="First Name")
    lname = StringVar(value="Last Name")
    ID = IntVar(value=0)
    grade = IntVar(value=0)
    # classes = Variable(value=[])
    c1 = StringVar(value="class")
    c2 = StringVar(value="class")
    c3 = StringVar(value="class")
    c4 = StringVar(value="class")
    c5 = StringVar(value="class")

    fnamelbl = Label(text='Student First Name')
    fnameEntry = Entry(textvariable=fname)

    lnamelbl = Label(text='Student Last Name')
    lnameEntry = Entry(textvariable=lname)

    IDlbl = Label(text='Student ID')
    IDEntry = Entry(textvariable=ID)

    gradelbl = Label(text='Student Grade')
    gradeEntry = Entry(textvariable=grade)

    classlbl = Label(text='Classes')
    c1_ = Entry(textvariable=c1)
    c2_ = Entry(textvariable=c2)
    c3_ = Entry(textvariable=c3)
    c4_ = Entry(textvariable=c4)
    c5_ = Entry(textvariable=c5)

    fnamelbl.pack()
    fnameEntry.pack()
    lnamelbl.pack()
    lnameEntry.pack()
    IDlbl.pack()
    IDEntry.pack()
    gradelbl.pack()
    gradeEntry.pack()
    classlbl.pack()
    c1_.pack()
    c2_.pack()
    c3_.pack()
    c4_.pack()
    c5_.pack()

    def submit_clicked():
        fn = fname.get()
        ln = lname.get()
        id = ID.get()
        grd = grade.get()

        classes = [c1.get(), c2.get(), c3.get(), c4.get(), c5.get()]

        newStudent = s.student(fn, ln, id, grade=grd, classes=classes)
        s.SaveStudentInfo(newStudent)

        fnamelbl.destroy()
        fnameEntry.destroy()
        lnamelbl.destroy()
        lnameEntry.destroy()
        IDlbl.destroy()
        IDEntry.destroy()
        gradelbl.destroy()
        gradeEntry.destroy()
        classlbl.destroy()
        c1_.destroy()
        c2_.destroy()
        c3_.destroy()
        c4_.destroy()
        c5_.destroy()
        btn.destroy()
        Title.destroy()

        done = Label(text="Student Information Submitted")
        done.pack()
        done.after(1500, lambda: done.destroy())

    btn = Button(text='Submit', command=submit_clicked)
    btn.pack()


def Search():
    if welcomelblactive:
        DestroyWelcome()

    Title = Label(text='Search For Student', font="Helvetica 16 bold italic")
    Title.pack()

    Id = StringVar(value="Student ID")
    Fn = StringVar(value="Student First Name")
    Ln = StringVar(value="Student Last Name")

    searchlbl = Label(text="Search For Student")
    sID = Entry(textvariable=Id)
    sFn = Entry(textvariable=Fn)
    sLn = Entry(textvariable=Ln)

    def search_clicked():
        searchlbl.destroy()
        sID.destroy()
        sFn.destroy()
        sLn.destroy()
        searchbtn.destroy()
        Title.destroy()

        Name, ID, Grade, HomeRM, Classes = s.SerchForStudent(Fn.get(), Ln.get(), int(Id.get()))

        text = Text(bd=10)
        info = f"=== Student Information Dump ===\n" \
               f"Name: {Name}\n" \
               f"ID: {ID}\n" \
               f"Grade: {Grade}\n" \
               f"Home Room: {HomeRM}\n" \
               f"Classes: {Classes}\n" \
               f"==============================="
        text.insert(END, info)
        text.pack()

        def _done():
            done.destroy()
            text.destroy()

        done = Button(text="Done", command=_done)
        done.pack()

    searchbtn = Button(text="Search", command=search_clicked)

    searchlbl.pack()
    sID.pack()
    sFn.pack()
    sLn.pack()
    searchbtn.pack()


def ViewRawData():
    if welcomelblactive:
        DestroyWelcome()

    info = s.ReturnAllData()
    text = Text(bd=5, yscrollcommand=True, xscrollcommand=True)
    text.insert(END, info)

    def _done():
        text.destroy()
        btn.destroy()

    btn = Button(text="Done", command=_done)

    text.pack()
    btn.pack()



menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
Othermenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New Student", command=NewStudent)
filemenu.add_command(label="Search...", command=Search)
filemenu.add_command(label="Show All Data", command=ViewRawData)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)

Othermenu.add_command(label="Filler", command=win.quit)

menubar.add_cascade(label="Functions", menu=filemenu)
menubar.add_cascade(label="Other", menu=Othermenu)


win.config(menu=menubar)
win.mainloop()
