import os
from langchain_openai import ChatOpenAI
import streamlit as st

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Title and Description
st.title("Bhuman-GPT")
st.markdown("Generate Linkedin posts on any topic like [Bhuman Pandita](https://www.linkedin.com/in/bhumanpandita/)")
st.markdown("Powered by GPT-4o-mini fine-tuned model")

# Text input for topic
topic = st.text_input("Please enter your topic")

st.code(""" 
            Try:
            What are TRIGGERS in postgres?
            What are Window Functions?
        """,language= None)

# Initialize the models
gpt_base_model = ChatOpenAI(model = "gpt-4o-mini")
gpt_finetuned_model = ChatOpenAI(model = "ft:gpt-4o-mini-2024-07-18:personal::AL6AB1Ao")

def generate_linked_post(prompt,gpt_base_model=gpt_base_model,gpt_finetuned_model=gpt_finetuned_model):
    response1 = gpt_base_model.invoke(prompt)
    response2 = gpt_finetuned_model(prompt)
    return response1,response2

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating Posts..."):
            base_response,ft_response = generate_linked_post(f"Write me a LinkedIn Post on {topic}")
        
        col1,col2 = st.columns(2)

        with col1:
            st.subheader("Base Model (gpt-4o-mini)")
            st.markdown(f'<div class ="output-text"{base_response}</div>',unsafe_allow_html = True)
        with col2:
            st.subheader("Bhuman-GPT Model (Fine-tuned model)")
            st.markdown(f'<div class ="output-text"{ft_response}</div>',unsafe_allow_html = True)
    else:
        st.warning("Please enter a topic before generating posts")
