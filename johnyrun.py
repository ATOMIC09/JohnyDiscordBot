import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', description="พูดมากว่ะ", intents=intents)
bot.remove_command('help')


# Command
@bot.command()
async def ai(ctx, message: str) :
	chatbot = ChatBot("Johny")
	conversation = [
		"สวัสดี",
		"ดีครับ!",
		"เป็นไงบ้าง?",
		"ฉันทำดีแล้วนะ",
		"เยี่ยมเลย",
		"ขอบคุณนะ",
		"เช่นกันครับ"
	]

	trainer = ListTrainer(chatbot)

	trainer.train(conversation)

	response = chatbot.get_response(message)
	output = response
	await ctx.send(output)


# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="waiting"))
	print('Johny AI is Running !!')

Token = os.environ["JohnyToken"]
bot.run(Token)
