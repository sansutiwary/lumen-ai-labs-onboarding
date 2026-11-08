from dotenv import load_dotenv
load_dotenv()
import streamlit as st

from langchain_groq import ChatGroq

llm=ChatGroq(model="openai/gpt-oss-120b")
# while True:
#     ques=input("User :")

#     if ques.lower() in ["no","exite","stop"]:

#         print("Ok thanks")
#         break
#     else:
#         res=llm.invoke(ques)
#         print(res.content)
st.title("🤖 AI Q & N bot")
st.markdown("MY Q&A bot usign langchain and openAI")
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)


#history=[]
quary=st.chat_input("Ask anything")
if quary:
    #history.append({"role":"user","content":quary})
    st.session_state.messages.append({"role":"user","content":quary})
    st.chat_message("user").markdown(quary)
    res=llm.invoke(st.session_state.messages)
    #history.append({"role":"ai","content":res.content})
    st.chat_message("ai").markdown(res.content)
    
    st.session_state.messages.append({"role":"ai","content":res.content})
