# Description: Initialization functions.

import os
import random
import numpy as np
import torch
from loguru import logger

def init_openai_api(api_config: dict):
    """Initialize OpenAI API configuration."""
    os.environ['OPENAI_API_KEY'] = api_config['api_key']
    os.environ['OPENAI_API_BASE'] = api_config['api_base']
    logger.info('OpenAI API initialized.')

def init_google_colab_secrets():
    """Initialize API keys from Google Colab secrets."""
    try:
        # Try to import Google Colab secrets
        from google.colab import userdata
        
        # Initialize DeepSeek API from secrets
        try:
            deepseek_api_key = userdata.get('DEEPSEEK_API_KEY')
            if deepseek_api_key:
                os.environ['OPENAI_API_KEY'] = deepseek_api_key
                logger.info('DeepSeek API key loaded from Google Colab secrets.')
        except Exception as e:
            logger.warning(f'Could not load DeepSeek API key from secrets: {e}')
        
        # Initialize Google API from secrets
        try:
            google_api_key = userdata.get('GOOGLE_API_KEY')
            if google_api_key:
                os.environ['GOOGLE_API_KEY'] = google_api_key
                logger.info('Google API key loaded from Google Colab secrets.')
        except Exception as e:
            logger.warning(f'Could not load Google API key from secrets: {e}')
            
        # Initialize Google CSE ID from secrets
        try:
            google_cse_id = userdata.get('GOOGLE_CSE_ID')
            if google_cse_id:
                os.environ['GOOGLE_CSE_ID'] = google_cse_id
                logger.info('Google CSE ID loaded from Google Colab secrets.')
        except Exception as e:
            logger.warning(f'Could not load Google CSE ID from secrets: {e}')
            
    except ImportError:
        logger.info('Google Colab not detected, using environment variables or config files.')
    except Exception as e:
        logger.warning(f'Error initializing Google Colab secrets: {e}')

def init_all_seeds(seed: int = 0) -> None:
    """Initialize all random seeds."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    logger.info(f'All seeds initialized with seed {seed}.')
