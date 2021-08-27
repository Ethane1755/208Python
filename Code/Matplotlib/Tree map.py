# libraries
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
import pandas as pd

sizes = [50, 25, 12, 6]
label = [50, 25, 12, 6]

df = pd.read_csv('D:/USER/Downloads/archive/Book1.csv')
# convert to numeric and drop na
df['Cases'] = pd.to_numeric(df['Cases'], errors='coerce')
df.dropna(inplace=True)
df.head()
df.sort_values('Cases', ascending=False, inplace=True)
df

fig, ax = plt.subplots(1, figsize = (12,12))
squarify.plot(sizes=df['Cases'], 
              label=df['State'][:11], 
              alpha=.8 )
plt.axis('off')
plt.title('India\'s Covid-19 Cases')
plt.show()