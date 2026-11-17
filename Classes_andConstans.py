import discord


BOARD_SIZE = 10
WATER = ":blue_square:"
EMPTY = ":black_circle:"
HIT = ":red_circle:"
SHIP = ":white_circle:"



class Player:
    def __init__(self, member):
        self.member = member
        self.own_map = [[WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#1
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#2
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#3
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#4
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#5
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#6
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#7
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#8
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#9
                        [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],
                        ]
        self.enemy_map = [[WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#1
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#2
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#3
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#4
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#5
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#6
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#7
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#8
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],#9
                         [WATER,WATER,WATER,WATER,WATER, WATER,WATER,WATER,WATER,WATER],
                         ]










#Custom View Class (experiment fra hjemmeside til at lave en knap)
class MyView(discord.ui.View):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        super().__init__()
        

    #setting up button (you can add multiple such)
    @discord.ui.button(label='yes', style=discord.ButtonStyle.green)
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # on interaction
        await self.player1.send('The other player said yes')
        
    @discord.ui.button(label='no', style=discord.ButtonStyle.red)
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # on interaction
        await interaction.response.send_message('NO!')
        print("no")


    
