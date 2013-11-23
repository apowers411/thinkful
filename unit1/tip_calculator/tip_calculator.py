#! /usr/bin/env python
import sys
from optparse import OptionParser

mine=OptionParser()
mine.add_option("-m","--meal", dest="meal",help="meal cost",type="float")
mine.add_option("-x","--tax", dest="tax",help="tax cost",default=.12,type="float")
mine.add_option("-p","--tip", dest="tip",help="tip cost",type="float")

(options, args)=mine.parse_args()

if not (options.meal or options.tip):
    parser.error("You need to supple an argument for -tip or -meal ")

tax_value=options.meal*options.tax
meal_with_tax=options.meal+tax_value
tip_value=options.meal*options.tip
total=meal_with_tax+tip_value

print("This is the meal %.2f" % options.meal)
print("This is the tax value %.2f" % tax_value)
print("This is the tip_value %.2f" % tip_value)
print("This is the total %.2f" % total)

