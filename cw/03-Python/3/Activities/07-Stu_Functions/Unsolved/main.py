# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    output= float(sum(numbers)/len(numbers))
    return output

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))

number_input= [1,2,3,4,5,6,7,8,9,10]

val=0
for num in number_input :
    val = num+val

print(val/10)
