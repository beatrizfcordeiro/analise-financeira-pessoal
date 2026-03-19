import pandas as pd

# Carregar os dados
df = pd.read_csv("dados.csv")

# Mostrar dados
print("📊 Dados:")
print(df)

# Total de gastos
total = df["valor"].sum()
print("\n💰 Total de gastos:", total)

# Percentual por categoria
df["percentual"] = (df["valor"] / total) * 100

print("\n📈 Percentual de gastos:")
print(df)

# Maior gasto
maior_gasto = df.loc[df["valor"].idxmax()]
print("\n🔥 Maior gasto:")
print(maior_gasto)
