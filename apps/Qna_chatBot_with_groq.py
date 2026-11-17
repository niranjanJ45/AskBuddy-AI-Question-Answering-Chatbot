#LLM               
#TOOL - gOOGLE    
#AGENT
#MEMORY
#python -m streamlit run .\Qna_chatBot_with_groq.py----->run the project 
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

llm = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()
tools = [search.run] 

if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = [] 

agent = create_agent(
    model=llm, 
    tools=tools, 
    checkpointer=st.session_state.memory,
    system_prompt=(
        "You are a helpful assistant. Answer the user's actual question directly. "
        "Use Google Search for current information or when reliable sources are needed, "
        "then summarize the results in a clear answer instead of repeating search snippets. "
        "For greetings and questions that do not need web research, respond conversationally."
    )
)

print(st.session_state.memory)

### Building Web Interface using Streamlit
st.title("QuikAnswer - Answers at the speed of thought")

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything ?")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query}) 

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = agent.invoke(
                {"messages": [{"role": "user", "content": query}]},
                {"configurable": {"thread_id": "1"}}
            )

        answer = response["messages"][-1].content
        if not isinstance(answer, str):
            answer = "\n".join(
                block["text"]
                for block in answer
                if isinstance(block, dict) and isinstance(block.get("text"), str)
            )
        st.markdown(answer)

    st.session_state.history.append({"role": "assistant", "content": answer})