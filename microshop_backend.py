import pandas as pd
from transformers import pipeline

# ---------------------------------------------------
# Load Models Once (for efficiency)
# ---------------------------------------------------
print("🔄 Loading AI models... (this may take a few minutes the first time)")

# Message generation model (English)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

# Hindi translation model (for vernacular support)
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

print("✅ Models loaded successfully!\n")

# ---------------------------------------------------
# Analyze inventory and detect low-stock items
# ---------------------------------------------------
def analyze_inventory(data):
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data  # already a DataFrame
    low_stock = df[df["stock"] < df["threshold"]]
    return low_stock

# ---------------------------------------------------
# Suggest reorder quantity
# ---------------------------------------------------
def suggest_reorder(df):
    df["reorder_qty"] = (df["threshold"] * 1.5 - df["stock"]).astype(int)
    return df

# ---------------------------------------------------
# Generate reorder messages (grouped by supplier)
# ---------------------------------------------------
def generate_grouped_messages(low_stock):
    supplier_groups = {}

    # Group items by supplier
    for _, row in low_stock.iterrows():
        supplier = row["supplier"]
        if supplier not in supplier_groups:
            supplier_groups[supplier] = []
        supplier_groups[supplier].append((row["item"], row["reorder_qty"]))

    messages = {}

    # Generate one message per supplier
    for supplier, items in supplier_groups.items():
        item_list = ", ".join([f"{qty} units of {item}" for item, qty in items])

        prompt = (
            f"Write a short and polite business message to reorder the following items "
            f"from supplier {supplier}: {item_list}. Keep it concise and professional."
        )

        english_msg = generator(prompt, max_length=120, temperature=0.7)[0]["generated_text"]
        hindi_msg = translator(english_msg)[0]["translation_text"]

        messages[supplier] = {
            "english": english_msg,
            "hindi": hindi_msg
        }

    return messages


# ---------------------------------------------------
# Main Execution
# ---------------------------------------------------
if __name__ == "__main__":
    inventory_path = "inventory.csv"

    low_stock = analyze_inventory(inventory_path)
    if len(low_stock) == 0:
        print("✅ All items sufficiently stocked!")
    else:
        low_stock = suggest_reorder(low_stock)
        print("🚨 Low-stock items detected:\n")
        print(low_stock[["item", "stock", "threshold", "reorder_qty"]])

        print("\n📩 Generated reorder messages (Grouped by Supplier):\n")

        messages = generate_grouped_messages(low_stock)

        for supplier, content in messages.items():
            print(f"To {supplier}:")
            print(f"🗣️ English: {content['english']}")
            print(f"🪶 Hindi: {content['hindi']}\n")
