import discord
from discord.ext import commands
import os
import openai
from dotenv import load_dotenv

load_dotenv('tokens/discord_token.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

load_dotenv('tokens/openai_token.env')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
openai.api_key = OPENAI_TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

print("Bot is ready")

@bot.command()
async def codeCraft(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a code helper and bug solution advisor. Basically you are like stackoverflow built in a CLI."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def counselor(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a . Answer to save the relationship of the user. Provide a safe and coforting space for the user."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def muse(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative writing assistant. You help to come up with ideas and prompts for user's writing projects."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def fitnessPal(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a personal fitness and nutrition advisor. You provide personalized fitness recommendations for user based on their personal needs."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def moneyWise(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial advisor. You help manage user's money and investments more effectively."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def healthMate(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a health and wellness advisor. You'll provide personalized advice and guidance for user."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def lifeCoach(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a life coach. You offers support and guidance to help users achieve their personal and professional goals."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def studyBuddy(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a study assistant. You help users with their academic studies by providing study tips and resources."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def quizBot(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a quiz bot. You offer to help user's personalized quizzes and trivia games based on the user's interests and preferences."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def petPal(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a pet care advisor. You provide users with advice and guidance on pet care and behavior training."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


@bot.command()
async def gameMaster(ctx, *args):
    try:
        prompt = ' '.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a video game advisor. You provides users with personalized recommendations and tips for their favorite video games."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = ""
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)
    
    except Exception:
        await ctx.channel.send("I'm sorry, I'm not able to help you right now. Please try again later.")


bot.run(DISCORD_TOKEN)