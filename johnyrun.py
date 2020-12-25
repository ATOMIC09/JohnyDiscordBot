import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from time import sleep

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='(', description="Powered by Ai-Engine", intents=intents)
bot.remove_command('help')

# Listen
@bot.listen()
async def on_message(message):
    chatbot = ChatBot("Johny")
    conversation = [
        "Hello",
        "Hello, my name is Johny",
        "Nice to meet you",
        "How are you?",
        "Fine thanks, and you?",
        "I’m okay, thank you",
        "Where are you from?",
        "I’m from Thailand",
        "How old are you?",
        "I’m 0 years old",
        "When is your birthday?",
        "23th Dec 2020",
        "Do you have a mobile phone?",
        "Yes, I do",
        "No, I don't",
        "How long have you been here for? ",
        "What’s your nationality?",
        "Everybody can be my friend.",
        "So we’ve met again,eh?",
        "What have you been doing?",
        "Training",
        "Who is your favourite singer?",
        "I like hip-hop music",
        "What kind of music do you like?",
        "I like pop music",
        "I like electronic music",
        "What’s your favorite food?",
        "My favourite food is noodle",
        "I like rock music",
        "What’s your favorite movie?",
        "My favourite movie is Avenger",
        "My favourite movie is Interstellar",
        "I like jazz music",
        "My favourite movie is Avatar",
        "What’s your favorite sport?",
        "My favourite sport is chairball",
        "What animals do you like?",
        "My favourite sport is football",
        "My favourite sport is basketball",
        "I like cats",
        "My favourite sport is tennis",
        "My favourite sport is batminton",
        "I like dogs",
        "What kind of fruit do you like?",
        "Do you like bananas?",
        "I like watching TV",
        "I really like gardening",
        "I love the cinema",
        "I enjoy travelling",
        "I’m interested in photography",
        "I read a lot",
        "How many languages can you speak?",
        "Can you sing?",
        "Yes",
        "I’ll pay",
        "What do you want to eat?",
        "What are you looking for?",
        "I’m looking for shoes",
        "I’m just looking",
        "Can I try it on?",
        "It’s just right",
        "I’ll take this one",
        "I like it very much",
        "I’ll take it",
        "No",
        "This is the last piece!",
        "That seems expensive",
        "Do you have a less expensive one?",
        "How much is it?",
        "Can you give me a discount?",
        "This is a special price for you",
        "Do you deliver?",
        "Does it have a warranty?",
	    "I am good",
	    "That is good to hear",
	    "Thank you",
        "You are welcome",
        "Thanks for everything",
        "That’s not fair"
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    response = chatbot.get_response(textttt)
    output = str(response) + "\n"

    if message.author.id == bot.user.id:
	    return
    await message.channel.send(output)

# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Testing"))
	print('Johny is Running !!')

Token = os.environ["JohnyToken"]
bot.run(Token)