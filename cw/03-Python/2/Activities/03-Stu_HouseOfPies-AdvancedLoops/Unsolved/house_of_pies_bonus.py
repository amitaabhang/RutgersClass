# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0,0,0,0,0,0,0,0,0,0,0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")
i=0
for pie in pie_list:
    print(str(i)+' '+pie)

# While we are still shopping...
# Loop starts here

need_more = "y"

while need_more=="y":
    selected_pie_index = int(input("Choose the pie you want"))
    pie_purchases[selected_pie_index] = pie_purchases[selected_pie_index]+1
    need_more=input("Need to shop more: ")


# Loop end here
# Once the pie list is complete
print("------------------------------------------------------------------------")
print("You purchased a total of " + str(len(pie_purchases)) + ".")
i =0
for selected_pie in pie_purchases:
    print(pie_purchases[i] + str() +pie_list[i])