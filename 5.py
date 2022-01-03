import streamlit as st
import datetime
import pandas as pd
import numpy as np
import random
import os
from requests import get

endpoint = "https://api-model-engine-chatbot.juanengml.repl.co/bot"


st.set_page_config(
  page_title="Análise Comportamento Consumidor",
  page_icon="💰",
  layout="centered",
  initial_sidebar_state="expanded",)

def main(): 
    st.title(" 🤖 Meu ChatBot")
    
    me = st.text_area(" 😃 Me:", value="Escreva", key=None)
    if st.button(" ✉️ Enviar") == True:
           data = {'pergunta': me}
           r = get(endpoint,data).json()
          # st.write(data)
           st.write("acc: ",r['bot']['confidence'])
           msg = r['bot']['GeorgeBot']
           st.text_area(" 🤖 Bot:",msg, key=None)

        
if __name__ == "__main__":
    main()
