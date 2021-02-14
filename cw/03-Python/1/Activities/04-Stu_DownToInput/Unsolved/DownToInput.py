# Take input of you and your neighbor
your_name= input("What is your name? ")
neighbours_name= input("What is your neighbours name? ")

# Take how long each of you have been coding
your_coding_time =  int(input("How long have you been coding ?"))
your_neighbours_coding_time = int(input("How long is your neighbour coding ? "))

# Add total month
total_months_coded =  your_coding_time + your_neighbours_coding_time

# Print results
print("I am "+ your_name+ " and "+neighbours_name+ " is my neighbour")
print(f"We both are coding for {total_months_coded}")
