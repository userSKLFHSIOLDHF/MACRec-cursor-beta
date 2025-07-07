from macrec.tools.base import Tool
from macrec.tools.summarize import TextSummarizer
from macrec.tools.wikipedia import Wikipedia
from macrec.tools.info_database import InfoDatabase
from macrec.tools.interaction import InteractionRetriever
from langchain_google_community import GoogleSearchAPIWrapper

TOOL_MAP: dict[str, type] = {
    'summarize': TextSummarizer,
    'wikipedia': Wikipedia,
    'info': InfoDatabase,
    'interaction': InteractionRetriever,
    'google': GoogleSearchAPIWrapper
}
