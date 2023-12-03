# Question 16(a)
# Student Name:
#David Cummins
#This program is a simple ordering system 
print("Welcome to the new online ordering system.\n")
staff = input("Who is processing the order")

total_cost=0
item_count=input("How many items are in your order")
item_count= int(item_count)
x = item_count+1
while item_count<x:
    if item_count<0:
        print("invalid option")
        break
    end = 0
    balance = input("What is the customers balance")
    balance = float(balance)
    while end!=item_count:
        price_of_item=float(input("Enter the price of item {}".format(item_count)+" : € "))
        total_cost+=price_of_item
        end = end+1


    balance1 = balance-total_cost
    if balance1<0:
        print("The customer does not have enough credit, they still owe: €",((balance1)*-1))
    print("You entered",item_count,"items and the total due is €",total_cost)
    print("What is the customers balance before payment: €",balance)
    print("Your remaining balance after payment: €",(balance-total_cost))
    print("The staff that processed your order was ",staff)
    break