import random
import json


class student:
    def __init__(self, fname, lname, ID, grade, classes: list):
        if classes is None:
            classes = []
        self.m_fname = fname
        self.m_lname = lname
        self.m_ID = ID
        self.m_grade = grade
        self.m_classes = classes
        self.m_homeRM = random.choice(self.m_classes)



def GetClasses(classes: list = None):
    if classes == None:
        _classes = []
        i = 0
        while i < 5:
            NewClass = input("New class: ")
            _classes.append(NewClass)
            i += 1
        return _classes
    else:
        return classes


def SerchForStudent(StudentFirstName: str, StudentLasttName: str, StudentID: int):
    """
    serches for the student record
    """
    f = open("./StudentDB.txt", "r")
    print("\033[92m\nFetching student info...\n\033[0m")
    for line in f:
        contents = json.loads(line)
        if contents["First Name"] == StudentFirstName and contents["Last Name"] == StudentLasttName and contents["ID Number"] == StudentID:
            Name = f'{contents["First Name"]} {contents["Last Name"]}'
            ID = f'{contents["ID Number"]}'
            Grade = f'{contents["Grade Level"]}'
            HomeRm = f'{contents["Home Room"]}'
            Classes = f'{contents["Classes"]}'

            return Name, ID, Grade, HomeRm, Classes
        else:
            continue
    f.close()


def SaveStudentInfo(_student):
    """
    Saves Information to a database
    """
    print("\033[92m\nSaving studen info...\033[0m")
    f = open("StudentDB.json", "a")
    appendInfo = {"First Name": _student.m_fname,
                  "Last Name": _student.m_lname,
                  "Home Room": _student.m_homeRM,
                  "ID Number": _student.m_ID,
                  "Grade Level": _student.m_grade,
                  "Classes": _student.m_classes
                  }
    append = json.dumps(appendInfo)
    f.write(f"{append}")
    f.write("\n")
    f.close()
    print("\033[92mSaved student to database\033[0m\n")


def CreateStudent():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    ID = int(input("ID #: "))
    grade = int(input("Grade: "))
    classes = GetClasses()

    newStudent = student(fname, lname, ID, grade, classes=classes)

    SaveStudentInfo(newStudent)

def ReturnAllData():
    f = open("StudentDB.json", "r")
    contents = ""
    for line in f:
        contents += f"{line}\n"
    return contents
    f.close()


def ModifyStudent(id= int, c_fn=None, c_ln=None, c_gl=None, c_hmr=None):
    f = open("StudentDB.json", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        line.strip("\n")
        contents = json.loads(line)
        print(contents)
        if contents["ID Number"] == id:

            if c_fn != None:
                contents["First Name"] = c_fn
            if c_ln != None:
                contents["Last Name"] = c_ln
            if c_gl != None:
                contents["Grade Level"] = c_gl
            if c_hmr != None:
                contents["Home Room"] = c_hmr
            lines.append(json.dumps(contents))
            info = lines
            del line
            break

    def reformat():
        f = open("StudentDB.json", "r")
        raw = f.readlines()
        f.close()

        for line in raw:
            if line == " " or line == "\n":
                del line
                continue
        print(raw)

    f = open("StudentDB.json", "w")
    i = 0
    for lines in info:
        i+=1
        print(lines, i)
        f.write(f"{lines}\n")
    f.close()
    reformat()
'''
run = True
while run:
    option = input("1) Create Student\n2) Search\n3) Quit\nChoice(1, 2, 3): ")
    if option == "1":
        CreateStudent()
    if option == "2":
        fn = str(input("Student First Name: "))
        ln = str(input("Student Last Name: "))
        id = int(input("Student ID: "))
        SerchForStudent(fn, ln, id)
    if option == "3":
        quit()
'''
ModifyStudent(47262, "J", "c", 2, "AB")