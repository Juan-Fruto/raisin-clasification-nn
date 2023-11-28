import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from tabulate import tabulate

columns = ["Measure"]
mean = ["Mean"]
median = ["Median"]
mode = ["Mode"]

# dataframe
df = pd.read_excel('./dataset/Raisin_Dataset.xlsx')

# unlabel dataset
df = df.drop('Class', axis=1)

# graphs settings
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
fig.suptitle('Data distribution for each column', fontsize=16)

for i, column in enumerate(df.columns):
  # graph by each column
  row, col = divmod(i, 4)
  sns.histplot(df[column], kde=True, ax=axes[row, col])
  axes[row, col].set_title(column)
  axes[row, col].set_xlabel('Values')
  axes[row, col].set_ylabel('Frecuency')

  # meseaure of each column
  columns.append(column)
  mean.append(df[column].mean())
  median.append(df[column].median())
  mode.append(statistics.mode(df[column]))

# desing settings
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('./distribution/original_distribution.png')

print(tabulate([mean, median, mode], columns, floatfmt=".4f", tablefmt="pretty"))
