
print(credits)
import discord,json,os,random
from discord.ext import commands

with open("config.json") as file:
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot is Running")
@bot.command()
async def stock(ctx):
    stockmenu = discord.Embed(title="Stock",description="")
    for filename in os.listdir("Main/Accounts/"):
        with open("Main/Accounts/"+filename) as f: 
            ammount = len(f.read().splitlines())
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","")
            stockmenu.description += f"*{name}* - {ammount}\n"
    await ctx.send(embed=stockmenu)



@bot.command()
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Invalid command")
    else:
        name = name.lower()+".txt" 
        if name not in os.listdir("Main/Accounts/"): 
            await ctx.send(f"Invaild Command")
        else:
            with open("Main/Accounts/"+name) as file:
                lines = file.read().splitlines() 
            if len(lines) == 0: 
                await ctx.send("Out of Stock!")
            else:
                with open("Main/Accounts/"+name) as file:
                    account = random.choice(lines)
                try:
                    await ctx.author.send(f"Rose Alts: {str(account)}",delete_after=delete)
                except:
                    await ctx.send("Failed To Dm")
                else:
                    await ctx.send("Account Sent to Your Dms!")
                    with open("Main/Accounts/"+name,"w") as file:
                        file.write("")
                    with open("Main/Accounts/"+name,"a") as file:
                        for line in lines: 
                            if line != account:
                                file.write(line+"\n")
bot.run(token)