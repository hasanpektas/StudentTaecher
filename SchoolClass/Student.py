class Student:
    def __init__(self,name,surname,studentid):
        self.name=name
        self.surname=surname
        self.studentid=studentid
    def __str__(self): 
        return f"Student Name: {self.name}\nStudent Surname:{self.surname}\nStudent ID:{self.studentid}"
