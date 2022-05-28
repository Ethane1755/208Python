import pandas as pd
data=pd.read_csv("https://bit.ly/3mJhnpV")
df=pd.DataFrame(data)
print(df.loc[:,"size_bytes"].max())

