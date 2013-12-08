class DiscountCalculator(object):
    def calculate(self, total, discount_amount,discount_type):
         if discount_type=="percent":
             discount=float(total)*float(discount_amount)/100
            
         elif discount_type == 'absolute': 
             discount=discount_amount
         else: 
             raise ValueError("Invalid discount type")
         return discount
