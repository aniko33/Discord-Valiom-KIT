import discord
from discord.ext import commands 
import time

bot = commands.Bot(command_prefix="./")

print("""

░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░░░░░░░██████╗░░█████╗░████████╗  ██████╗░██╗░░░██╗
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝
╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝█████╗██████╦╝██║░░██║░░░██║░░░  ██████╦╝░╚████╔╝░
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗╚════╝██╔══██╗██║░░██║░░░██║░░░  ██╔══██╗░░╚██╔╝░░
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║░░░░░░██████╦╝╚█████╔╝░░░██║░░░  ██████╦╝░░░██║░░░
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░

░█████╗░███╗░░██╗██╗██╗░░██╗░█████╗░
██╔══██╗████╗░██║██║██║░██╔╝██╔══██╗
███████║██╔██╗██║██║█████═╝░██║░░██║
██╔══██║██║╚████║██║██╔═██╗░██║░░██║
██║░░██║██║░╚███║██║██║░╚██╗╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝░╚════╝░

""")

token = input ("Token: ")
message = input ("Message: ")
print ("./startspam")

@bot.command()
async def startspam(ctx):
    while 130 == 130:
        await ctx.send(message)
        await ctx.send(message)
        await ctx.send(message)
        await ctx.send(message)
        print ("send")

bot.run(token)