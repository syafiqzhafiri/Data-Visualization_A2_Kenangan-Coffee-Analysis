import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Gambar
st.image("banner.jpg", use_container_width=True)

# Title
st.title("☕ Kenangan Coffee Sales Analysis")

# Data
data = {
'Coffee Type': ['Kopi Susu Black Aren', 'Latte', 'Moccha Latte', 'Americano', 'Cappucino'],
'Sales': [500, 450, 350, 200, 250],
}
df = pd.DataFrame(data)

with st.expander("Bar Chart of Coffee Sales"):
    # Bar Chart - Best and worst sales
    best_sale = df[df["Sales"] == df["Sales"].max()]
    worst_sale = df[df["Sales"] == df["Sales"].min()]

    # Bar Chart
    st.subheader("Bar Chart of Coffee Sales")
    fig, ax = plt.subplots()
    ax.bar(df["Coffee Type"], df["Sales"], color="skyblue")
    ax.tick_params(axis='x', labelsize=8) #biar dia keliatan font nya
    ax.bar(best_sale["Coffee Type"], best_sale["Sales"], color="green", label="Best Sale")
    ax.bar(worst_sale["Coffee Type"], worst_sale["Sales"], color="red", label="Worst Sale")
    ax.legend()
    st.pyplot(fig)

with st.expander("Pie Chart of Coffee Sales"):
    # Pie Chart
    st.subheader("Pie Chart of Coffee Sales")
    fig2, ax2 = plt.subplots()
    colors = ["#ff9999","#66b3ff","#99ff99","#ffcc99", "#ff6666"]
    ax2.pie(df["Sales"], labels=df["Coffee Type"], autopct="%1.1f%%", startangle=90,
    colors=colors)
    ax2.axis("equal")
    st.pyplot(fig2)

    # Best and Worst Sale Info
    st.write("### Best Sale")
    st.write(best_sale)
    st.write("### Worst Sale")
    st.write(worst_sale)

with st.expander("Filter by Minimum Sales"):
    # Sliders (for number 2)
    st.subheader("Filter by Minimum Sales")
    min_sales = st.slider(
        "",
        min_value=0,
        max_value=500,
        value=0
    )

    filtered_df = df[df["Sales"] >= min_sales]

    # Chart using filtered_df
    fig, ax = plt.subplots()

    ax.bar(filtered_df["Coffee Type"], filtered_df["Sales"], color="#6F4E37")

    ax.tick_params(axis='x', labelsize=8)
    plt.xticks(rotation=30, ha='right')

    st.pyplot(fig)