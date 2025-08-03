import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.genai import types
from google.adk.tools.google_api_tool import GmailToolset

load_dotenv()

MODEL = "gemini-2.0-flash-001"
AGENT_APP_NAME = 'enterpriseagent'

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
SEARCH_PROMPT = os.getenv('SEARCH_PROMPT')
LATEST_NUMBER_OF_MESSAGES_TO_SEARCH_FOR = os.getenv('LATEST_NUMBER_OF_MESSAGES_TO_SEARCH_FOR')

gmail_toolset = GmailToolset(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        tool_filter=["gmail_users_messages_list", "gmail_users_messages_get", "gmail_users_messages_attachments_get", "gmail_users_messages_import"]
)
email_subject = "Security Alert",
root_agent = Agent(
        model=MODEL,
        name=AGENT_APP_NAME,
        description="You are helpful assistant helping a client to filter the gmail messages based on the instruction. You can start executing the instruction when user types 'filter' ",
        instruction=f"Instruction: In kruise.redalert@gmail.com, {SEARCH_PROMPT}. Always limit your search to the latest {LATEST_NUMBER_OF_MESSAGES_TO_SEARCH_FOR} messages",
        tools = [gmail_toolset]
)