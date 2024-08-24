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
        super.__init__(name, id)
        self.__monthlySalary = monthlySalary
        self.__bonus = 0
        self.__deduction = 0
        
    def calculateSalary(self):
        return self.__monthlySalary + self.__bonus - self.__deductions
    
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
        return self.__monthlySalary + self.__bonus - self.__deductions
    
    def calculateBonus(self):
        return self.__bonus
    
    def calculateDeductions(self):
        return self.__deduction
    
    def setDeduction(self, deduction):
        self.__deduction = deduction
        
    def setBonus(self, bonus):
        self.__bonus = bonus