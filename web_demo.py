import os
from macrec.pages.demo import demo
from macrec.utils import init_google_colab_secrets

# Initialize Google Colab secrets before starting the demo
init_google_colab_secrets()

if __name__ == '__main__':
    demo()
