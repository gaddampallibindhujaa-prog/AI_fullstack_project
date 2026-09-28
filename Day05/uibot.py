import ollama
import streamlit as st
import time
st.markdown("# Welcome to my ChatBot App!!! :sunflower:")
with st.sidebar:
    st.header("Chat Settings ⚙️")

    if st.button("Clear Chat🚮"):
       st.session_state.messages=[]
       st.header("_Chat is Cleared_ :sunglasses:")
    personalities={
       "Study assistant 📖":"Answer question like you are explaining to an engineering student",
       "English Tutor 👩🏻‍🏫":"Answer question like you are explaining to a student who is learning english ",
       "Story Generator 🗣️":"answer like you are giving story to a 5 year old"
    }
    personality =st.selectbox("Select a personality",personalities.keys())
    uploaded_file = st.file_uploader("Choose a file 📂")
    try:
       if uploaded_file is not None:
          st.badge("File Uploaded Successfully 🎉", icon=":material/check:", color="green")
          if st.button("Read Context"):
             context=uploaded_file.read().decode("utf-8")
             st.write(context)
    except:
       st.error("Please Choose Correct Extension💀")
if "messages" not in st.session_state:
   st.session_state.messages = []
for msg in st.session_state.messages:
   with st.chat_message(msg["role"]):
      st.write(msg["content"])
question = st.chat_input("You: ")
if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.chat_message("user"):
      st.write(question)
    with st.spinner("Wait for it...", show_time=True):
       response = ollama.chat( 
        model = "llama3.2:3b",
        messages= [
        {"role": "system","content": personalities[personality]}]
        +st.session_state.messages)
    st.session_state.messages.append(
        {"role": "assistant",
            "content": response["message"]["content"]
        }
    ) 
    with st.chat_message("assistant"):
     ( "AI",response["message"]["content"])

  
    
       
