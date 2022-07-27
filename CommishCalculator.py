print("Lets find out the commission amount!")

sale_price = input("Please enter the Sale Price: ")
commission_percentage = input("Please enter the Commission Percentage: ")

print(f"The Commission amount is \n ${(int(sale_price) + int(commission_percentage))/100}")

print(f"The Real Revenue after Commission is \n ${int(sale_price) - ((int(sale_price) + int(commission_percentage))/100)}")
