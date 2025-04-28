import telebot
import threading
import time
import random

# Replace this with your bot token
TOKEN = '7490093532:AAGnn9iuPNBe2RDFSUs35OwKgUjUg6wNT4k'
bot = telebot.TeleBot(TOKEN)

# Load your 100 quotes
quotes = [
    "Believe you can and you're halfway there.",
    "You're capable of amazing things.",
    "Keep going, you're doing great!",
    "Stay positive, work hard, make it happen.",
    "Doubt kills more dreams than failure ever will.",
    "Every day is a second chance.",
    "You are stronger than you think.",
    "Dream it. Wish it. Do it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn't come from what you do occasionally, it comes from what you do consistently.",
    "Little things make big days.",
    "It always seems impossible until it's done.",
    "Difficult roads often lead to beautiful destinations.",
    "Believe in yourself and all that you are.",
    "Your only limit is your mind.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t stop until you’re proud.",
    "Great things never come from comfort zones.",
    "Push through the pain, it’s worth it.",
    "The best view comes after the hardest climb.",
    "You don’t have to be perfect to be amazing.",
    "You are enough just as you are.",
    "Mistakes are proof that you are trying.",
    "Believe in the magic inside you.",
    "Small steps every day.",
    "Stay strong. The weekend is coming!",
    "You were born to be real, not perfect.",
    "Success is what happens after you survive all your mistakes.",
    "You are doing better than you think.",
    "You’ve got this.",
    "Everything you need is already inside you.",
    "Be fearless in the pursuit of what sets your soul on fire.",
    "The comeback is always stronger than the setback.",
    "You’re one step closer every day.",
    "Stay patient and trust your journey.",
    "The secret of getting ahead is getting started.",
    "It’s a slow process, but quitting won’t speed it up.",
    "Never give up on things that make you smile.",
    "Train your mind to see the good in every situation.",
    "Difficulties in life are intended to make us better, not bitter.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "Positive mind. Positive vibes. Positive life.",
    "Be proud of how hard you are trying.",
    "Work hard in silence. Let success make the noise.",
    "Success is no accident.",
    "Fall seven times, stand up eight.",
    "You didn’t come this far to only come this far.",
    "Grow through what you go through.",
    "When you feel like quitting, think about why you started.",
]
# To store the user's chat ID
user_chat_id = None

# Function to send random quotes every 30 minutes
def send_quotes_forever():
    while True:
        if user_chat_id:  # Only if someone has started
            random_quote = random.choice(quotes)
            try:
                bot.send_message(user_chat_id, random_quote)
            except Exception as e:
                print(f"Error sending message: {e}")
        time.sleep(1800)  # Sleep for 30 minutes (1800 seconds)

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user_chat_id
    user_chat_id = message.chat.id
    bot.reply_to(message, "Heyyy 👋! Welcome to your personal motivation bot! ✨\nYou'll get a random quote every 30 minutes!\nYou can also type /quote to get one right now! 🚀")

# /quote command handler
@bot.message_handler(commands=['quote'])
def send_random_quote(message):
    if message.chat.id == user_chat_id:
        random_quote = random.choice(quotes)
        bot.send_message(user_chat_id, random_quote)
    else:
        bot.reply_to(message, "You need to /start first before you can get a quote! 😉")

# Start the quote-sending thread
threading.Thread(target=send_quotes_forever, daemon=True).start()

# Start the bot
bot.infinity_polling()
