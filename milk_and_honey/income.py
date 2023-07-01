income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if (income <= 0):
    tax = 0

elif (income <= 85528):
    tax = (0.18 * income) - 556.02 
            
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

