import json 
import discord
from discord.ext import commands 
from datetime import datetime

from user_input import user_interface
from api_checker import staked_amount

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

file_path = 'stats/stats.json'
with open(file_path, 'r') as file:
    config = json.load(file)


@bot.command()
async def p(ctx, *arg):
    
    with open(file_path,'r') as file: 
        config = json.load(file)
    print ("--------------------------------")
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - Command by {ctx.author.name}") 
    args_str = ' '.join(arg) #*arg is a list, i want a string with spaces
    asked_addies = user_interface(args_str)
    staked = staked_amount(asked_addies)

    staked_value = {}
    annual_apr = {}

    for project in staked: 
        staked_value [project] = staked[project] * config[project]['Price']
        
    for project in staked_value: 
        annual_apr[project] = staked_value[project] * config[project]['APR']/100

    total_income = 0 
    for project in annual_apr: 
        total_income += annual_apr[project]
    await ctx.send(f"**Total income per year**\n{round(total_income,2)}$")
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - /p command executed ✅")




@bot.command()
async def f(ctx, *arg):

    with open(file_path,'r') as file: 
        config = json.load(file)
    
    print ("--------------------------------")
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - Command by {ctx.author.name}") 
    args_str = ' '.join(arg) #*arg is a list, i want a string with spaces
    asked_addies = user_interface(args_str)
    staked = staked_amount(asked_addies)

    staked_value = {}
    annual_apr = {}

    for project in staked:
        staked_value[project] = staked[project] * config[project]['Price']

    for project in staked_value:
        annual_apr[project] = staked_value[project] * config[project]['APR'] / 100

    total_income = 0
    for project in annual_apr:
        total_income += annual_apr[project]

    message = "Annual Incomes:\n\n"
    message += "Project         | Annual Income\n"
    message += "----------------|--------------\n"

    for project in annual_apr:
        message += f"{project:<15} | ${round(annual_apr[project], 2):<12}\n"
    
    message += "\n"
    message += f"Total Income per Year: ${round(total_income, 2)}"

    await ctx.send(f"```\n{message}\n```")
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - /f command executed ✅")

@bot.command()
async def helpp(ctx):
    await ctx.send(f"Send /f and one or more cosmos addresses seperated with space\nThe bot finds the addresses from other cosmos networks and calculates your Annual Income")

bot.run("INSERT DISCORD BOT TOKEN")


