import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#a) Börja med att läsa in filen riket2023_åk9_np.xlsx och sheets för de olika ämnena (engelska, matematik, svenska,
# svenska som andraspråk). Ändra kolumnnamnen på respektive dataframe så du får något liknande som nedan.

#Läser in datan från Excelfilen.
df_Engelska = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx',skiprows=8, sheet_name="Engelska")
df_Matematik = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx',skiprows=8, sheet_name="Matematik")
df_Svenska = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx',skiprows=8, sheet_name="Svenska")
df_Svenska_som_andraspråk = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx',skiprows=8, sheet_name="Svenska som andraspråk")



