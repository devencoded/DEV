class Employee:
    def __init__(self, name, ID, department, job_title):
        self.__name = name
        self.__ID = ID
        self.__dept = department
        self.__job= job_title

    def set_department(self, department):
        self.__dept = department
    def set_job_title(self, job_title):
        self.__job = job_title
    def get_name(self):
        return self.__name
    def get_ID_number(self):
        return self.__ID
    def get_department(self):
        return self.__dept
    def get_job_title(self):
        return self.__job
    def __str__(self):
        return 'Name: ' + self.__name + '\n' +\
               'ID Number: ' + str(self.__ID) + '\n' +\
               'Department: ' + self.__dept + '\n' +\
               'Job Title: ' + self.__job

susan = Employee ('Susan Meyers', 47899, 'Accounting', 'Vice President')
mark = Employee('Mark Jones', 39119,'IT', 'Programmer')
joy = Employee('Joy Rogers' , 81774, 'Manufacturing', 'Engineer')
tick = Employee ('Dev', 99991,'Management', 'Analyst')

print(susan, end = '\n\n')
print(mark, end = '\n\n')
print(joy, end = '\n\n')
print(tick)

