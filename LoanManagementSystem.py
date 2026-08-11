class Loan:
    def __init__(self, loan_id, customer_name, loan_type, amount, rate, tenure_months): 
        self.loan_id = loan_id
        self.customer_name = customer_name
        self.loan_type = loan_type
        self.amount = amount
        self.rate = rate
        self.tenure_months = tenure_months
        self.emi = 0
        self.total_interest = 0
        self.total_amount = 0
        self.status = "Active"
        self.calculate_emi()
    
    def calculate_emi(self):
        """Calculate EMI using formula: E = P * r * (1+r)^n / ((1+r)^n - 1)"""
        if self.rate == 0:
            self.emi = self.amount / self.tenure_months
        else:
            monthly_rate = self.rate / (12 * 100)
            self.emi = self.amount * monthly_rate * ((1 + monthly_rate) ** self.tenure_months) / (((1 + monthly_rate) ** self.tenure_months) - 1)
        
        self.total_amount = self.emi * self.tenure_months
        self.total_interest = self.total_amount - self.amount
    
    def display(self):
        print("=======================")
        print("LOAN DETAILS")
        print("=======================")
        print("Loan ID:", self.loan_id)
        print("Customer Name:", self.customer_name)
        print("Loan Type:", self.loan_type)
        print("Loan Amount:", self.amount)
        print("Interest Rate:", self.rate, "%")
        print("Tenure (Months):", self.tenure_months)
        print("Monthly EMI:", round(self.emi, 2))
        print("Total Interest:", round(self.total_interest, 2))
        print("Total Amount:", round(self.total_amount, 2))
        print("Status:", self.status)
        print("=======================")

    def update_status(self, new_status):
        old_status = self.status
        self.status = new_status
        print(f"Status updated from {old_status} to {new_status}")

    def calculate_outstanding(self, months_paid):
        outstanding = self.total_amount - (self.emi * months_paid)
        if outstanding < 0:
            outstanding = 0
        print("Outstanding Amount:", round(outstanding, 2))
        return outstanding

    def prepayment(self, amount):
        if amount > 0:
            self.amount -= amount
            self.calculate_emi()
            print(f"Prepayment of {amount} accepted. New EMI recalculated.")
        else:
            print("Invalid prepayment amount")

    def show_loan_summary(self):
        print("\n")
        print("LOAN SUMMARY")
        print("=========================")
        print("Customer:", self.customer_name)
        print("Loan ID:", self.loan_id)
        print("Loan Type:", self.loan_type)
        print("Principal Amount:", self.amount)
        print("Interest Rate:", self.rate, "%")
        print("Tenure:", self.tenure_months, "months")
        print("Monthly EMI:", round(self.emi, 2))
        print("Total Interest:", round(self.total_interest, 2))
        print("Total Payable:", round(self.total_amount, 2))
        print("Status:", self.status)
        print("=========================")

    def get_emi(self):
        return self.emi

    def get_total_amount(self):
        return self.total_amount


loans = []

def add_loan(): 
    print("Add New Loan") 
    loan_id = int(input("Enter Loan ID: ")) 
    customer_name = input("Enter Customer Name: ") 
    loan_type = input("Enter Loan Type (Home/Personal/Education/Car): ") 
    amount = float(input("Enter Loan Amount: ")) 
    rate = float(input("Enter Annual Interest Rate (%): "))
    tenure_months = int(input("Enter Tenure (Months): "))
    loan = Loan(loan_id, customer_name, loan_type, amount, rate, tenure_months) 
    loans.append(loan) 
    print("Loan Added Successfully")

def view_loans():
    if len(loans) == 0:
        print("No Loans Found")
        return
    for loan in loans:
        loan.display()

def search_loan():
    loan_id = int(input("Enter Loan ID: ")) 
    for loan in loans:
        if loan.loan_id == loan_id:
            loan.display()
            return loan
    print("Loan not found")
    return None

def remove_loan(): 
    loan_id = int(input("Enter Loan ID: ")) 
    for loan in loans:
        if loan.loan_id == loan_id:
            loans.remove(loan) 
            print("Loan removed successfully") 
            return
    print("Loan not found")

def update_loan_status():
    loan = search_loan()
    if loan:
        new_status = input("Enter new status (Active/Closed): ")
        loan.update_status(new_status)

def calculate_outstanding():
    loan = search_loan()
    if loan:
        months = int(input("Enter number of months paid: "))
        loan.calculate_outstanding(months)

def prepayment():
    loan = search_loan()
    if loan:
        amount = float(input("Enter prepayment amount: "))
        loan.prepayment(amount)

def show_loan_summary():
    loan = search_loan()
    if loan:
        loan.show_loan_summary()

def get_emi():
    loan = search_loan()
    if loan:
        print("Monthly EMI:", round(loan.get_emi(), 2))

def get_total_amount():
    loan = search_loan()
    if loan:
        print("Total Amount Payable:", round(loan.get_total_amount(), 2))

def emi_calculator():
    print("\nEMI CALCULATOR")
    print("=========================")
    amount = float(input("Enter Loan Amount: "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    tenure = int(input("Enter Tenure (Months): "))
    
    if rate == 0:
        emi = amount / tenure
    else:
        monthly_rate = rate / (12 * 100)
        emi = amount * monthly_rate * ((1 + monthly_rate) ** tenure) / (((1 + monthly_rate) ** tenure) - 1)
    
    total_amount = emi * tenure
    total_interest = total_amount - amount
    
    print("\nCALCULATION RESULTS")
    print("=========================")
    print("Loan Amount:", amount)
    print("Interest Rate:", rate, "%")
    print("Tenure:", tenure, "months")
    print("Monthly EMI:", round(emi, 2))
    print("Total Interest:", round(total_interest, 2))
    print("Total Amount:", round(total_amount, 2))
    print("=========================")


while True:
    print("\n")
    print("================================")
    print("LOAN MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Loan")
    print("2. View All Loans")
    print("3. Search Loan")
    print("4. Remove Loan")
    print("5. Update Loan Status")
    print("6. Calculate Outstanding Amount")
    print("7. Prepayment")
    print("8. Show Loan Summary")
    print("9. Get Monthly EMI")
    print("10. Get Total Amount")
    print("11. EMI Calculator")
    print("12. Exit")

    choice = int(input("Enter choice: ")) 
    if choice == 1:
        add_loan()
    elif choice == 2:
        view_loans() 
    elif choice == 3:
        search_loan()
    elif choice == 4:
        remove_loan()
    elif choice == 5:
        update_loan_status()
    elif choice == 6:
        calculate_outstanding()
    elif choice == 7:
        prepayment()
    elif choice == 8:
        show_loan_summary()
    elif choice == 9:
        get_emi()
    elif choice == 10:
        get_total_amount()
    elif choice == 11:
        emi_calculator()
    elif choice == 12:
        print("Thank you for using Loan Management System!")
        break
    else:
        print("Invalid choice")
    



