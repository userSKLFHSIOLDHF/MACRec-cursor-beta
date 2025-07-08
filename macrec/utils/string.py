# Description: Functions for string processing.

import re
from typing import Any, Union

def format_step(step: str) -> str:
    """Format a step string."""
    return f'Step {step}:'

def format_last_attempt(input: str, scratchpad: str, header: str) -> str:
    """Format the last attempt."""
    return f'{header}\n\nInput: {input}\n\nScratchpad: {scratchpad}'

def format_reflections(reflections: list[str], header: str) -> str:
    """Format reflections."""
    if len(reflections) == 0:
        return ''
    reflection_text = '\n\n'.join([f'Reflection {i + 1}: {reflection}' for i, reflection in enumerate(reflections)])
    return f'{header}\n\n{reflection_text}'

def format_history(history: list[dict]) -> str:
    """Format history."""
    if len(history) == 0:
        return ''
    history_text = []
    for i, turn in enumerate(history):
        history_text.append(f'Step {i + 1}:')
        if 'command' in turn:
            history_text.append(f'Command: {turn["command"]}')
        if 'observation' in turn:
            history_text.append(f'Observation: {turn["observation"]}')
        history_text.append('')
    return '\n'.join(history_text)

def format_chat_history(history: list[tuple[str, str]]) -> str:
    """Format chat history."""
    if len(history) == 0:
        return ''
    history_text = []
    for role, message in history:
        history_text.append(f'{role.capitalize()}: {message}')
    return '\n\n'.join(history_text)

def str2list(s: str) -> list[int]:
    """Convert a string to a list of integers."""
    if s == '':
        return []
    s = s.strip()
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1]
    return [int(x.strip()) for x in s.split(',') if x.strip() != '']

def get_avatar(agent_type: str) -> str:
    """Get the avatar for an agent type."""
    avatar_map = {
        'manager': '🤖',
        'analyst': '📊',
        'interpreter': '💬',
        'reflector': '🤔',
        'searcher': '🔍',
    }
    return avatar_map.get(agent_type.lower(), '🤖')

def format_dict_to_text(data: Union[dict, Any], indent: int = 0) -> str:
    """
    Convert a dictionary to user-friendly formatted text.
    
    Args:
        data: The dictionary or data to format
        indent: Current indentation level
    
    Returns:
        Formatted text string
    """
    if not isinstance(data, dict):
        return str(data)
    
    lines = []
    indent_str = "  " * indent
    
    for key, value in data.items():
        # Format the key (convert snake_case to Title Case)
        formatted_key = key.replace('_', ' ').title()
        
        if isinstance(value, dict):
            # For nested dictionaries, add a header and format recursively
            lines.append(f"{indent_str}**{formatted_key}:**")
            lines.append(format_dict_to_text(value, indent + 1))
        elif isinstance(value, list):
            # For lists, format each item
            lines.append(f"{indent_str}**{formatted_key}:**")
            for i, item in enumerate(value, 1):
                if isinstance(item, dict):
                    lines.append(f"{indent_str}  {i}. {format_dict_to_text(item, indent + 2)}")
                else:
                    lines.append(f"{indent_str}  {i}. {item}")
        else:
            # For simple values, format as key-value pair
            lines.append(f"{indent_str}**{formatted_key}:** {value}")
    
    return "\n".join(lines)

def format_comparison_dict(data: dict) -> str:
    """
    Special formatter for comparison dictionaries with similarities and differences.
    
    Args:
        data: Comparison dictionary
    
    Returns:
        Formatted comparison text
    """
    if not isinstance(data, dict) or 'comparison' not in data:
        return format_dict_to_text(data)
    
    comparison = data['comparison']
    lines = []
    
    for category, content in comparison.items():
        if isinstance(content, dict):
            # Format category header
            category_title = category.replace('_', ' ').title()
            lines.append(f"## {category_title}")
            lines.append("")
            
            # Handle similarities and differences specially
            similarities = content.get('similarities', '')
            differences = content.get('differences', '')
            
            # Add individual items
            for key, value in content.items():
                if key not in ['similarities', 'differences']:
                    item_name = key.replace('_', ' ').title()
                    lines.append(f"**{item_name}:** {value}")
                    lines.append("")
            
            # Add similarities and differences if they exist
            if similarities:
                lines.append("**Similarities:** " + similarities)
                lines.append("")
            if differences:
                lines.append("**Differences:** " + differences)
                lines.append("")
    
    return "\n".join(lines)
