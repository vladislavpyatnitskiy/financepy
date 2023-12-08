# Function to calculate monthly mortgage payment
def mortgage_payment_calculator(a, r, t, c = "£"):
  
  p = round((a * r / 12) / (1 - (1 + r / 12) ** (-t * 12)), 2)
  
  print(f"Payment for {c}{a} mortgage for {t} year at {r}% is {c}{p} a month")

mortgage_payment_calculator(200000, 0.045, 30) # Test
