import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.InputMismatchException;

abstract class Employee {
    private String name;
    private int id;

    public Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public abstract double calculateSalary();
    public abstract double calculateBonus();
    public abstract double calculateDeductions();

    @Override
    public String toString() {
        return "Employee [name=" + name + ", id=" + id + ", salary=" + calculateSalary() + "]";
    }
}

class FullTimeEmployee extends Employee {
    private double monthlySalary;
    private double bonus;
    private double deductions;

    public FullTimeEmployee(String name, int id, double monthlySalary) {
        super(name, id);
        this.monthlySalary = monthlySalary;
        this.bonus = 0;
        this.deductions = 0;
    }

    @Override
    public double calculateSalary() {
        return monthlySalary + bonus - deductions;
    }

    @Override
    public double calculateBonus() {
        return bonus;
    }

    @Override
    public double calculateDeductions() {
        return deductions;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public void setDeductions(double deductions) {
        this.deductions = deductions;
    }
}

class PartTimeEmployee extends Employee {
    private int hoursWorked;
    private double hourlyRate;
    private double bonus;
    private double deductions;

    public PartTimeEmployee(String name, int id, int hoursWorked, double hourlyRate) {
        super(name, id);
        this.hoursWorked = hoursWorked;
        this.hourlyRate = hourlyRate;
        this.bonus = 0;
        this.deductions = 0;
    }

    @Override
    public double calculateSalary() {
        return (hoursWorked * hourlyRate) + bonus - deductions;
    }

    @Override
    public double calculateBonus() {
        return bonus;
    }

    @Override
    public double calculateDeductions() {
        return deductions;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public void setDeductions(double deductions) {
        this.deductions = deductions;
    }
}

class PayrollSystem {
    private List<Employee> employeeList;

    public PayrollSystem() {
        employeeList = new ArrayList<>();
    }

    public void addEmployee(Employee employee) {
        employeeList.add(employee);
    }

    public void removeEmployee(int id) {
        Employee employeeToRemove = null;
        for (Employee employee : employeeList) {
            if (employee.getId() == id) {
                employeeToRemove = employee;
                break;
            }
        }
        if (employeeToRemove != null) {
            employeeList.remove(employeeToRemove);
        }
    }

    public void displayEmployees() {
        for (Employee employee : employeeList) {
            System.out.println("Employee: " + employee.getName());
            System.out.println("Salary: " + employee.calculateSalary());
            System.out.println("Bonus: " + employee.calculateBonus());
            System.out.println("Deductions: " + employee.calculateDeductions());
            System.out.println("---");
        }
    }
}

public class main {
    public static void main(String[] args) {
        PayrollSystem payrollSystem = new PayrollSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println(" ");
            System.out.print("\t***********************************************************\n");
            System.out.print("\t*            Please enter your choice for menu:           *\n");
            System.out.print("\t*                                                         *\n");
            System.out.print("\t*          |--------------------------------------|       *\n");
            System.out.print("\t*          | Enter 1 -> Add Employee              |       *\n");
            System.out.print("\t*          |--------------------------------------|       *\n");
            System.out.print("\t*          | Enter 2 -> Remove Employee           |       *\n");
            System.out.print("\t*          |--------------------------------------|       *\n");
            System.out.print("\t*          | Enter 3 -> Display Employees         |       *\n");
            System.out.print("\t*          |--------------------------------------|       *\n");
            System.out.print("\t*          | Enter 4 -> Exit                      |       *\n");
            System.out.print("\t*          |--------------------------------------|       *\n");
            System.out.print("\t*                                                         *\n");
            System.out.print("\t***********************************************************\n");

            System.out.print("Enter your choice: ");

            try {
                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                    case 1:
                        System.out.print("Enter employee name: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter employee ID: ");
                        int id = scanner.nextInt();
                        System.out.print("Is this a Full-Time Employee (1) or Part-Time Employee (2): ");
                        int empType = scanner.nextInt();
                        if (empType == 1) {
                            System.out.print("Enter monthly salary: ");
                            double monthlySalary = scanner.nextDouble();
                            FullTimeEmployee fullTimeEmployee = new FullTimeEmployee(name, id, monthlySalary);
                            System.out.print("Enter bonus for " + fullTimeEmployee.getName() + ": ");
                            double bonus = scanner.nextDouble();
                            fullTimeEmployee.setBonus(bonus);
                            System.out.print("Enter deductions for " + fullTimeEmployee.getName() + ": ");
                            double deductions = scanner.nextDouble();
                            fullTimeEmployee.setDeductions(deductions);
                            payrollSystem.addEmployee(fullTimeEmployee);
                        } else if (empType == 2) {
                            System.out.print("Enter hours worked: ");
                            int hoursWorked = scanner.nextInt();
                            System.out.print("Enter hourly rate: ");
                            double hourlyRate = scanner.nextDouble();
                            PartTimeEmployee partTimeEmployee = new PartTimeEmployee(name, id, hoursWorked, hourlyRate);
                            System.out.print("Enter bonus for " + partTimeEmployee.getName() + ": ");
                            double bonus = scanner.nextDouble();
                            partTimeEmployee.setBonus(bonus);
                            System.out.print("Enter deductions for " + partTimeEmployee.getName() + ": ");
                            double deductions = scanner.nextDouble();
                            partTimeEmployee.setDeductions(deductions);
                            payrollSystem.addEmployee(partTimeEmployee);
                        }
                        break;
                    case 2:
                        System.out.print("Enter employee ID to remove: ");
                        int empIdToRemove = scanner.nextInt();
                        payrollSystem.removeEmployee(empIdToRemove);
                        break;
                    case 3:
                        System.out.println("Employee Details:");
                        payrollSystem.displayEmployees();
                        break;
                    case 4:
                        scanner.close();
                        System.exit(0);
                    default:
                        System.out.println("Invalid choice. Please select a valid option.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.nextLine();
            }
        }
    }
}