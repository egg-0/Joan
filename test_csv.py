import csv
import pandas as pd

id_file_name = 'steam_id.csv'

with open(id_file_name, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    spamwriter.writerow(['DISCORD_ID','STEAM_ID'])
    spamwriter.writerow(['123', '456'])

csvfile.close()

#with open(id_file_name, 'r', newline='') as csvfile:
#    reader = csvfile.readlines()
    #for line in reader:
        #print(line)


df = pd.read_csv('steam_id.csv')

print(df)

df.append(['7','8'])

print(df)

#print(csv_file.head(3))

#print(csv_file.columns)
#print(csv_file.STEAM_ID)

#print(csv_file.STEAM_ID._ndarray_values)