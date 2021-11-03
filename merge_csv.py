import pandas
import os

import pandas as pd

# df = pd.read_csv("valid_urls.csv")
# df = df.iloc[:50000,:]
# df.to_csv("sample_urls.csv", index=False)


flag = 0

df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        if file == 0:
            df = pd.read_csv(file)
            flag = 1
        else:
            df = pd.concat([df, pd.read_csv(file)])
        os.remove(file)

df.to_csv("valid_urls.csv", index=False)
