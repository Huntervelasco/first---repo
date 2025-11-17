print("welcome to la cafeteria")
bill = 0
size = input("what size of coffe do you want? S, M or L: ").upper()
if size == "S":
    bill += 25
elif size == "M":
    bill += 30
elif size == "L":
    bill += 35
else:
    print("not valid option")
sabor_yn = input("do you want any additional flavor? Y or N:")
sabor_a = "None"
if sabor_yn == "Y":
    print("we have Vainilla (V)  $5 or Caramelo (C) $7")
    sabor_a = input("which one do you choose?: ").upper()
    if sabor_a == "V":
        bill += 5
    elif sabor_a == "C":
        bill += 7
special_milk = input("do you want any special milk? Y or N: ")
special_me = "Entera"
if special_milk == "Y":
    print("we have Deslactosada (D)  or Avena (A)   $4")
    special_me = input("wich one do you choose?: ").upper()
    if special_me == "D" or special_me == "A":
        bill += 4
number_of_coffes = int(input("how many coffes will you buy?: "))
if number_of_coffes >= 3:
    print("there is a discount of 10 percent")
    bill = (number_of_coffes * bill)*.9
else:
    bill = (number_of_coffes * bill)
print("\n---ORDER SUMMARY---")
print(f"coffe size: {size}")
print(f"Flavor: {sabor_a}")
print(f"Milk: {special_me}")
print(f"your bill is ${bill}")
print(f"Thank you for your order!")

