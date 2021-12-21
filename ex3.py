product_purchased = int(input("enter the quantity:"))
if product_purchased <10 :
 	tot_cost = product_purchased * 12
 	print("total cost:",tot_cost)
elif product_purchased >10 or product_purchased < 99:
 	tot_cost = product_purchased * 10
 	print("total cost:",tot_cost)
elif product_purchased >100:
 	tot_cost = product_purchased * 7
 	print("total cost:",tot_cost)
 	
 	
