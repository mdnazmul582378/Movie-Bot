from telethon import TelegramClient, events
import os

API_ID = 27447242  
API_HASH = "693c22b58ee3d6d73ea66d88172bd245" 
BOT_TOKEN = "7887571273:AAG5YixqdDOoWljVUG0AZRm1bmzuWLOfrlw"  

CHANNEL_ID = "@new4kmoviez"  

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("🔥 হ্যালো! আমি তোমার মুভি সার্চ বট! শুধু মুভির নাম দাও, আমি তোমার চ্যানেল থেকে খুঁজে আনবো!")

@bot.on(events.NewMessage)
async def movie_search(event):
    query = event.text.lower()  
    
    async for message in bot.iter_messages(CHANNEL_ID, search=query):
        await event.reply(f"🎬 **তোর মুভি পাওয়া গেছে!**\n\n{message.text}")
        return

    await event.reply("❌ দুঃখিত! তোমার মুভি খুঁজে পাইনি।")

bot.run_until_disconnected()
