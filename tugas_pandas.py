
#1
import pandas as pd
df_sampah = pd.read_excel('dataset_sampah.xlsx', sheet_name='data')

print(df_sampah)

print('='*30)
#2
total_2015=[]
for index, row in df_sampah.iterrows():
    if row['tahun']==2015:
        total_2015.append(row['jumlah_produksi_sampah'])

total_sampah_2015=sum(total_2015)
print(f"jumlah total sampah di tahun 2015: {total_sampah_2015}")
print('='*30)

#3
from collections import defaultdict
sampah_pertahun = defaultdict(int)

for index, row in df_sampah.iterrows():
    sampah_pertahun[row['tahun']] += row['jumlah_produksi_sampah']

sampah_pertahun = dict(sampah_pertahun)

for index, row in sampah_pertahun.items():
    print(f"Total Sampah di Tahun {index}: {round(row, 2)} ")


print('='*30)

#4

jumlah_sampah_perkota = defaultdict(int)

for index, row in df_sampah.iterrows():
    jumlah_sampah_perkota[row['nama_kabupaten_kota']] += row['jumlah_produksi_sampah']

jumlah_sampah_perkota = dict(jumlah_sampah_perkota)
for index, row in jumlah_sampah_perkota.items():
    print(f"Total sampah di {index} periode 2015-2021: {round(row, 2)}")

print('='*30)

#export cvs dan excel
df_jumlah_pertahun = pd.DataFrame(list(sampah_pertahun.items()), columns=['tahun', 'total_sampah'])
df_jumlah_pertahun.to_csv('sampah_pertahun.csv', index=False)
df_jumlah_pertahun.to_excel('sampah_pertahun.xlsx', index=False)

df_jumlah_perkota = pd.DataFrame(list(jumlah_sampah_perkota.items()), columns=['wilayah', 'total_sampah'])
df_jumlah_perkota.to_csv('sampah_perkota.csv', index=False)
df_jumlah_perkota.to_excel('sampah_perkota.xlsx', index=False)