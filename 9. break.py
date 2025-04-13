fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

discount = 50
customer = 56

for i in range(1, customer + 1):
    print(f"Discounted customer no. {i}")
    if i == discount:
        break