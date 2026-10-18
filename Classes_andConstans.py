import discord


BOARD_SIZE = 10
WATER = ":blue_square:"
EMPTY = ":black_circle:"
HIT = ":red_circle:"
SHIP = "white_circle:"



class Player:
    def __init__(self):
        self.BOARD_SIZE = 10
        self.own_map = [[WATER for cols in range(self.BOARD_SIZE)]for rows in range(self.BOARD_SIZE)]
        self.enemy_map = [[WATER for cols in range(self.BOARD_SIZE)]for rows in range(self.BOARD_SIZE)]

    

#Custom View Class (experiment fra hjemmeside til at lave en knap)
class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()

    #setting up button (you can add multiple such)
    @discord.ui.button(label='test', style=discord.ButtonStyle.grey)
    async def asdf(self, interaction: discord.Interaction, button: discord.ui.Button):
        # on interaction
        await interaction.response.send_message('workie', ephemeral=True)
        print("yes")


    