import asyncio
from telethon.sync import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins
from dotenv import load_dotenv
import os
from operator import itemgetter

# Load environment variables
load_dotenv()

# Replace with your API credentials
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
chat = os.getenv("CHAT_ID")
limit = int(os.getenv("LIMIT"))


client = TelegramClient('session', api_id, api_hash)
client.start()


def get_admins():
    # Connect to the client
    
    # Get the list of admins
    admins = client.get_participants(chat, filter=ChannelParticipantsAdmins)

    # Return the list of admins
    return admins

# Run the async function
#admins = await get_admins()
admins = get_admins()

# Define a dictionary to store the count for each admin
admin_count = {}

# Iterate over the last messages and increment the count for the sender if they are an admin
for message in client.iter_messages(chat, limit=limit):
    if message.sender in admins:
        # Get the name of the sender
        if message.sender.username:
            name = '@' + message.sender.username
        else:
            name = ''
            if message.sender.first_name:
                name = message.sender.first_name
            if message.sender.last_name:
                name += ' ' + message.sender.last_name
            if name == '':
                name = message.sender
        # If the name is already in the dictionary, increment the count by one
        msgln = 0
        if message.message:
            msgln += len(message.message)
        else:
            msgln = 1
            
        if name in admin_count:
            admin_count[name] += msgln
        # Otherwise, initialize the count to one
        else:
            admin_count[name] = msgln
        

# Print the result as a list of names and counts
print(f'تعداد پیام‌های ارسال شده توسط هر مدیر در آخرین {limit} پیام:')
print('برحسب تعداد کلمات ارسال شده')
admin_count = dict(sorted(admin_count.items(), key=itemgetter(1),reverse=True))
for name, count in admin_count.items():
    print(f'- {name}: {count}')
