def monthly_vs_yearly_payment(x, m, r, P): # Compare plans

    # Calculate Monthly and Yearly plans
    M = sum([-x / ((1 + r) ** (1 / m)) ** i for i in range(m)])
    Y = sum([-P / m * ((1 + r) ** (1 / m)) ** i for i in range(m)])

    D = round(abs(Y - M), 2)  # Calculate difference and show beneficial one

    if M > Y:
        return f"Subscribe to a monthly payment as it is {D} cheaper"
    else:
        return f"Subscribe to a yearly payment as it is {D} cheaper"

print(monthly_vs_yearly_payment(x = 6.99, m = 12, r = 0.05, P = 69.99)) # Test
