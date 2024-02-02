import pandas as pd
import numpy as np

def pmt_df_interest(a, t):
    l = pd.DataFrame(columns=["Interest (%)", "Amount"])
    
    for r in np.arange(0, 0.51, 0.01):
        interest = (a * r / 12) / (1 - (1 + r / 12) ** (-t * 12))
        l = l.append({"Interest (%)": round(r * 100, 2), 
                      "Amount": round(interest, 2)}, ignore_index=True)

    l.at[0, "Amount"] = a / (t * 12)

    return l

result_df = pmt_df_interest(200000, 30)
print(result_df)
