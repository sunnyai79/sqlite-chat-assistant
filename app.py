import streamlit as st
import pandas as pd
from db import get_db_connection
from query_handler import process_query

# Streamlit UI Setup
st.set_page_config(page_title="SQLite Chat Assistant", layout="wide")
st.title("💬 SQLite Chat Assistant")

query = st.text_input("Ask your question about employees or departments:")

if st.button("Submit"):
    if query:
        sql_query = process_query(query)
        
        if sql_query:
            try:
                conn = get_db_connection()
                result = pd.read_sql_query(sql_query, conn)
                conn.close()

                if not result.empty:
                    st.dataframe(result, use_container_width=True)
                else:
                    st.warning("No data found for your query.")
            except Exception as e:
                st.error(f"Error executing query: {e}")
        else:
            st.warning("Sorry, I couldn't understand your query.")
