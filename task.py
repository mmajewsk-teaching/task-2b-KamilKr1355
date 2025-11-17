class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []
        self.attendance = {"attended" : 0,"not_attended": 0}
    
    def give_grade(self,grade):
        if grade >=1 and grade <=6:
            self.grades.append(grade) 
        else:
            return
        
    def average_grades(self):
        return sum(self.grades)/len(self.grades)
    
    def is_present(self,present):
        if present:
            self.attendance["attended"]+=1
        self.attendance["not_attended"]+=1

    def attendance_percentage(self):
        return str(self.attendance["attended"]/(self.attendance["attended"]+self.attendance["not_attended"])*100)+"%"
    
class Highschool_class:
    def __init__(self,name):
        self.name = name
        self.students = []  

    def add_student(self,student):
        self.students.append(student)

    def get_average_grade(self):
        summed = 0

        for s in self.students:
            summed+=sum(s.grades)/len(s.grades)
        
        return summed/len(self.students)


if __name__ == "__main__":

    student1 = Student("Kamil","Krawiec")
    student1.give_grade(3)
    student1.give_grade(6)

    student2 = Student("Grzegorz","Brzęczyszczykiewicz")
    student2.give_grade(1)
    student2.give_grade(3)

    student1.is_present(True)
    student1.is_present(False)

    class1 = Highschool_class("4b")
    class1.add_student(student1)
    class1.add_student(student2)
    
    print("Average grade: ",class1.get_average_grade())

    print("Student1 average grade: ",student1.average_grades())

    print("Attendance: ",student1.attendance_percentage())
    
