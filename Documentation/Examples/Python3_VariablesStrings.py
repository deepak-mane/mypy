# Building a Mileage Convertor with User Input

print("How many Kilometers did you Cycle today? ")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was {miles}mi")

#round(thing to round, how many decimal points)