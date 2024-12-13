import streamlit as st
from pathlib import Path
from langchain.agents import initialize_agent
from langchain_community.utilities import SQLDatabase  # Corrected import for SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StdOutCallbackHandler
from langchain.tools import Tool
from sqlalchemy import create_engine
from main import connect
from config import config
from urllib.parse import quote  # Import the connect function to establish the PostgreSQL connection
from langchain_groq import ChatGroq
import os

st.set_page_config(page_title="LangChain: Postgres AI", page_icon="📚")
st.title("📚 LangChain: Postgres AI")

# Sidebar for API key
api_key = st.sidebar.text_input(label="Groq API Key", type="password")
if not api_key:
    st.error("Groq API Key not found. Please enter it in the sidebar.")
    st.stop()

# Initialize the LLM model with the Groq API key
llm = ChatGroq(groq_api_key=api_key, model_name="mixtral-8x7b-32768", streaming=True)



def configure_db():
    """Establish and return a connection to the PostgreSQL database using SQLAlchemy."""
    try:
        # Use connect() to retrieve connection parameters
        params = config()

        # URL-encode the password to handle special characters
        user = quote(params["user"])
        password = quote(params["password"])
        host = params["host"]
        port = params["port"]
        database = params["database"]

        # Build the connection string
        connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        print(f"Connection string: {connection_string}")  # Debugging line

        # Create SQLAlchemy engine
        engine = create_engine(connection_string)
        return SQLDatabase(engine)
    except KeyError as key_error:
        st.error(f"Missing database connection parameter: {key_error}")
        st.stop()
    except Exception as e:
        st.error(f"Failed to configure the database: {e}")
        st.stop()





# Configure database
try:
    db = configure_db()
except Exception as e:
    st.error(f"Database configuration failed: {e}")
    st.stop()

# Toolkit function for running database queries
def query_database(query):
    """Execute a query on the connected database."""
    try:
        print(f"Executing query: {query}")  # Debugging line
        # Ensure the query is properly formatted
        sanitized_query = query.strip().strip(";")
        return db.run(sanitized_query)
    except Exception as e:
        st.error(f"Query execution failed: {e}")
        return None


# Set up the LangChain agent
agent = initialize_agent(
    tools=[Tool(name="SQL Query Tool", func=query_database, description="Use this to query the database.")],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Initialize session state for message history
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input from the user
user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        stdout_callback = StdOutCallbackHandler()
        try:
            response = agent.run(user_query, callbacks=[stdout_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
        except Exception as e:
            st.error(f"Failed to process the query: {e}")
