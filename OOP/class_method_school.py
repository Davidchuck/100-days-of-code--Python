#case 1 using university class
class school:
    #adding constructor
    def __init__(self, category,level, departments):
        self.category=category
        self.level=level
        self.departments=departments

        #method to return category
    def get_cat(self):
        return self.category
        
        #method to return level
    def get_level(self):
        return self.level
        
        #method to return departments
    def get_dept(self):
        return self.departments
school_cat=input("What type of a school did you school in? public or private: ")
school_level =input("What was your level? ")
school_department=input("Which department were you in ")
#creating an object to the method
myschool=school(school_cat, school_level, school_department)
print ("I schooled at a", myschool.get_cat(), myschool.get_level(),"school and was in ", myschool.get_dept(), "Department.")

    
