# Input values
monthly_investment = float(input("Enter monthly investment: "))
yearly_interest_rate = float(input("Enter yearly interest rate (as a percentage): "))
investment_years = int(input("Enter number of years: "))

if monthly_investment < 0:
    print("Error: Monthly investment cannot be negative.")
    monthly_investment = float(input("Enter monthly investment: "))

if yearly_interest_rate < 0:
    print("Error: Yearly interest rate cannot be negative.")
    yearly_interest_rate = float(input("Enter yearly interest rate (as a percentage): "))

if investment_years < 0:
    print("Error: Number of years cannot be negative.")
    investment_years = int(input("Enter number of years: "))

# Calculate each month's revenue
months = investment_years * 12 
monthly_interest_rate = yearly_interest_rate / 12 / 100

for month in range(1, months + 1):
    # Calculate the future value
    revenue = monthly_investment * (((1 + monthly_interest_rate) ** month - 1) / monthly_interest_rate)
    
    # Print the result
    print(f"Month {month} Revenue: ${revenue}")

# Print total revenue after x years
print("After", investment_years, "years, you will recieve a total investment") 
print(f"revenue of ${revenue:.2f} at a yearly rate of {yearly_interest_rate}%.")