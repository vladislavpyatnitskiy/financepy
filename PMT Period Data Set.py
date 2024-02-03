def pmt_df_period(a, r):
    l = pd.DataFrame(columns=["Period", "Amount"])
    
    for t in np.arange(1, 50, 1):
        interest = (a * r / 12) / (1 - (1 + r / 12) ** (-t * 12))
        l = l.append({"Period": t, 
                      "Amount": round(interest, 2)}, ignore_index=True)

    return l

result_df = pmt_df_period(200000, 0.045)
print(result_df)
