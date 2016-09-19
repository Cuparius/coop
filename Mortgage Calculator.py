# Lab04v100Dena.py
# The Mortgage Payment Program
# This is the student starting file of the Lab04 Assignment.
#

p = eval (input('Enter principal'))
ar = eval (input('Enter annual rate'))
ny = eval (input('Enter number of years'))

r = ar / 100 / 12
n = ny * 12

monthly_payment = round(((r * (1 + r) ** n) / ((1 + r) ** n - 1)) * p, 2

print ('Principal:        $ ' + str(p))
print ('Annual Rate:        ' + str(ar) + ' %')
print ('Number of years     ' + str(ny))
print ('Monthly Interest  $ ' + str(monthly_payment))

total_payments = monthly_payments * n
total_interest = total_payments - p

print ('Total Payment:    $ ' + str(round(total_payments, 1)))
print ('Total Interst:    $ ' + str(round(total_interest, 1)))