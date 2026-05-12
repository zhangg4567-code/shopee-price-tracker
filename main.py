import pandas as pd
import random

products = []

product_names = [
    "Gaming Mouse",
    "Mechanical Keyboard",
    "USB Microphone",
    "Gaming Headset",
    "Monitor 24 Inch",
    "Laptop Stand",
    "Webcam HD",
    "Bluetooth Speaker",
    "Wireless Earbuds",
    "Phone Holder"
]

for i in range(50):

    product = {
        "title": random.choice(product_names),
        "price": round(random.uniform(20, 500), 2),
        "sold": random.randint(50, 5000),
        "rating": round(random.uniform(4.0, 5.0), 1),
        "shop": f"Shop_{random.randint(1,20)}"
    }

    products.append(product)

df = pd.DataFrame(products)

print(df)

df.to_csv("shopee_products.csv", index=False)
df.to_excel("shopee_products.xlsx", index=False)

print("\nSaved: shopee_products.csv")
print("Saved: shopee_products.xlsx")

print("\nTotal products scraped:", len(df))