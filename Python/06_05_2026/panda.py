# Install Pandas
# IDLE cant't install this package  must be the same Python intepreter that IDLE uses.

import sys
print(sys.executable)

import pandas as pd
print(pd.__version__)

data = {
    "name":["Alice" , "BOB"  , "Charlie"],
        "score":[78 , 89 , 56]
        }

df = pd.DataFrame(data)
print(df)

print("min" , df["score"].min())
print("min" , df["score"].max())
