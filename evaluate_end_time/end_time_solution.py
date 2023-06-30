hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
total_time = hour * 60 + mins + dura
total_hours = total_time // 60 % 24
total_mins = total_time % 60

print(total_hours, end=":")
print(total_mins)

