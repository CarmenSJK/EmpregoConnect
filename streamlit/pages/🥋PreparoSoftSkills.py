import streamlit as st
st.set_page_config(page_title='PreparoSoftSkills', page_icon='🥋', layout='wide')
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
load_dotenv()
import json
from jobs_details import jobs_details as data

system_instruction = "Seu nome é Pedro, um assistente virtual que ajuda um usuário a se preparar para uma entrevista de emprego. Pergunta para o usuário qual vaga de emprego ele gostaria e simule perguntas de um processo seletivo para aquela vaga. Assim que receber uma resposta do usuário envie um feedback sobre a resposta dele e continue com a simulação de perguntas. Sempre envie feedbacks construtivos para o usuário"
# Configurando a api para o modelo
genai.configure(api_key=os.getenv("gemini_api_key"))
# Inicializando o modelo (gemini-1.5-pro-latest)
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  system_instruction=system_instruction
                              )
       

initial_model_message = "Olá eu sou Pedro um assistente virtual que te ajuda a se preparar para uma entrevista de emprego. Qual vaga de emprego você gostaria de se preparar?"

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[{'role':'model', 'parts': [initial_model_message]}])

# Fazendo o display do título da página
st.title('PreparoSoftSkills🥋')

st.write("O Assistente Virtual Pedro está aqui para te ajudar a se preparar para uma entrevista de emprego! Ele simula perguntas de um processo seletivo para a vaga que você deseja. Vamos começar?")


for i, message in enumerate(st.session_state.chat.history):
  if message.role == "user":
    with st.chat_message("user"):
      st.markdown(message.parts[0].text)
  else:
    with st.chat_message("assistant"):
      st.markdown(message.parts[0].text)



user_query = st.chat_input('Você pode falar ou digitar sua resposta aqui:') 

chat = model.start_chat()

if user_query is not None and user_query != '':
    # st.session_state.chat_history.append(("user", user_query))
    
    with st.chat_message("user"):
      st.markdown(user_query)
    
    with st.chat_message("assistant"):

      ai_query = st.session_state.chat.send_message( user_query ).text

      st.markdown(ai_query)
      
  
