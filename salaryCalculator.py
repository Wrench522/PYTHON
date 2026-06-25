# KLM Company Salary Calculator

# Input employee details
payroll_no = input("Enter Payroll Number: ")
name = input("Enter Employee Name: ")
gender = input("Enter Gender: ")
job_group = input("Enter Job Group (J/K/L/M): ").upper()
salary = float(input("Enter Basic Salary: "))

# Determine house allowance
if job_group == "J":
    allowance = 5000
elif job_group == "K":
    allowance = 5500
elif job_group == "L":
    allowance = 6000
elif job_group == "M":
    allowance = 6500
else:
    allowance = 0
    print("Invalid Job Group!")

# Calculate gross pay, taxes, and net pay
gross_pay = salary + allowance
taxes = 0.12 * salary
net_pay = gross_pay - taxes

# Display employee details
print("\n===== EMPLOYEE PAYSLIP =====")
print("Payroll Number:", payroll_no)
print("Name:", name)
print("Gender:", gender)
print("Job Group:", job_group)
print("Basic Salary:", salary)
print("House Allowance:", allowance)
print("Gross Pay:", gross_pay)
print("Taxes (12%):", taxes)
print("Net Pay:", net_pay)