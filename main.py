from pyrogram import Client, filters

app = Client(
    "video_reply_bot",
    bot_token="8544033095:AAGOw6vrqnGS4gYU9QxaUcYsDQREustNDxM",
    api_id=37107854,
    api_hash="b7bd75330bf9f058feeec3ca7e31b1ad"
)

@app.on_message(filters.video)
def reply_video(client, message):
    message.reply_text("✅ Video received successfully!")

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Bot is online. Send me a video.")

app.run()
