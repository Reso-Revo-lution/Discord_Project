import discord
from discord.ext import commands
from discord import app_commands
WATER = ":blue_square:"
EMPTY = ":black_circle:"
HIT = ":red_circle:"
SHIP = "white_circle:"

BOARD_SIZE = 10

player_1 = [[WATER for cols in range(BOARD_SIZE)]for y in range(BOARD_SIZE)]

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())


def print_maps():
    interaction: discord.Interaction
    for tile in player_1:
        for i in tile:
            interaction.response.send_message(f"Hello {interaction.user.mention}!",ephemeral=True)
    
# Create a slash command group
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



# Simple slash command
@bot.tree.command(name="hello", description="Greets the user")
async def hello(interaction: discord.Interaction):
    """Basic slash command that greets the user"""
    
    current_map = []
    for col in player_1:
        current_map.append("\n")
        for row in col:
            current_map.append(row)

       

            
    await interaction.response.send_message(f"map\n{"".join(current_map)}",ephemeral=True)




# Run the bot
bot.run("TOKEN_HERE")
