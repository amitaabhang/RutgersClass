import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
total_months=0
total_profit = 0
total_loss=0
dateyear =[]
profits=[]
loss=[]

profits_dict = {"DateYear": [], "Profits":[]}
losses_dict =  {"DateYear":[], "Loss":[]}

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
    csv_header = next(csv_reader)

    print(f"CSV Header: {csv_header}")

    #Make lists

    i=0
    for row in csv_reader:
        if(float(row[1]) >= 0):
            #print("Profits"+row[0] + row[1])
            profits_dict["DateYear"].append(row[0])
            profits_dict["Profits"].append(row[1])
        elif(float(row[1]) < 0):
            #print("Loss"+row[0] + row[1])
            losses_dict["DateYear"].append(row[0])
            losses_dict["Loss"].append(row[1])

     
    #print(profits_dict["DateYear"])
    #print(profits_dict["Profits"])
    #print(losses_dict["DateYear"])
    #print(losses_dict["Loss"])
  

def GreatestIncreaseInProfit(profits_data):
    new_profits_data = list(map(int, profits_data))
    #maxProfitValue = max((max(profits_data["Profits"]) for key in profits_data))
    #dict_indices = [i for i, d in enumerate(profits_data) if d["Profits"] == maxValue]
    print(new_profits_data)
    value = (max(new_profits_data))

    return value

def GreatestDecreaseInLosses(losses_data):
    
   # maxLossValue = max((max(new_losses_data["Loss"]) for key in new_losses_data))
    #dict_indices = [i for i, d in enumerate(profits_data) if d["Profits"] == maxValue]
    return maxLossValue
    #return dict_indices

print(GreatestIncreaseInProfit(profits_dict))
print(GreatestDecreaseInLosses(losses_dict))