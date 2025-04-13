print ("coupon is applicable above 2000")
purchase = 1500
if purchase > 2000:
  discount = purchase / 10
  pay=purchase - discount
  print (f"coupon is applicable because purchase value {purchase}")
  print (f"Total amount: {pay}")
else:
  print (f"coupon is not applicable because purchase value {purchase}")