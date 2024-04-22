def calculate_salary(days, employee):
    if days == 22:
        return employee.salary 
    elif days < 22:
        return employee.salary  * 0.7
    else:
        return employee.salary  * 1.3
    