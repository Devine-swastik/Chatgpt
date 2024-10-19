import os

# Telegram Bot Configuration
API_ID = int(os.getenv('API_ID', '29644708'))
API_HASH = os.getenv('API_HASH', '0db39046c635489ccb05d9a0ca395c9f')
BOT_TOKEN = os.getenv('BOT_TOKEN', '7866262568:AAG-DzguR8kK6B7dzFQW53RFxoUUmeLzQsg')
BOT_NAME = os.getenv('BOT_NAME', 'Chat Gpt')
BOT_USERNAME = os.getenv('BOT_USERNAME', 'Devine_chatgpt_bot')
OWNER_ID = int(os.getenv('OWNER_ID', '6338745050'))
OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'devine4x')
UPDATE_CHANNEL = os.getenv('UPDATE_CHANNEL', '-1001835308211')
SUPPORT_GROUP = os.getenv('SUPPORT_GROUP', '-1002082533215')

# OpenAI Configuration
OPENAI_KEY = os.getenv('OPENAI_KEY', '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')

# MongoDB Configuration
MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb+srv://godofgenjutsu9229:K2HFlJA7EbSZjC6Z@cluster0.l6zam.mongodb.net/?retryWrites=true&w=majority')

# Check if all required environment variables are set
if not all([API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, OWNER_ID, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP, MONGODB_URL]):
    raise RuntimeError("Please set all required environment variables: API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, OWNER_ID, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP, MONGODB_URL")
