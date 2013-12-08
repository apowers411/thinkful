class DiscountCalculator(object):
    def calculate(self, total, discount_amount,discount_type):
         if discount_type=="percent":
             discount=float(total)*float(discount_amount)/100
             return discount
         if discount_type=='dollar':
             discount=total-discount_amount
             return discount
