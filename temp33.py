def get_salary(employee):
    return employee["salary"]

def not_min_or_max(salary, min_salary, max_salary):
    return salary != min_salary and salary != max_salary

def avg_salary_excluding_min_max(employees):
    salaries = list(map(get_salary, employees))
    min_salary = min(salaries)
    max_salary = max(salaries)
    def salary_filter(salary):
        return not_min_or_max(salary, min_salary, max_salary)   
    middle_salary = list(filter(salary_filter,salaries))
    avg=sum(middle_salary)/len(middle_salary)
    return avg 

def not_min_or_max(salary, min_salary, max_salary):
    return salary != min_salary and salary != max_salary

def main():
    employees = [
        {"name": "A", "salary": 30000},
        {"name": "B", "salary": 50000},
        {"name": "C", "salary": 40000},
        {"name": "D", "salary": 60000}
    ]
    avg = avg_salary_excluding_min_max(employees)
    print(f"Average salary excluding min and max: {avg}")
    
if __name__ == "__main__":
    main()
