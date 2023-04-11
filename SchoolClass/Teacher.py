class Teacher:
    def __init__(self,name,surname,profession):
        self.name=name
        self.surname=surname
        self.profession=profession
    def __str__(self): 
        return f"Teacher Name: {self.name}\nTeacher Surname:{self.surname}\nTeacher Profession:{self.profession}" 
        
        