import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv("updated_business_categories.csv", encoding='latin-1')

# Clean up column names and text
df.columns = df.columns.str.strip()  # Strip any extra spaces in column names
df["business category"] = df["business category"].str.lower().str.strip()  # Lowercase and strip spaces
df["Size"].fillna("-", inplace=True)

# Display the county logo at the top of the app
st.image("County Logo.png", width=300)  # Adjust the width as necessary

# App title
st.title("📜 Uasin Gishu County Business Lookup Tool")
st.subheader("Directorate of Licensing and Compliance")

# User input
category_input = st.text_input("Enter a business category:", "").strip().lower()

if category_input:
    # Filter data using a case-insensitive partial match
    results = df[df["business category"].str.contains(category_input, na=False, case=False)]

    if not results.empty:
        # Pivot for better display
        pivot_df = results.pivot(index=["code", "business category", "Size"], columns="location", values="charge").reset_index()
        pivot_df.rename(columns={"cbd": "CBD Charge", "estates": "Estates Charge", "townships": "Townships Charge"}, inplace=True)

        # Display results
        st.write("### Matching Business Categories")
        st.dataframe(pivot_df, use_container_width=True)
    else:
        st.warning(f"No matching business category found for '{category_input}'.")
