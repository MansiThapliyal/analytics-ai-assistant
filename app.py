import streamlit as st
from sql_agent import question_to_sql
from executor import run_sql

st.title("🚗 Rental Analytics Assistant")
q = st.text_input("Ask a business question:")

if q:
    with st.spinner("Thinking..."):
        try:
            sql = question_to_sql(q)
            st.code(sql, language="sql")     # transparency: show the SQL
            df = run_sql(sql)
            st.dataframe(df)
            if len(df.columns) == 2 and len(df) > 1:
                st.bar_chart(df.set_index(df.columns[0]))
        except Exception as e:
            st.error(f"Failed: {e}")