from dotenv import load_dotenv
load_dotenv()
from langchain.llms import OpenAI
#we have the open_api_key in the .env file. We use the dotenv.
# llm = OpenAI(openai_api_key="...")
#Frontend Streamlit https://docs.streamlit.io/library/api-reference
import streamlit as st 
#llm model
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


# Streamlit 
# Run "streamlit run main.py"
st.title('AI POET')
theme = st.text_input('Enter the theme of the poet')

if st.button('Write poem'):
    with st.spinner('Generating Poem . . . '):
        result = chat_model.predict("write me a poem on" + theme)
        st.write(result)









