


class People:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))  

def get_employees():
    employees_list = []
    employees = {'Дима': 20000, 'Маша':18000, 'Олег': 34000}
    for employee in employees:
        emp = employee
        emp = People(employee, employees[employee])
        employees_list.append(emp)
    return employees_list
