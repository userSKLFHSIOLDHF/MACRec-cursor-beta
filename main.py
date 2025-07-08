import argparse
import sys
import os
from loguru import logger
from macrec.tasks import *
from macrec.utils import init_openai_api, init_google_colab_secrets, read_json
from macrec.tasks.base import Task

os.environ["GOOGLE_API_KEY"] = "AIzaSyCkKKnTj1T0evVy6kmvZ8AciKZvyja6QKk"
os.environ["GOOGLE_CSE_ID"] = "b555d8f9855ad4f4b"

def main():
    # Initialize Google Colab secrets first
    init_google_colab_secrets()
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='task', help='Task to run')
    
    # Add task parsers
    for task_class in Task.__subclasses__():
        task_class.parse_task_args(subparsers.add_parser(task_class.__name__.lower()))
    
    args = parser.parse_args()
    
    if args.task is None:
        parser.print_help()
        sys.exit(1)
    
    # Initialize API if config is provided
    if hasattr(args, 'api_config'):
        init_openai_api(read_json(args.api_config))
    
    # Get task class and run
    task_class = next(task_class for task_class in Task.__subclasses__() if task_class.__name__.lower() == args.task)
    task = task_class()
    task.launch()

if __name__ == '__main__':
    main()
