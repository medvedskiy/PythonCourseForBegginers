# Program gets rate and ammount of dollars and returns ammount of rubbles to be spent for such ammount of dollars
rate, ammount = float(input()), int(input())
message = f"""Current dollar rate is {rate}. You want to buy {ammount} dollars
You must pay {rate * ammount}"""
print(message)
