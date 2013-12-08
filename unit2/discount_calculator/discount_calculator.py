class DiscountCalculator(object):
    def calculate(self, total, discount_amount,discount_type):
         if discount_type=="percent":
             if discount_amount>100:
                 raise ValueError("Percentage discount cannot exceed 100%)
             discount=float(total)*float(discount_amount)/100
         elif discount_type == 'absolute': 
             if discount_amount>total:
                raise ValueError("absolute discount cannot exceed order total")
             discount=discount_amount
         else: 
             raise ValueError("Invalid discount type")
         return discount
