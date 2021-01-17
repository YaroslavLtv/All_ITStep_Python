input_seconds = int(input("Enter time in seconds: "))
output_hours = input_seconds // 3600
output_minutes = input_seconds % 3600 // 60
rest_of_seconds = input_seconds % 3600 % 60

print(f" The time in format HH:MM:SS is: \n {output_hours} : {output_minutes} : {rest_of_seconds}")
