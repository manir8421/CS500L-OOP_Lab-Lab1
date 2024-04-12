# Python Lab (CS500L)/Week:01/Lab:01/Q:04
# 20099_MANIRUZZAMAN_MD
# A local bakery employs three bakers with varying hourly rates and overtime rules .....


# given data for Baker 1
rate_baker1 = 15.00
threshold_baker1 = 35

# given for Baker 2
rate_baker2 = 16.25
threshold_baker2 = 40

# given data for Baker 3
rate_baker3 = 17.75
threshold1_baker3 = 40
threshold2_baker3 = 45

# Input for hours worked by Baker 1
hours_baker1 = float(input("Enter hours worked by Baker 1:"))

# Input for hours worked by Baker 2
hours_baker2 = float(input("Enter hours worked by Baker 2:"))

# Input for hours worked by Baker 3
hours_baker3 = float(input("Enter hours worked by Baker 3:"))

# Calculate gross pay for Baker 1
if hours_baker1 <= threshold_baker1:
    gross_pay_baker1 = hours_baker1 * rate_baker1  # Regular hours pay
else:
    hours_baker1 > threshold_baker1
    gross_pay_baker1 = (threshold_baker1 * rate_baker1) + ((hours_baker1-threshold_baker1) * 1.5 * rate_baker1)   # Overtime pay

# Calculate gross pay for Baker 2
if hours_baker2 <= threshold_baker2:
    gross_pay_baker2 = hours_baker2 * rate_baker2  # Regular hours pay
else:
    hours_baker2 > threshold_baker2
    gross_pay_baker2 = (threshold_baker2 * rate_baker2) + ((hours_baker2-threshold_baker2) * 2 * rate_baker2)  # Double-time overtime pay

# Calculate gross pay for Baker 3
if hours_baker3 <= threshold1_baker3:
    gross_pay_baker3 = hours_baker3 * rate_baker3  # rerular pay
elif hours_baker3 > threshold1_baker3 and hours_baker3 <= threshold2_baker3:
    gross_pay_baker3 = (threshold1_baker3 * rate_baker3) + (rate_baker3 * 1.5 * (hours_baker3 - threshold1_baker3))   # rerular pay with 1.5 times
else:
    hours_baker3 > threshold2_baker3
    gross_pay_baker3 = (threshold1_baker3 * rate_baker3) + (rate_baker3 * 1.5 * (threshold2_baker3 - threshold1_baker3)) + (rate_baker3 * 2 * (hours_baker3 - threshold2_baker3))  # Double-time overtime pay

# Calculate taxes for Baker 1
tax = 0.30
taxes_baker1 = gross_pay_baker1 * tax

# Calculate taxes for Baker 2
tax = 0.30
taxes_baker2 = gross_pay_baker2 * tax

# Calculate taxes for Baker 3
tax = 0.30
taxes_baker3 = gross_pay_baker3 * tax

# Calculate net pay for Baker 1
net_pay_baker1 = gross_pay_baker1 - taxes_baker1

# Calculate net pay for Baker 2
net_pay_baker2 = gross_pay_baker2 - taxes_baker2

# Calculate net pay for Baker 3
net_pay_baker3 = gross_pay_baker3 - taxes_baker3

# Display results for Baker 1
print("\nPayment Details for Baker 1:")
print(f"Hours Worked: {hours_baker1}")
print(f"Gross Pay   : ${gross_pay_baker1:.2f}")
print(f"Taxes       : ${taxes_baker1:.2f}")
print(f"Net Pay     : ${net_pay_baker1:.2f}")

# Display results for Baker 2
print("\nPayment Details for Baker 2:")
print(f"Hours Worked: {hours_baker2}")
print(f"Gross Pay   : ${gross_pay_baker2:.2f}")
print(f"Taxes       : ${taxes_baker2:.2f}")
print(f"Net Pay     : ${net_pay_baker2:.2f}")

# Display results for Baker 3
print("\nPayment Details for Baker 3:")
print(f"Hours Worked: {hours_baker3}")
print(f"Gross Pay   : ${gross_pay_baker3:.2f}")
print(f"Taxes       : ${taxes_baker3:.2f}")
print(f"Net Pay     : ${net_pay_baker3:.2f}")