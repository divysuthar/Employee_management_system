import sqlite3

class DatabaseHandler:
    def __init__(self, db_file='database.sqlite'):
        """Initialize the database connection."""
        self.__conn = sqlite3.connect(db_file)
        self.__cursor = self.__conn.cursor()
        self.__create_table()

    def __create_table(self):
        """Create a table for employees."""
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id TEXT PRIMARY KEY,
            name TEXT,
            type TEXT,
            monthly_salary REAL,
            hours_worked REAL,
            hourly_rate REAL,
            bonus REAL,
            deduction REAL
        )
        ''')
        self.__conn.commit()

    def add_employee(self, employee, FullTimeEmployee):
        """Add an employee to the database."""
        emp_data = {
            'id': employee.getId(),
            'name': employee.getName(),
            'type': 'FullTime' if isinstance(employee, FullTimeEmployee) else 'PartTime',
            'monthly_salary': getattr(employee, '_FullTimeEmployee__monthlySalary', None),
            'hours_worked': getattr(employee, '_PartTimeEmployee__hoursWorked', None),
            'hourly_rate': getattr(employee, '_PartTimeEmployee__hourlyRate', None),
            'bonus': employee.calculateBonus(),
            'deduction': employee.calculateDeductions()
        }
        sql = '''
        INSERT INTO employees (id, name, type, monthly_salary, hours_worked, hourly_rate, bonus, deduction)
        VALUES (:id, :name, :type, :monthly_salary, :hours_worked, :hourly_rate, :bonus, :deduction)
        ON CONFLICT(id) DO UPDATE SET
            name = excluded.name,
            type = excluded.type,
            monthly_salary = excluded.monthly_salary,
            hours_worked = excluded.hours_worked,
            hourly_rate = excluded.hourly_rate,
            bonus = excluded.bonus,
            deduction = excluded.deduction
        '''
        self.__cursor.execute(sql, emp_data)
        self.__conn.commit()

    def remove_employee(self, emp_id):
        """Remove an employee from the database."""
        self.__cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
        self.__conn.commit()

    def get_employees(self):
        """Fetch all employees from the database."""
        self.__cursor.execute('SELECT * FROM employees')
        return self.__cursor.fetchall()

    def __del__(self):
        """Close the database connection."""
        self.__cursor.close()
        self.__conn.close()
