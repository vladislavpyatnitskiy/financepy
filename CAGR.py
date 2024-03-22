def CAGR(x): # Compound Annual Growth Rate
    
    l = []  # Store values

    for n in range(len(x)):
        while x[n] != x[-1]:  # Add values Till last number
            l.append(round((x[n + 1] / x[0]) ** (1 / (n + 1)) - 1, 2))
            break  # Stop when cycle is over

    return l  # Display


print(CAGR([1000, 1200, 900, 1600, 1800, 2250]))  # Test
