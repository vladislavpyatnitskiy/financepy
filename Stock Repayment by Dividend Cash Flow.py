def dividend_cf(x, y, f): # How much time needed for stock to be repaid by divs
    
    cf_sum = 0  # Original cash flow value

    while x > cf_sum:
        cf_sum += y  # Add until cash flow sum < price

    return f"Stock will be repaid in {round(cf_sum / (y * f), 2)} years "

print(dividend_cf(51, 0.51, 4))  # Test
