sender_name = input("Input sender Name :  ")
type_of_items = input("Input type of items :  ")

is_fragile = input("is it fragile? : ") 
weight = float(input("Input the weight : "))
distance = float(input("Input distance :  "))
is_express = input("Input if it is express :  ") 
is_international = input("Input if it is internatinal : ") 

base_cost = (weight * 2.50) + (distance * 0.15)

free_shipping = 0
international_express = (base_cost * 1.40) + 50
express_heavy = (base_cost * 1.20) + 25
oversized = base_cost + 30
standard = base_cost

if weight <= 2 and distance <= 100 and is_express == False and is_international == False:
    total = free_shipping
    print("Free Shipping")

elif is_international == True and is_express == True:
    total = international_express
    print("International Express")

elif is_express == True or (is_international == True and weight > 20):
    total = express_heavy
    print("Express or Heavy International")

elif weight > 30 or distance > 1000:
    total = oversized
    print("Oversized")

else:
    total = standard
    print("Standard Rate")

print("Sender Name: ", sender_name)
print("type of items: ", type_of_items)
print("Fragile?: ", is_fragile)
print("Weight: ", weight)
print("Distance: ", distance)
print("Express?: ", is_express)
print("International?: ", is_international)
print("Total: ", total)
