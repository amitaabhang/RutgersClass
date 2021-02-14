# Dictionary full of info
my_info = {
    "Name":"Arisha",
    "Age":4,
    "Hobbies":["Drawing","Playing","Jumping","Running"],
    "WakeUpTimes":{"Monday":7,"Tuesday":7,"Weekend":8.29}
}

# Print out results are stored in the dictionary
print(f'I am {my_info["Name"]} and I am {my_info["Age"]} years old')
print(f'I love  {my_info["Hobbies"][0]}, {my_info["Hobbies"][1]}, {my_info["Hobbies"][3]}')
print(f'I wake up at {float(my_info["WakeUpTimes"]["Weekend"])} on weekends ')
print(my_info.keys())
