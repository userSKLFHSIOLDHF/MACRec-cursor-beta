import streamlit as st
from loguru import logger
import json

from macrec.systems import ChatSystem, CollaborationSystem
from macrec.utils import add_chat_message

def chat_page(system: ChatSystem | CollaborationSystem) -> None:
    for chat in st.session_state.chat_history:
        if isinstance(chat['message'], str):
            st.chat_message(chat['role']).markdown(chat['message'])
        elif isinstance(chat['message'], list):
            with st.chat_message(chat['role']):
                for message in chat['message']:
                    st.markdown(f'{message}')
        elif isinstance(chat['message'], dict):
            with st.chat_message(chat['role']):
                st.markdown("```json\n" + json.dumps(chat['message'], indent=2, ensure_ascii=False) + "\n```")
        else:
            logger.error(f"Unexpected message type in chat history: {type(chat['message'])}, value: {chat['message']}")
            st.warning(f"Skipped a message due to unexpected type: {type(chat['message'])}")
            continue
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
