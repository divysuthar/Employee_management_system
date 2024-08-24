from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
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
        return f"Employee [name={self.__name}, id={self.__id}, salary={salary}]"
    
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthlySalary):
        super().__init__(name, id)
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
    def __init__(self, name, id, hoursWorked, hourlyRate):
        super().__init__(name, id)
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
        self.__employeeList = []
        
    def addEmployee(self, employee):
        self.__employeeList.append(employee)
    
    def removeEmployee(self, id):
        employee_to_remove = None
        for employee in self.__employeeList:
            if(employee.getId() == id):
                print(employee.getId())
                employee_to_remove = employee
                break
        if(employee_to_remove != None):
            self.__employeeList.remove(employee_to_remove)
        
    def displayEmployees(self):
        for employee in self.__employeeList:
            print(f"  Employee: {employee.getName()}")
            print(f"  Salary: {employee.calculateSalary()}")
            print(f"  Bonus: {employee.calculateBonus()}")
            print(f"  Deductions: {employee.calculateDeductions()}")
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
                id = input("Enter employee id: ")
                print("")
                try:
                    empType = int(input("Enter 1 for Full-Time Employee and 2 for Part-Time Employee: "))
                    if empType == 1:
                        monthlySalary = int(input("Enter monthly salary: "))
                        fulltimeEmployee = FullTimeEmployee(name, id, monthlySalary)
                        bonus = int(input(f"Enter bonus for {fulltimeEmployee.getName()}: "))
                        deduction = int(input(f"Enter deduction for {fulltimeEmployee.getName()}: "))
                        fulltimeEmployee.setBonus(bonus)
                        fulltimeEmployee.setDeduction(deduction)
                        payroll_system.addEmployee(fulltimeEmployee)
                    elif empType == 2:
                        hoursWorked = int(input("Enter hours worked: "))
                        hourlyRate = int(input("Enter hourly rate: "))
                        parttimeEmployee = PartTimeEmployee(name, id, hoursWorked, hourlyRate)
                        bonus = int(input(f"Enter bonus for {parttimeEmployee.getName()}: "))
                        deduction = int(input(f"Enter deduction for {parttimeEmployee.getName()}: "))
                        parttimeEmployee.setBonus(bonus)
                        parttimeEmployee.setDeduction(deduction)
                        payroll_system.addEmployee(parttimeEmployee)
                except ValueError:
                    print("Invalid Choice.")
            elif choice == 2:
                empIdToRemove = input("Enter employee ID to remove: ")
                payroll_system.removeEmployee(empIdToRemove)
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