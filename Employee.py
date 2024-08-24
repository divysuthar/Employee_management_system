from abc import ABC, abstractmethod
from database_management import DatabaseHandler

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.__name = name
        self.__emp_id = emp_id
        
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__emp_id
    
    @abstractmethod
    def calculateSalary(self):
        pass
    
    @abstractmethod
    def calculateBonus(self):
        pass
    
    @abstractmethod
    def calculateDeductions(self):
        pass
    
    def toString(self):
        salary = self.calculateSalary()
        return f"Employee [name={self.__name}, id={self.__emp_id}, salary={salary}]"
    
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthlySalary):
        super().__init__(name, emp_id)
        self.__monthlySalary = monthlySalary
        self.__bonus = 0
        self.__deduction = 0
        
    def calculateSalary(self):
        return self.__monthlySalary + self.__bonus - self.__deduction
    
    def calculateBonus(self):
        return self.__bonus
    
    def calculateDeductions(self):
        return self.__deduction
    
    def setDeduction(self, deduction):
        self.__deduction = deduction
        
    def setBonus(self, bonus):
        self.__bonus = bonus
        
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hoursWorked, hourlyRate):
        super().__init__(name, emp_id)
        self.__hoursWorked = hoursWorked
        self.__hourlyRate = hourlyRate
        self.__bonus = 0
        self.__deduction = 0
        
    def calculateSalary(self):
        return (self.__hoursWorked * self.__hourlyRate) + self.__bonus - self.__deduction
    
    def calculateBonus(self):
        return self.__bonus
    
    def calculateDeductions(self):
        return self.__deduction
    
    def setDeduction(self, deduction):
        self.__deduction = deduction
        
    def setBonus(self, bonus):
        self.__bonus = bonus
        
class PayrollSystem:
    def __init__(self):
        self.__sqlite_handler = DatabaseHandler()
        
    def addEmployee(self, employee):
        self.__sqlite_handler.add_employee(employee, FullTimeEmployee)
    
    def removeEmployee(self, emp_id):
        self.__sqlite_handler.remove_employee(emp_id)
        
    def displayEmployees(self):
        employees = self.__sqlite_handler.get_employees()
        for emp in employees:
            print(f"  Employee: {emp[1]}")
            print(f"  Salary: {emp[3] if emp[2] == 'FullTime' else (emp[4] * emp[5])}")
            print(f"  Bonus: {emp[6]}")
            print(f"  Deductions: {emp[7]}")
            print("")
            print("------------------------------")
        print("---------   End   ------------")
        
def main():
    payroll_system = PayrollSystem()
    
    while True:
        print("")
        print("      Please Enter your choice for menu  ")
        print("")
        print(" Enter 1 -> Add Employee")
        print(" Enter 2 -> Remove Employee")
        print(" Enter 3 -> Display Employee")
        print(" Enter 4 -> Exit")
        print("")
        
        try:
            choice = int(input("Enter your choice: "))
            print("")
            if choice == 1:
                name = input("Enter employee name: ")
                emp_id = input("Enter employee ID: ")
                print("")
                try:
                    empType = int(input("Enter 1 for Full-Time Employee and 2 for Part-Time Employee: "))
                    if empType == 1:
                        monthlySalary = int(input("Enter monthly salary: "))
                        fulltimeEmployee = FullTimeEmployee(name, emp_id, monthlySalary)
                        bonus = int(input(f"Enter bonus for {fulltimeEmployee.getName()}: "))
                        deduction = int(input(f"Enter deduction for {fulltimeEmployee.getName()}: "))
                        fulltimeEmployee.setBonus(bonus)
                        fulltimeEmployee.setDeduction(deduction)
                        payroll_system.addEmployee(fulltimeEmployee)
                    elif empType == 2:
                        hoursWorked = int(input("Enter hours worked: "))
                        hourlyRate = int(input("Enter hourly rate: "))
                        parttimeEmployee = PartTimeEmployee(name, emp_id, hoursWorked, hourlyRate)
                        bonus = int(input(f"Enter bonus for {parttimeEmployee.getName()}: "))
                        deduction = int(input(f"Enter deduction for {parttimeEmployee.getName()}: "))
                        parttimeEmployee.setBonus(bonus)
                        parttimeEmployee.setDeduction(deduction)
                        payroll_system.addEmployee(parttimeEmployee)
                except ValueError:
                    print("Invalid Choice.")
            elif choice == 2:
                emp_id_to_remove = input("Enter employee ID to remove: ")
                payroll_system.removeEmployee(emp_id_to_remove)
                print("")
            elif choice == 3:
                print("------  Employee List  ------")
                print("")
                payroll_system.displayEmployees()
                print("")
            elif choice == 4:
                break
            else:
                print("Invalid Choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
if __name__ == "__main__":
    main()