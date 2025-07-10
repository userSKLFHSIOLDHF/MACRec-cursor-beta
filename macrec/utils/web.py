import streamlit as st
from typing import Optional
import json
from macrec.utils.string import dict_to_markdown

def add_chat_message(role: str, message: str | dict, avatar: Optional[str] = None):
    """Add a chat message to the chat history.

    Args:
        `role` (`str`): The role of the message.
        `message` (`str` | `dict`): The message to be added.
        `avatar` (`Optional[str]`): The avatar of the agent. If `avatar` is `None`, use the default avatar.
    """
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Handle dictionary messages by converting to user-friendly Markdown
    if isinstance(message, dict):
        display_message = dict_to_markdown(message)
    else:
        display_message = str(message)
    
    st.session_state.chat_history.append({'role': role, 'message': message})
    if avatar is not None:
        st.chat_message(role, avatar=avatar).markdown(display_message)
    else:
        st.chat_message(role).markdown(display_message)

def get_color(agent_type: str) -> str:
    """Get the color of the agent.

    Args:
        `agent_type` (`str`): The type of the agent.
    Returns:
        `str`: The color name of the agent.
    """
    if 'manager' in agent_type.lower():
        return 'rainbow'
    elif 'reflector' in agent_type.lower():
        return 'orange'
    elif 'searcher' in agent_type.lower():
        return 'blue'
    elif 'interpreter' in agent_type.lower():
        return 'green'
    elif 'analyst' in agent_type.lower():
        return 'red'
    else:
        return 'gray'
