hour_worked = int(input("enter the  hour:"))
rate = int(input("enter the rate:"))
if hour_worked > 40:
	normal_rate = hour_worked * rate
	overtime_pay = (hour_worked - 40) * (rate * .5)
	print("payable amount:",normal_rate+overtime_pay)
else:
	pay =  hour_worked * rate
	print("payable amount:",pay)
	
	


