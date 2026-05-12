import streamlit as st

from utils.llm import generate_sql
from utils.db import run_query, get_schema
from utils.validator import validate_query
from utils.charts import create_chart

# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="AI SQL Agent",
    layout="wide"
)

# --------------------------------
# Session State
# --------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------
# Title
# --------------------------------
st.title("AI SQL Agent")

st.write(
    "Ask questions in natural language."
)

# --------------------------------
# Sidebar
# --------------------------------
st.sidebar.header("Database Schema")

schema = get_schema()

st.sidebar.code(schema)

# --------------------------------
# User Input
# --------------------------------
question = st.chat_input(
    "Ask about your data..."
)

# --------------------------------
# Process Question
# --------------------------------
if question:

    st.chat_message("user").write(question)

    with st.spinner("Generating SQL..."):

        sql_query = generate_sql(
            question,
            schema
        )

    st.chat_message("assistant").write(
        "Generated SQL:"
    )

    st.code(sql_query, language="sql")

    # --------------------------------
    # Validate Query
    # --------------------------------
    if not validate_query(sql_query):

        st.error(
            "Dangerous query blocked."
        )

    else:

        try:

            # Execute Query
            df = run_query(sql_query)

            st.subheader("Results")

            st.dataframe(
                df,
                width='stretch'
            )

            # Create Chart
            fig = create_chart(df)

            if fig:
                st.plotly_chart(
                    fig,
                    width='stretch'
                )

            # Save History
            st.session_state.history.append({
                "question": question,
                "sql": sql_query
            })

        except Exception as e:

            st.error(str(e))

# --------------------------------
# History
# --------------------------------
st.sidebar.header("Query History")

for item in st.session_state.history:

    st.sidebar.write(
        f"Q: {item['question']}"
    )

    st.sidebar.code(
        item["sql"]
    )