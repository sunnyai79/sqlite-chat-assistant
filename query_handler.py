import re

# Function to process user queries and convert them into SQL statements
def process_query(user_input):
    user_input = user_input.lower()

    # 1. Show all employees in a department
    if "employees in the" in user_input and "department" in user_input:
        match = re.search(r"employees in the (\w+) department", user_input)
        if match:
            department = match.group(1).capitalize()
            return f"SELECT * FROM Employees WHERE Department = '{department}'"

    # 2. Find the manager of a department
    elif "manager of the" in user_input and "department" in user_input:
        match = re.search(r"manager of the (\w+) department", user_input)
        if match:
            department = match.group(1).capitalize()
            return f"SELECT Manager FROM Departments WHERE Name = '{department}'"

    # 3. List all departments
    elif "list all departments" in user_input:
        return "SELECT Name FROM Departments"

    # 4. Total salary expense for a department
    elif "total salary expense for the" in user_input:
        match = re.search(r"total salary expense for the (\w+) department", user_input)
        if match:
            department = match.group(1).capitalize()
            return f"SELECT SUM(Salary) AS Total_Salary FROM Employees WHERE Department = '{department}'"

    # 5. Employees earning more than a certain amount
    elif "employees earning more than" in user_input:
        match = re.search(r"employees earning more than (\d+)", user_input)
        if match:
            salary = match.group(1)
            return f"SELECT * FROM Employees WHERE Salary > {salary}"

    # 6. Employees earning less than a certain amount
    elif "employees earning less than" in user_input:
        match = re.search(r"employees earning less than (\d+)", user_input)
        if match:
            salary = match.group(1)
            return f"SELECT * FROM Employees WHERE Salary < {salary}"

    # 7. Average salary in a department
    elif "average salary in the" in user_input and "department" in user_input:
        match = re.search(r"average salary in the (\w+) department", user_input)
        if match:
            department = match.group(1).capitalize()
            return f"SELECT AVG(Salary) AS Average_Salary FROM Employees WHERE Department = '{department}'"

    # 8. Employees hired after a certain date
    elif "employees hired after" in user_input:
        match = re.search(r"employees hired after (\d{4}-\d{2}-\d{2})", user_input)
        if match:
            date = match.group(1)
            return f"SELECT * FROM Employees WHERE Hire_Date > '{date}'"

    # 9. Find the newest employee hired
    elif "newest employee" in user_input:
        return "SELECT Name, Department, Hire_Date FROM Employees ORDER BY Hire_Date DESC LIMIT 1"

    # 10. Find the oldest employee hired
    elif "oldest employee" in user_input:
        return "SELECT Name, Department, Hire_Date FROM Employees ORDER BY Hire_Date ASC LIMIT 1"

    # 11. Employees hired in a specific year
    elif "employees hired in" in user_input:
        match = re.search(r"employees hired in (\d{4})", user_input)
        if match:
            year = match.group(1)
            return f"SELECT * FROM Employees WHERE strftime('%Y', Hire_Date) = '{year}'"

    return None
