from dotenv import load_dotenv
#we have the open_api_key in the .env file. We use the dotenv.
# llm = OpenAI(openai_api_key="...")
load_dotenv()
#Frontend Streamlit https://docs.streamlit.io/library/api-reference
import streamlit as st 
#llm model
from langchain.llms import OpenAI
#chat model
from langchain.chat_models import ChatOpenAI

# # initiate LLM
# llm = OpenAI()
# # result = llm.predict("hi!")
# # print(result)

#initiate Chat model
chat_model = ChatOpenAI()
# result2=chat_model.predict("hi!")
# # print(result2)

st.title('AI POET')
theme = st.text_input('Enter the theme of the poet')

if st.button('Write poem'):
    with st.spinner('Generating Poem . . . '):
        result = chat_model.predict("write me a poem on" + theme)
        st.write(result)









