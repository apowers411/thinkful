

meal = 44.50
tax = 0.0675
tip = 0.15

tax_value=meal*tax
meal_with_tax=meal+tax_value
tip_value=meal*tip
total=meal_with_tax+tip_value

print("%.2f" % meal)
print("%.2f" % tax_value)
print("%.2f" % tip_value)
print("%.2f" % total)

