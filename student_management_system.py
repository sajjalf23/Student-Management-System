class Student:

    def __init__( self , id , name , age , gender , marks ):
        self.id = id
        self.name = name 
        self.age = age
        self.gender = gender
        self.marks = marks

    def display_student( self ):
        print("Name : " , self.name , " Id : " , self.id , " Age : " , self.age  , " Gender : " , self.gender , " Marks : " , self.marks )


class Student_Manager:

    def __init__(self):
        self.Student_List = []

    def add_student( self , id , name , age , gender , marks ):
        s1 = Student( id , name , age , gender , marks )
        self.Student_List.append(s1)
        print(name , " added successfully in the list .")
        self.addStudent_in_File(s1)

    def display_List( self ):
        for s in self.Student_List:
            s.display_student()
    
    def update_student(self , id , name = " " , age = -1 , gender = "N" , marks = -1):
        for s in self.Student_List:
            if( s.id == id ):
                if( name != " " ):
                    s.name = name
                if( age != -1 ):
                    s.age = Age
                if( gender != "N" ):
                    s.gender = gender
                if( marks != -1 ):
                    s.marks = marks
                print(" Student  Info Updated .")
                self.updateStudent_in_File()
                return
        print(" No Student with " , id , " is found .")
    

    def delete_Student( self , id ):
        for s in self.Student_List:
            if( s.id == id ):
                self.Student_List.remove(s)
                print("Student with " , id ," is removed .")
                self.updateStudent_in_File()
                return
        print(" No Student with " , id , " is found .")
            

    def search_student( self , id ):
        for s in self.Student_List:
            if(s.id == id ):
                print(" Student found ! ")
                s.display_student()
                return s
        print("Student not found !")

    def addStudent_in_File(self , s1 ):
        f = open("student_List.txt", "a")
        data = s1.name + " " + str(s1.id) + " " + str(s1.age ) + " " + s1.gender + " " + str(s1.marks)+"\n" 
        f.write(data)
        f.close()

    def updateStudent_in_File(self ):
        f = open("student_List.txt", "w")
        for s1 in self.Student_List:
            data = s1.name + " " + str(s1.id) + " " + str(s1.age ) + " " + s1.gender + " " + str(s1.marks) +"\n" 
            f.write(data)
        f.close()

    def read_STudent_File(self):
        f = open("student_List.txt", "r")
        data = f.read()
        print(data)
        f.close()
            

    def RUN(self):
        description = "1. Add Student \n 2. View Students \n 3. Update Student \n 4. Delete Student \n 5. Read from the TEXT REcord File \n 6. Exit \n "
        while(True):
            i = input(description)
            i = int(i)
            if(i == 1):
                ID = input( "Enter id : ")
                NAME = input("Enter name : " )
                AGE = input("Enter age : ")
                GENDER = input("Enter Gender : ")
                MARKS = input("Enter Marks : ")
                ID = int(ID)
                AGE = int(AGE)
                MARKS = int(MARKS)
                self.add_student( ID , NAME , AGE , GENDER , MARKS )
            if(i == 2):
                self.display_List()
            if(i == 3):
                ID = input("ENTER THE STUDENT ID WHOOSE CREDENTIALS U WANNNA CHANGE : ")
                NAME = " "
                AGE = -1
                GENDER = "N"
                MARKS = -1
                while(True):
                    print("Step by step enter the changes u wanna made ")
                    des = "1. Change Name  \n 2. Change age \n 3. Change Gender \n 4. Change MArks \n 5. DONE \n"
                    choose = input(des)
                    choose = int(choose)
                    if(choose == 1):
                        NAME = input("Enter name : " )
                    if(choose == 2): 
                        AGE = input("Enter age : ")
                        AGE = int(AGE)
                    if(choose == 3):
                       GENDER = input("Enter Gender : ")
                    if(choose == 4):
                       MARKS = input("Enter Marks : ")
                       MARKS = int(MARKS) 
                    if(choose == 5):
                        break
                self.update_student(ID , NAME , AGE , GENDER , MARKS)
            if(i == 4):
                print("Enter the id of the student u wanna delete")
                ID = input()
                ID = int(ID)
                self.delete_Student(ID)
            if(i == 6):
                break
            if(i == 5):
                self.read_STudent_File()



M1 = Student_Manager()
M1.RUN()
