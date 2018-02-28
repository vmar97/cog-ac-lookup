import discord
from discord.ext import commands
from lxml import html
import requests
import re

class villagerLookup:
        """Grab villager information from Nookipedia"""

        def __init__(self, bot):
                self.bot = bot

        @commands.command(pass_context=True)
        async def villager(self, ctx, villager):
                description = "Villager info for **" + villager + "**:"
                data = discord.Embed(colour=0x67AC42, description=description)

                attributes = ["species", "gender", "personality", "birthday", "clothes", "starsign", "phrase", "song", "appearances"]

                page = requests.get('https://nookipedia.com/wiki/' + villager)

                if page.status_code == 404:
                        data.add_field(name="Error", value="Villager does not exist!")
                else:
                        tree = html.fromstring(page.content)

                        for att in attributes:
                                id = str("Infobox-villager-" + att)
                                temp = str(tree.xpath('//td[@id="' + id + '"]//text()'))
                                if len(temp) > 2:
                                        if att == "appearances":
                                                temp = temp.replace("', '*', '","\n").replace("', ',', '","\n").replace("', '","\n")
                                        if att == "clothes":
                                                temp = temp.replace("', '*', '","\n")
                                        temp = temp.replace("['","").replace("']","").replace("*","").replace("', '","") # Remove list notation surrounding data
                                        temp = temp[:-2] # Remove trailing '\n' at the end of each string; for some reason, .replace or .rstrip doesn't work
                                        if att == "phrase":
                                                temp = re.sub(r'\([^)]*\)', '', temp) # Remove sets of parenthese and their contents (in this case, language indications: (EN), (JP), etc.)
                                                temp = re.sub('[^a-zA-Z]', '', temp) # Remove any non-English alphabet characters (in this case, Japanese)
                                        data.add_field(name=att.capitalize(), value=temp)
                                else:
                                        temp="N/A"
                                        data.add_field(name=att.capitalize(), value=temp)

                await self.bot.say(embed=data)

def setup(bot):
	bot.add_cog(villagerLookup(bot))
