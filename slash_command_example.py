import discord
from discord.ext import commands
from discord import app_commands

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

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
    await interaction.response.send_message(f"Hello {interaction.user.mention}!")

# Slash command with parameters
@bot.tree.command(name="greet", description="Greet someone with a custom message")
@app_commands.describe(
    name="The name of the person to greet",
    message="Custom greeting message"
)
async def greet(
    interaction: discord.Interaction, 
    name: str, 
    message: str = "Hello"
):
    """Slash command with required and optional parameters"""
    await interaction.response.send_message(f"{message}, {name}!")

# Slash command with choices
@bot.tree.command(name="choose", description="Pick a color")
@app_commands.describe(color="Pick your favorite color")
@app_commands.choices(color=[
    app_commands.Choice(name="Red", value="red"),
    app_commands.Choice(name="Blue", value="blue"),
    app_commands.Choice(name="Green", value="green"),
])
async def choose_color(interaction: discord.Interaction, color: str):
    """Slash command with predefined choices"""
    await interaction.response.send_message(f"You chose: {color}")

# Slash command with number range
@bot.tree.command(name="roll", description="Roll a dice (1-20)")
@app_commands.describe(max_value="Maximum value for the dice (default 20)")
async def roll_dice(
    interaction: discord.Interaction, 
    max_value: app_commands.Range[int, 1, 100] = 20
):
    """Slash command with parameter range validation"""
    import random
    result = random.randint(1, max_value)
    await interaction.response.send_message(f"🎲 You rolled: **{result}**")

# Run the bot
bot.run("Token here")
