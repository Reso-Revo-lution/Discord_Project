import discord
from discord.ext import commands
from discord import app_commands
import Classes_andConstans
from Classes_andConstans import BOARD_SIZE


player1 = Classes_andConstans.Player()


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




# function for open fire on enemy map.
@bot.tree.command(
        name= "fire",
        description= "fire on enemy"
)
@app_commands.describe(
        x= "is the coordinate for the x axes (choose a letter)",
        y= " is the coordinate for the y axes (choose num)"
)
@app_commands.choices(
    x=[
    app_commands.Choice(name="a", value=0),
    app_commands.Choice(name="b", value=1),
    app_commands.Choice(name="c", value=2),
    app_commands.Choice(name="d", value=3),
    app_commands.Choice(name="e", value=4),
    app_commands.Choice(name="c", value=5),
    app_commands.Choice(name="g", value=6),
    app_commands.Choice(name="h", value=7),
    app_commands.Choice(name="i", value=8),
    app_commands.Choice(name="j", value=9),],
    y=[
        app_commands.Choice(name="1", value=0),
        app_commands.Choice(name="2", value=1),
        app_commands.Choice(name="3", value=2),
        app_commands.Choice(name="4", value=3),
        app_commands.Choice(name="5", value=4),
        app_commands.Choice(name="6", value=5),
        app_commands.Choice(name="7", value=6),
        app_commands.Choice(name="8", value=7),
        app_commands.Choice(name="9", value=8),
        app_commands.Choice(name="10", value=9),]    
    )
async def fire(
    interaction: discord.Interaction,
    x : int,
    y : int
    ):
    await interaction.response.send_message(f"you fire at ({x};{y})",ephemeral=True)

@bot.tree.command(
        name= "place",
        description= "Place your ships on the board"
)

@app_commands.choices(
    x=[
    app_commands.Choice(name="a", value="a"),
    app_commands.Choice(name="b", value="b"),
    app_commands.Choice(name="c", value="c"),
    app_commands.Choice(name="d", value="d"),
    app_commands.Choice(name="e", value="e"),
    app_commands.Choice(name="c", value="f"),
    app_commands.Choice(name="g", value="g"),
    app_commands.Choice(name="h", value="h"),
    app_commands.Choice(name="i", value="i"),
    app_commands.Choice(name="j", value="j"),],
    y=[
        app_commands.Choice(name="1", value=0),
        app_commands.Choice(name="2", value=1),
        app_commands.Choice(name="3", value=2),
        app_commands.Choice(name="4", value=3),
        app_commands.Choice(name="5", value=4),
        app_commands.Choice(name="6", value=5),
        app_commands.Choice(name="7", value=6),
        app_commands.Choice(name="8", value=7),
        app_commands.Choice(name="9", value=8),
        app_commands.Choice(name="10", value=9),]    
    )

async def place(
    interaction: discord.Interaction,
    x : str,
    y : int
    ):
    await interaction.response.send_message(f"You placed your ship at [{x}:{y+1}]",ephemeral=True)



# test hvordan en knap sættes op
@bot.tree.command(
        name="tester",
        description="tester")
async def tester(
    interaction: discord.Interaction
    ):
    # add the view to a message
    await interaction.response.send_message("tester", view=Classes_andConstans.MyView())


@bot.tree.command(
        name = "battleships",
        description = "choose players for the game and start")
@app_commands.describe(
    player1 = "The first player",
    player2 = "The second player"
)
async def battleships_get_players(
    interaction: discord.Interaction,
    player1: discord.Member,
    player2: discord.Member
    ):
    await player1.send(f"Do you join? Play battleships with {player2.name}")
    #await player2.send_message(f"Do you join? Play battleships with {player1.name}")
    await interaction.response.send_message(f'You selected player 1 = {player1.name} player 2 = {player2.name}.',ephemeral=True)


# Simple slash command (slag skibe skal være med lille s.)
@bot.tree.command(
        name="slagskib",
        description="Prints map"
        )
async def slagskibe(interaction: discord.Interaction):
    """Basic slash command that greets the user"""
    
    current_map = ["\n| a  | b  | c  | d  | e  | f  | g  | h  | i  | j  |"]
    row_num = 0
    for col in player1.own_map:
        
        if row_num > 0:

            current_map.append(" |"+str(row_num))

        current_map.append("\n")

        row_num = row_num + 1

        for row in col:
            current_map.append(row)
    
    current_map.append(" |"+str(BOARD_SIZE))
    await interaction.response.send_message(f"map{"".join(current_map)}",ephemeral=True)



# Run the bot
bot.run("Token here")
