import asyncio
import time
from pypresence import Presence
from discord.ext import commands

class RPCCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rpc_client = None  # Initialize RPC client to None
        self.large_image = 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDdxeThkdzZmM21wZG5qczRremM5ZmJpcjhoeTNqcnp4d3NicnZ5cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FPC5S2CmvwHvy/giphy.gif'  # Initial large image
        self.large_text = 'REAPERS '  # Text for large image tooltip
        self.state = "REAPERS"  # Default state text
        self.details = "REAPERS"  # Default details text

    @commands.command()
    async def srpc(self, ctx):
        """Starts the Discord Rich Presence (RPC) connection."""
        # Get your RPC details from config or define them here
        RpcClientID = "1327908151328116736"  # Your Discord application's client ID
        self.rpc_client = Presence(RpcClientID)
        
        # Connect to the RPC
        await ctx.send("Starting RPC...")
        await asyncio.to_thread(self.rpc_client.connect)
        
        await ctx.send("RPC Started!")

        # Start updating RPC status
        while True:
            # Replace these with the details you want to set
            discord_presence = {
                "state": self.state,
                "details": self.details,
                "start": int(time.time()),  # Set start time to now
                "large_image": self.large_image,
                "large_text": self.large_text,
                "small_image": "jgjgjgj",  # You can update this later if needed
                "small_text": "Ahmed",  # You can update this later if needed
                "party_id": "AhmedXLeon",
                "party_size": [1, 1],  # Adjust the party size range
                "buttons": [
                    {
                        "label": "Ahmed",
                        "url": "https://discord.gg/"
                    },
                    {
                        "label": "Leon",
                        "url": "https://discord.gg/"
                    }
                ]
            }

            await asyncio.to_thread(self.rpc_client.update, **discord_presence)
            await asyncio.sleep(100000000000000000000000000000000000) 

    @commands.command()
    async def rpce(self, ctx):
        """Stops the RPC."""
        if self.rpc_client:
            await ctx.send("Stopping RPC...")
            self.rpc_client.close()
            self.rpc_client = None
            await ctx.send("RPC Stopped!")
        else:
            await ctx.send("RPC is not running.")



# Setup function to add the cog to the bot
def setup(bot):
    bot.add_cog(RPCCog(bot))
