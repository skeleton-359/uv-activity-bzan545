import pandas as pd
from rich import print

print("I am running this with uv")

orders = pd.read_csv("data/snack_orders.csv")

print("Snack orders")
print(orders)

print("Top snacks by quantity")
top_snacks = orders.groupby("snack")["quantity"].sum().sort_values(ascending=False).head(3)
print(top_snacks)
