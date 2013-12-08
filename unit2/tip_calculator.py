import sys
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    total = total)
    return meal_info
 
 
def main(argv=sys.argv):
#sys.arg to get the values for meal base cost, tip percentage, and tax percentage.
    meal=sys.argv[1]
    tip=sys.argv[2]
    tax=sys.argv[3]
    try:
        meal=float(meal)
    except ValueError:
	print ("You entered a string")
        meal=float(raw_input("Please enter meal cost:"))
    except:
        print "unexpected error:", sys.exc_info()[0]
    try:
        tip=float(tip)
    except ValueError:
        print ("You entered a string")
        tip=float(raw_input("Please enter tip cost:"))
    except:
        print "unexpected error:", sys.exc_info()[0]
    try:
        tax=float(tax)
    except ValueError:
        print ("You entered a string")
        tax=float(raw_input("Please enter tax cost:"))
    except:
        print "unexpected error:", sys.exc_info()[0]

    meal_info = calculate_meal_costs(meal, tax, tip)
 
    print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(int(100*meal_info['tip_rate']), meal_info['tax_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])
 
if __name__ == '__main__':
    main()
