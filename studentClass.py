class Student:

    def __init__(self, id, first_name, last_name, gpa, semester):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.semster = semester

    def set_id(self,value):
        self.id = value

    def set_first_name(self,value):
        self.first_name = value
    
    def set_last_name(self,value):
        self.last_name = value
    
    def set_gpa(self,value):
        self.gpa = value
    
    def set_semster(self,value):
        self.semster = value

    def get_id(self):
        return self.id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gpa(self):
        return self.gpa
    
    def get_semester(self):
        return self.semster
    
    def get_all_attributes(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.gpa} {self.semster}"