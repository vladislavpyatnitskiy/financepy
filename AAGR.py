def AAGR(x): # Average Annual Growth Rate
    
    l = []  # Store values

    for n in range(len(x)):
        while x[n] != x[-1]:  # Add values
            l.append(round((x[n + 1] / x[n]) - 1, 2))  # Till last number
            break  # Stop when cycle is over

    return l  # Display


print(AAGR([1000, 1200, 900, 1600, 1800, 2250]))  # Test
