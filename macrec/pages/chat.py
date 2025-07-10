import streamlit as st
from loguru import logger
import json

from macrec.systems import ChatSystem, CollaborationSystem
from macrec.utils import add_chat_message
from macrec.utils.string import dict_to_markdown

def chat_page(system: ChatSystem | CollaborationSystem) -> None:
    for chat in st.session_state.chat_history:
        if isinstance(chat['message'], str):
            st.chat_message(chat['role']).markdown(chat['message'])
        elif isinstance(chat['message'], list):
            with st.chat_message(chat['role']):
                for message in chat['message']:
                    st.markdown(f'{message}')
        elif isinstance(chat['message'], dict):
            # Handle dictionary responses by converting to user-friendly Markdown
            formatted_message = dict_to_markdown(chat['message'])
            st.chat_message(chat['role']).markdown(formatted_message)
        else:
            # Convert any other type to string
            st.chat_message(chat['role']).markdown(str(chat['message']))
    logger.debug('Initialization complete!')
    if prompt := st.chat_input():
        add_chat_message('user', prompt)
        with st.chat_message('assistant'):
            st.markdown('#### System is running...')
            response = system(prompt)
            st.session_state.chat_history.append({
                'role': 'assistant',
                'message': ['#### System is running...'] + system.web_log
            })
        add_chat_message('assistant', response)
        st.rerun()
