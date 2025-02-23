import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        columns = df.columns.tolist()

        if columns:  # Check if the DataFrame has columns
            selected_column = st.selectbox("Select column to filter by", columns)
            
            if not df[selected_column].isnull().all():  # Ensure column has valid values
                unique_values = df[selected_column].dropna().unique()
                selected_value = st.selectbox("Select value", unique_values)

                filtered_df = df[df[selected_column] == selected_value]
                st.write(filtered_df)

                st.subheader("Plot Data")
                x_column = st.selectbox("Select x-axis column", columns)
                y_column = st.selectbox("Select y-axis column", columns)

                if st.button("Generate Plot") and not filtered_df.empty:
                    try:
                        st.line_chart(filtered_df.set_index(x_column)[y_column])
                    except Exception as e:
                        st.error(f"Plotting error: {e}")
            else:
                st.warning("Selected column has no valid values to filter.")
        else:
            st.warning("The uploaded CSV has no columns.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.write("Waiting on file upload...")
