# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to external Employee object

    def show_info(self):
        print(f"Department: {self.dept_name}")
        print(self.employee.get_details())

# Example usage
emp1 = Employee("Ayesha", 101)
dept1 = Department("Human Resources", emp1)

dept1.show_info()
