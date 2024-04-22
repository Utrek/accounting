from colorama import Fore, Back, Style
from datetime import datetime, date
from application.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    days = 24
    employees = get_employees()
    now = datetime.now()
    date_now = now.date()
    for employee in employees:
        salary = calculate_salary(days,employee.salary) 
        print(Fore.YELLOW)
        print(f'{date_now} {employee.name} зарплата: {salary}')
    