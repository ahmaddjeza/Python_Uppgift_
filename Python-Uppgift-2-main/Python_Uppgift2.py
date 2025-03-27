import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#a) Börja med att läsa in filen riket2023_åk9_np.xlsx och sheets för de olika ämnena (engelska, matematik, svenska,
# svenska som andraspråk). Ändra kolumnnamnen på respektive dataframe så du får något liknande som nedan.

#Läser in datan från Excelfilen.
df_Engelska = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx', skiprows=8, sheet_name="Engelska")
df_Matematik = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx', skiprows=8, sheet_name="Matematik")
df_Svenska = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx', skiprows=8, sheet_name="Svenska")
df_Svenska_som_andraspråk = pd.read_excel('visualiseringar/riket2023_åk9_np.xlsx', skiprows=8, sheet_name="Svenska som andraspråk")

#Ändrar kolumnamnen så att det ser ut som det gör enligt instruktionerna.
columnname = ["Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)",
              "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)", "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]

df_Engelska.columns = columnname
df_Matematik.columns = columnname
df_Svenska.columns = columnname
df_Svenska_som_andraspråk.columns = columnname

#b) För de olika ämnena, rita en stapeldiagram på totala poängen för de olika huvudmännen. Placera alla diagram i en
#plott med subplottar.

# Metod för att konvertera "Totalt (poäng)" till numeriska värden
def convert_to_numeric(df, column):
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Konvertera poängkolumnen för varje ämne
convert_to_numeric(df_Engelska, "Totalt (poäng)")
convert_to_numeric(df_Matematik, "Totalt (poäng)")
convert_to_numeric(df_Svenska, "Totalt (poäng)")
convert_to_numeric(df_Svenska_som_andraspråk, "Totalt (poäng)")

