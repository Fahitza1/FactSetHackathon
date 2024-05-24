import streamlit as st
import random
import time
import datetime
import moviepy.editor as mp
import os 
from openai import AzureOpenAI, Stream
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

st.set_page_config(
    page_title="BudgiBot",
    page_icon="image1.jpg",
    layout="centered",
    initial_sidebar_state="expanded"
)

css = """
<style>
.stApp {
    background-color: #8fbc8f;
}
.stButton>button {
    color: #FFF;
    background-color: #808080;
}
.stTextInput>label, .stTextArea>label, .stDateInput>label {
    color: #4CAF50;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Load env variables
load_dotenv(find_dotenv())

os.environ["SSL_CERT_FILE"] = os.getenv("REQUESTS_CA_BUNDLE")
st.title("BudgiBot")


if "financial_goals" not in st.session_state:
    st.session_state["financial_goals"] = []

html_content = f"""
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2lgr0IFLzRMcMAzXul8gLU?utm_source=generator" width="50%" height="auto" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
"""
st.markdown(html_content, unsafe_allow_html=True)

st.sidebar.title("Set Your Financial Goals")
with st.sidebar.form(key='financial_goal_form'):
    goal_title = st.text_input("Goal Title")
    goal_description = st.text_area("Goal Description")
    submit_button = st.form_submit_button(label='Add Goal')

    if submit_button and goal_title and goal_description:
        start_date = datetime.date.today()
        st.session_state["financial_goals"].append({
            "title": goal_title,
            "description": goal_description,
            "start_date": start_date
        })
        st.sidebar.success("Goal added!")

        # Display GIF for a short period
        if 'gif_display' not in st.session_state:
            st.session_state['gif_display'] = False

        st.session_state['gif_display'] = True

        # Use JavaScript to make the GIF disappear after 3 seconds
        st.markdown("""
        <script>
        setTimeout(function(){
          var gif = document.getElementById('add-goal-gif');
          if(gif) gif.style.display = 'none';
        }, 3000);
        </script>
        <img id="add-goal-gif" src="https://gifdb.com/images/high/monkey-holding-funny-money-zvcravxz3f64eirx.gif" alt="Goal added" style="display: block; margin: 0 auto; width: 50%; height: auto;">
        """, unsafe_allow_html=True)

# Function to calculate days since goal started
def calculate_days_since(start_date):
    return (datetime.date.today() - start_date).days

# Create columns
left_col, right_col = st.columns(2)

# Left Column: Display financial goals
with left_col:
    st.subheader("Your Financial Goals")
    for idx, goal in enumerate(st.session_state["financial_goals"]):
        days_since = calculate_days_since(goal['start_date'])
        st.write(f"**{goal['title']}**: {goal['description']} - **Days since started**: {days_since}")

        # Option to end and remove goal
        if st.button(f'End Goal {idx}', key=f'end_goal_btn_{idx}'):
            st.session_state["financial_goals"].pop(idx)
            st.success(f"Goal '{goal['title']}' completed!")
            st.experimental_rerun()

with right_col:
    st.subheader("The Laughing Stocks")

    def random_budget_tip():
        tips = [
            "Tip: Save at least 20% of your income!",
            "Tip: Track your expenses daily!",
            "Tip: Avoid impulse purchases!",
            "Tip: Plan your meals to save on food costs!",
            "Tip: Set up an emergency fund!",
            "Fact: Creating a budget helps you control your spending!",
            "Fact: Average household debt is around $145,000.",
            "Fact: Most financial experts recommend having 3-6 months' worth of expenses in an emergency fund.",
            "Tip: Use cash instead of cards to manage your spending better!",
            "Pun: Why did the banker switch careers? He lost interest.",
            "Pun: Why is money called dough? Because we all knead it.",
            "Pun: Why did the tomato take out a loan? To ketchup on bills.",
            "Pun: How do you get a millionaire to laugh? Just add a decimal.",
            "Pun: What's a pirate's favorite way to handle money? Using a 'loot'enant.",
            "Pun: Why did the vampire invest in the stock market? He heard it was going through a blood bath.",
            "Pun: What do you get when you cross a banker with a fish? A loan shark.",
            "Pun: What's the best way to save money?  Start with a budget app and a sense of humor-just don't laugh all the way to the bank.",
            "Pun: I bought some shoes from a drug dealer...I don't know what he laced them with, but I've been saving money with every step!"
        ]
        return random.choice(tips)

    st.write(random_budget_tip())

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"
    
### Do not remove the above code ###
CONTENT_PROMPT = {
    "role": "system",
    "content": "you are a senior financial advisor with special expertise in budgeting and planning give concise, specific, and accurate budgeting advice, avoid using '$' just say dollars in reference to money"
}
client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=os.getenv("OPENAI_API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask your budgeting questions here!"): #prompt part
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[CONTENT_PROMPT] + [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
