import logging
from pyrogram import Client, filters

logging.basicConfig(level=logging.DEBUG)

# Your API credentials
api_id = "12321125"  # Replace with your API ID
api_hash = "6a34b69aa63177ec36f8d9b24c296f40"  # Replace with your API Hash

app = Client("mybot", api_id=api_id, api_hash=api_hash)

SOURCE_CHANNEL_ID = -1002369069695  # Replace with source channel's numeric ID
TARGET_CHANNEL_ID = -1002252994329  # Replace with target channel's numeric ID

@app.on_message(filters.chat(SOURCE_CHANNEL_ID))
async def forward_message(client, message):
    print(f"Received message: {message.text or message.photo or message.video or message.audio or message.document or message.sticker or message.voice or message.location}")
    try:
        if message.text:
            await client.send_message(chat_id=TARGET_CHANNEL_ID, text=message.text)

        elif message.photo:
            await client.send_photo(chat_id=TARGET_CHANNEL_ID, photo=message.photo.file_id, caption=message.caption or "")

        elif message.video:
            await client.send_video(chat_id=TARGET_CHANNEL_ID, video=message.video.file_id, caption=message.caption or "")

        # Add similar blocks for other message types...

    except Exception as e:
        print(f"Error forwarding message: {e}")

if __name__ == "__main__":
    app.run()
