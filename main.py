print("==========================================")
print("      CodeAlpha - Credit Scoring System")
print("==========================================")
print("Welcome to Smart Credit Score Checker")
print("")

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
loan_amount = int(input("Enter loan amount you want: "))
loan_months = int(input("Enter loan duration in months: "))
existing_loan = input("Do you have any existing loan? (yes/no): ").lower()
job_type = input("Enter your job type (salaried/business/student): ").lower()
late_payments = int(input("How many times did you pay late in last 12 months? : "))
bank_balance = int(input("Enter your current bank balance: "))

print("")
print("------------------------------------------")
print("Analyzing your details, please wait...")
print("------------------------------------------")

score = 300

if age >= 21 and age <= 60:
    score = score + 80
elif age > 60:
    score = score + 40
else:
    score = score + 10

if monthly_income >= 80000:
    score = score + 150
elif monthly_income >= 50000:
    score = score + 120
elif monthly_income >= 30000:
    score = score + 80
elif monthly_income >= 15000:
    score = score + 40
else:
    score = score + 10

savings = monthly_income - monthly_expenses

if savings >= 40000:
    score = score + 100
elif savings >= 20000:
    score = score + 70
elif savings >= 10000:
    score = score + 40
elif savings >= 0:
    score = score + 10
else:
    score = score - 30

if existing_loan == "no":
    score = score + 80
elif existing_loan == "yes":
    score = score + 20
else:
    score = score + 0

if job_type == "salaried":
    score = score + 70
elif job_type == "business":
    score = score + 50
elif job_type == "student":
    score = score + 10
else:
    score = score + 20

if late_payments == 0:
    score = score + 100
elif late_payments == 1:
    score = score + 50
elif late_payments == 2:
    score = score + 20
else:
    score = score - 50

if bank_balance >= 100000:
    score = score + 80
elif bank_balance >= 50000:
    score = score + 50
elif bank_balance >= 10000:
    score = score + 30
else:
    score = score + 5

if loan_amount <= monthly_income * 5:
    score = score + 60
elif loan_amount <= monthly_income * 10:
    score = score + 30
else:
    score = score - 20

if loan_months <= 12:
    score = score + 20
elif loan_months <= 36:
    score = score + 10
else:
    score = score + 0

if score > 850:
    score = 850
if score < 300:
    score = 300

if score >= 750:
    grade = "Excellent"
    status = "APPROVED"
    message = "Congratulations! Your loan can be easily approved."
    interest = "10% per year"
elif score >= 650:
    grade = "Good"
    status = "APPROVED"
    message = "Good! Your loan can be approved with normal interest."
    interest = "12% per year"
elif score >= 550:
    grade = "Average"
    status = "CONDITIONAL APPROVAL"
    message = "Your loan can be approved with some extra documents."
    interest = "15% per year"
elif score >= 450:
    grade = "Poor"
    status = "NEED REVIEW"
    message = "Your profile needs improvement. Please try with less loan amount."
    interest = "18% per year"
else:
    grade = "Very Poor"
    status = "REJECTED"
    message = "Sorry! Your loan is risky right now. Please improve your score."
    interest = "Not Applicable"

emi = 0
if loan_months > 0:
    emi = loan_amount // loan_months

print("")
print("==========================================")
print("           CREDIT SCORE REPORT")
print("==========================================")
print("Name:", name)
print("Age:", age)
print("Monthly Income:", monthly_income)
print("Monthly Expenses:", monthly_expenses)
print("Monthly Savings:", savings)
print("Job Type:", job_type)
print("Existing Loan:", existing_loan)
print("Late Payments:", late_payments)
print("Bank Balance:", bank_balance)
print("Requested Loan Amount:", loan_amount)
print("Loan Duration:", loan_months, "months")
print("Estimated Monthly EMI:", emi)
print("------------------------------------------")
print("Your Credit Score:", score, "/ 850")
print("Your Grade:", grade)
print("Loan Status:", status)
print("Interest Rate:", interest)
print("------------------------------------------")
print(message)
print("")
print("Tips to improve your score:")
print("1. Pay all bills on time")
print("2. Save more money every month")
print("3. Do not take many loans at same time")
print("4. Keep good bank balance")
print("==========================================")
print("Thank you for using CodeAlpha System")
print("==========================================")
