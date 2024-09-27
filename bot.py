from pyrogram import Client, filters

# Your API credentials from my.telegram.org
api_id = "12321125"  # Replace with your API ID
api_hash = "6a34b69aa63177ec36f8d9b24c296f40"  # Replace with your API Hash

# Start the Pyrogram Client using your account (userbot)
app = Client("mybot", api_id=api_id, api_hash=api_hash)

# Source and target channel details
SOURCE_CHANNEL_ID = -1002369069695  # Replace with source channel's numeric ID
TARGET_CHANNEL_ID = -1002252994329  # Replace with target channel's numeric ID

# Function to forward messages without forward tag
@app.on_message(filters.chat(SOURCE_CHANNEL_ID))
async def forward_message(client, message):
    if message.text:
        await client.send_message(chat_id=TARGET_CHANNEL_ID, text=message.text)

    elif message.photo:
        await client.send_photo(chat_id=TARGET_CHANNEL_ID, photo=message.photo.file_id, caption=message.caption)

    elif message.video:
        await client.send_vide
