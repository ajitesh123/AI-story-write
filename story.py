import os
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# App configuration
st.set_page_config(page_title="Story Bot", page_icon="📖")

def get_response(user_query, chat_history):
    template = """
    You are a storytelling assistant. Help the user create an interactive story based on their input and the conversation history:

    Output with interestaing paragraph headings, plot twists, image draw using text etc. Keep output brief.

    Chat history: {chat_history}
    User input: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=OPENAI_API_KEY)
    
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query,
    })

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Once upon a time, in a magical land far away, there lived a brave adventurer. What would you like to name the adventurer?"),
    ]

# Sidebar for user input and AI conversation
with st.sidebar:
    st.title("Story Bot")
    st.write("Welcome to Story Bot! I'm here to help you create an interactive story. Let's embark on an exciting adventure together!")

    # User input
    st.header("Your Input")
    user_query = st.text_input("Type your message here...", key="user_input")
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("You"):
            st.markdown(user_query)
        
        with st.chat_message("Story Bot"):
            response = st.write_stream(get_response(user_query, st.session_state.chat_history))
        
        st.session_state.chat_history.append(AIMessage(content=response))

# Main area for displaying the story
story_col, _ = st.columns([2, 1])
with story_col:
    st.header("Story")
    story = ""
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            story += message.content + "\n\n"
    st.write(story)

# Styling
st.markdown(
    """
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .chat-message p {
        margin-bottom: 0;
    }
    .chat-message.ai {
        background-color: #f0f0f0;
    }
    .chat-message.human {
        background-color: #e6f7ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)