import pandas as pd


# Reading the csv file from the path
df_read = pd.read_csv('File.csv')

# saving xlsx file to the path
df_write = pd.ExcelWriter('File.xlsx')
df_read.to_excel(df_write, index=False)

df_write.save()
