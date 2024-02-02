### Gabriel_H_shoe_sale.py
### Gabriel Hesse
### January 25, 2024
### Time Spent = Two Hours 30 Mins

"""
Program that prints a recipt to the user.
"""

total = 0
discount_total = 0
overall_total = 0

# User input for number of items to be purchased.
num_item = int(input('Enter the number of items to be purchased: ')) 

# num_items needed to be able to compare to num_item and add up values.
num_items = int(0)

if num_item > 0:
     boot1 = int(input('Enter number of booties as digit(s): '))
     boot2 = int(input('Enter number of boots as digit(s): '))
     san1 = int(input('Enter number of sandals as digit(s)): '))
     loafers1 = int(input('Enter number of booties as digit(s): '))
     sneakers1 = int(input('Enter number of sneakers as digit(s): '))
     num_items += boot1
     num_items += boot2
     num_items += san1
     num_items += loafers1
     num_items += sneakers1
     # Error check to see if user has added too many items. 
     if num_items > num_item:
          print("Number of items chosen is too high.")
          exit()
     # If error check passes, proceed to do calcs to find values.
     elif num_items == num_item:
          boot1_total = boot1*120
          boot1_discount = boot1_total * 0.15
          boot1_discount_total = boot1_total - boot1_discount
          boot2_total = boot2*230
          boot2_discount = boot2_total * 0.10
          boot2_discount_total = boot2_total - boot2_discount
          san1_total = san1*40
          san1_discount = san1_total * 0.20
          san1_discount_total = san1_total - san1_discount
          loafers1_total = loafers1*90
          sneakers1_total = sneakers1*120
          overall_total = boot1_discount_total + boot2_discount_total + san1_discount_total + loafers1_total + sneakers1_total
          overall_total_tax = overall_total * 0.05
          complete_total = overall_total + overall_total_tax
     # Print statements that form the table to display the data to the user.  
          print("Items   Quanity   Original Cost   Discount Cost")
          print("Booties" "%5d" "%13d" "%16d" %(boot1,boot1_total,boot1_discount_total))
          print("Boots" "%7d" "%13d" "%16d" %(boot2,boot2_total,boot2_discount_total))
          print("Sandals" "%5d" "%13d" "%16d" %(san1,san1_total,san1_discount_total))
          print("Loafers" "%5d" "%13d" "%16d" %(loafers1,loafers1_total,loafers1_total))
          print("Sneakers" "%4d" "%13d" "%16d" %(sneakers1,sneakers1_total,sneakers1_total))
          print("_____________________________________________")
          print("                 Total: %.2f"%overall_total)
          print("                 GST/HST: %.2f"%overall_total_tax)
          print("                 Total with tax: %.2f"%complete_total)

     check = input("Confirm Purchase? Yes or No: ")
     if check == "Yes":
          print("Thank you for the purchase!")
     else:
          print("Purchase declined.")
          
          
          




