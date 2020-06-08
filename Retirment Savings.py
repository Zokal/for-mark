"""
Write a program that projects yearly income, amount saved towards retirement each year, and total retirement savings.
Assume a 3 percent raise on the starting income each year, and a 6% yearly return on investment.
You will need to ask the user their current age, at what age they want to retire, what their current income is,
what percent of their income they save each year, and how much they currently have in savings.
You will calculate how many years until retirement, and display the projected income, savings contribution,
and total savings each year.

 Hints: Assume they will enter a whole number for the percent of income saved
and divide it by 100 ( for 8 percent - 8/100 = .08).
Sample input with correct results is displayed below.
You will need to use the field size in the format settings to get everything to line up
nicely in table form.

Data:
age = int(input(“What is your current age?”))
retire = int(input(“What age do you want to retire?”))
salary = int(input(“What is your current income?”))
savings = int(input”What percentage of your income do you save each year?”))
now_savings = int(input(“How much money do you have in savings currently?”))

Processing:
Savings_percent = savings / 100
income = income * 1.03 # increasing salary by 3%
contribution = income * savings_percent
total_savings = total_savings * 1.06 # 6% rate of return
total_savings += contribution # money added in the year
"""
age = int(input("What is your current age? "))
retire = int(input("What age do you want to retire? "))
salary = int(input("What is your current income? "))
savings = int(input("What percentage of your income do you save each year? "))
total_savings = int(input("How much money do you have in savings currently? "))

savings_percent = savings / 100
years = 0
new_income = 0
contribution = 0

print("\n")

print("This projection assumes a 3% raise each year and a 6% yearly return on investment.\n")

print("Year\t\tIncome\t\tSavings Contribution\t\tTotal Savings")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for years in range(1, retire - age + 1):
    new_income += salary * 1.03
    contribution = salary * savings_percent
    total_savings = total_savings * 1.06
    total_savings += contribution
    print(years, '\t''\t', format(new_income, ',.0f'),'\t''\t''\t', format(contribution, ',.0f'),'\t''\t''\t''\t',
      format(total_savings, ',.0f'))



