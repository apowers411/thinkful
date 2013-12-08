class DiscountCalculator(object):
    def calculate(self, total, discount_amount,discount_type):
         if discount_type=="percent":
             discount=total*discount_amount/100
             return discount

