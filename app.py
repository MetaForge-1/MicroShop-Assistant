import streamlit as st
import pandas as pd
from microshop_backend import analyze_inventory, suggest_reorder, generate_grouped_messages

st.set_page_config(page_title="MicroShop Assistant", page_icon="🛍️", layout="wide")
st.title("🛒 MicroShop Assistant")
st.write("An AI-powered assistant that helps shopkeepers track low stock and auto-generate reorder messages in English and Hindi.")

uploaded_file = st.file_uploader("📂 Upload your inventory CSV file", type=["csv"])

if uploaded_file is not None:
    # Read uploaded CSV once
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Inventory Data")
    st.dataframe(df)

    # Analyze low-stock items directly from df (not file)
    low_stock = analyze_inventory(df)

    if len(low_stock) == 0:
        st.success("✅ All items sufficiently stocked!")
    else:
        low_stock = suggest_reorder(low_stock)
        st.subheader("🚨 Low-Stock Items Detected")
        st.dataframe(low_stock[["item", "stock", "threshold", "reorder_qty"]])

        st.subheader("📩 AI-Generated Reorder Messages")
        with st.spinner("Generating messages..."):
            messages = generate_grouped_messages(low_stock)

        for supplier, content in messages.items():
            st.markdown(f"### 🏪 {supplier}")
            st.markdown(f"**English:** {content['english']}")
            st.markdown(f"**Hindi:** {content['hindi']}")
            st.markdown("---")

else:
    st.info("👆 Upload an inventory CSV file to get started.")
