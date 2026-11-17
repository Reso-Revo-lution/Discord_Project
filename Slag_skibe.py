import discord
from discord.ext import commands
from discord import app_commands
import Classes_andConstans
from Classes_andConstans import EMPTY
from Classes_andConstans import SHIP
from Classes_andConstans import WATER
from Classes_andConstans import HIT
from Classes_andConstans import BOARD_SIZE

players={}

intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)


#----------get the token from different file
TOK_FILE = "Token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token


# Create a slash command group
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



# ----------------------- test hvordan en knap sættes op
@bot.tree.command(
        name="tester",
        description="tester")
async def tester(
    interaction: discord.Interaction
    ):
    # add the view to a message
    await interaction.response.send_message("tester", view=Classes_andConstans.MyView())



# ---------------- function for open fire on enemy map.
@bot.tree.command(
        name= "fire",
        description= "fire on enemy")
@app_commands.describe(
        x= "is the coordinate for the x axes (choose a letter)",
        y= "is the coordinate for the y axes (choose num)"
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

    if interaction.user == player1.member:
        match player2.own_map[y][x]:
            case Classes_andConstans.SHIP:
                player2.own_map[y][x] = HIT
                player1.enemy_map[y][x] = HIT
            case Classes_andConstans.WATER:
                player1.enemy_map[y][x] = EMPTY

    if interaction.user.name == player2.member:
        match player1.own_map[y][x]:
            case Classes_andConstans.SHIP:
                player1.own_map[y][x] = HIT
                player2.enemy_map[y][x] = HIT
            case Classes_andConstans.WATER:
                player2.enemy_map[y][x] = EMPTY
        
    await interaction.response.send_message(f"you fire at ({x};{y})",ephemeral=True)



# ----------------------------------------- Place ship
@bot.tree.command(
        name= "place",
        description= "Place your ships on the board"
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
async def place(
    interaction: discord.Interaction,
    x : int,
    y : int
    ):

    if interaction.user == player1.member:
        player1.own_map[y][x] = SHIP
        await interaction.response.send_message("None")
        

    if interaction.user == player2.member:
            player2.own_map[y][x] = SHIP
            await interaction.response.send_message("None")



# -------------------------------------- Start spillet
@bot.tree.command(
        name = "battleships",
        description = "choose players for the game and start")
@app_commands.describe(
    player1_message = "The first player",
    player2_message = "The second player"
)
async def battleships_get_players(
    interaction: discord.Interaction,
    player1_message: discord.Member,
    player2_message: discord.Member
    ):
    
    global player1
    global player2
    player1 = Classes_andConstans.Player(member=player1_message)
    player2 = Classes_andConstans.Player(member=player2_message)
    

    await player1_message.send(f"Do you join? Play battleships with {player2_message.name}")
    await player2_message.send(f"Do you join? Play battleships with {player1_message.name}")
    



# ------------------------------------- Prints map
@bot.tree.command(
        name="print_map",
        description="prints_map"
        )
async def print_map(interaction: discord.Interaction):
    
    if interaction.user == player1.member:
        await player1.member.send(f"Own map{"".join(make_map(player1.own_map))}")
        await interaction.response.send_message(f"Enemy map{"".join(make_map(player1.enemy_map))}")

    if interaction.user == player2.member:
        await player2.member.send(f"Own map{"".join(make_map(player2.own_map))}")
        await interaction.response.send_message(f"Enemy map{"".join(make_map(player2.enemy_map))}")

    

   



# -------------- subroutine
def make_map(map):
    current_map = ["\n| a  | b  | c  | d  | e  | f  | g  | h  | i  | j  |"]
    row_num = 0
    for col in map:
                
        if row_num > 0:

            current_map.append(" |"+str(row_num))

        current_map.append("\n")

        row_num = row_num + 1

        for row in col:
            current_map.append(row)

    current_map.append(" |"+str(BOARD_SIZE))
    
    return current_map

token = get_token()

# Run the bot
bot.run(token)
