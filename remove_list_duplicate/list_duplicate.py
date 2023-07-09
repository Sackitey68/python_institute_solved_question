my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
result = []
for item in my_list:
    if item not in result:
        result.append(item)
#

my_list = result
print("The list with unique elements only:")
print(my_list)
