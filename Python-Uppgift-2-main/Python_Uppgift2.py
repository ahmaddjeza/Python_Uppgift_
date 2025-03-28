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

# Skapa en 2x2 subplot för att visa alla fyra diagram
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Första diagrammet - Engelska
axes[0, 1].bar(df_Engelska["Huvudman"], df_Engelska["Totalt (poäng)"], color="yellow")
axes[0, 1].set_title("Engelska - Totalt Poäng")
axes[0, 1].set_xlabel("Huvudman")
axes[0, 1].set_ylabel("Poäng")
axes[0, 1].set_xticklabels(df_Engelska["Huvudman"], rotation=45)

# Andra diagrammet - Matematik
axes[1, 0].bar(df_Matematik["Huvudman"], df_Matematik["Totalt (poäng)"], color="green")
axes[1, 0].set_title("Matematik - Totalt Poäng")
axes[1, 0].set_xlabel("Huvudman")
axes[1, 0].set_ylabel("Poäng")
axes[1, 0].set_xticklabels(df_Matematik["Huvudman"], rotation=45)

# Tredje diagrammet - Svenska
axes[0, 0].bar(df_Svenska["Huvudman"], df_Svenska["Totalt (poäng)"], color="blue")
axes[0, 0].set_title("Svenska - Totalt Poäng")
axes[0, 0].set_xlabel("Huvudman")
axes[0, 0].set_ylabel("Poäng")
axes[0, 0].set_xticklabels(df_Svenska["Huvudman"], rotation=45)

# Fjärde diagrammet - Svenska som andraspråk
axes[1, 1].bar(df_Svenska_som_andraspråk["Huvudman"], df_Svenska_som_andraspråk["Totalt (poäng)"], color="red")
axes[1, 1].set_title("Svenska som andraspråk - Totalt Poäng")
axes[1, 1].set_xlabel("Huvudman")
axes[1, 1].set_ylabel("Poäng")
axes[1, 1].set_xticklabels(df_Svenska_som_andraspråk["Huvudman"], rotation=45)

# Justera layouten så att diagrammen inte överlappar varandra
plt.tight_layout()

# Spara bilden
plt.savefig("visualiseringar/np_totalt_poäng.png")

# Visa bilden
plt.show()

#Uppgift 2
#I uppgifterna nedan ska du använda dig av datasetet betyg_o_prov_riksnivå.xlsx. Använd Plotly för att rita diagrammen
#nedan för de uppgifter som kräver diagram. Använd Pandas för att svara på frågor om datasetet.

#a) Rita ett linjediagram för andel elever som saknar godkänt betyg i ett eller fler ämnen för läsår 18-23. Ta med totalt,
#flickor och pojkar i samma graf.

#Läser in datan från Excelfilen.
df_betyg_och_prov = pd.read_excel("visualiseringar\\betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1B", skiprows=7)

# Sätter nya kolumnnamn
kolumner = ["Läsår", "Meritvärde Totalt", "Meritvärde Flickor", "Meritvärde Pojkar", "Totalt", "Flickor", "Pojkar", "Ej Godkänt Totalt", "Ej Godkänt Flickor", "Ej Godkänt Pojkar"]
df_betyg_och_prov.columns = kolumner

# Väljer bara de kolumner vi behöver
df_ej_godkänt = df_betyg_och_prov[["Läsår", "Ej Godkänt Totalt", "Ej Godkänt Flickor", "Ej Godkänt Pojkar"]]

# Tar bara med de senaste 5 åren
df_ej_godkänt = df_ej_godkänt.head(5)

