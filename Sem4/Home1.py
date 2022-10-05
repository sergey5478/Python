# 1. Вычислить число c заданной точностью d
# in Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out 9.000000

from decimal import Decimal,ROUND_HALF_DOWN

number = input("Enter a real number: ")
accuracy = input ("Enter the required accuracy '0.0001'")

def Number(number,accuracy):
     number_accuracy = Decimal(number).quantize(Decimal(accuracy),\
         ROUND_HALF_DOWN)
     return number_accuracy
print (Number(number,accuracy))
