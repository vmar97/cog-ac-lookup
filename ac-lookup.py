from redbot.core import commands
import discord
import requests
import json

class ACLookup(commands.Cog):
        """Grab information from Nookipedia"""

        def __init__(self, bot):
                self.bot = bot

        @commands.command(pass_context=True)
        async def villager(self, ctx, villager, *args):
                for arg in args:
                        villager = villager + " " + arg
                if villager == "Renee" or villager == "renee":
                        villager = 'Renée'
                elif villager == "Etoile" or villager == "etoile":
                        villager = 'Étoile'
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/villagers?name=' + villager + '&nhdetails=true&api_key=' + apikey)
                nookapi = apilink.json()
                if bool(nookapi) == False:
                        data = discord.Embed()
                        data.add_field(name="Error", value="Villager does not exist!", inline=False)
                else:
                        if bool(nookapi[0]['title_color']) == True:
                                villagercol = int(nookapi[0]['title_color'], 16)
                        else:
                                villagercol = int('67ac42', 16)
                        data = discord.Embed(title="Villager info", colour=villagercol, description=nookapi[0]["quote"])
                        data.set_thumbnail(url=nookapi[0]["image_url"])
                        if bool(nookapi[0]["nh_details"]) == True:
                                data.set_author(name=nookapi[0]["name"], url=nookapi[0]["url"], icon_url=nookapi[0]["nh_details"]["photo_url"])
                        else:
                                data.set_author(name=nookapi[0]["name"], url=nookapi[0]["url"])
                        data.add_field(name="Species", value=nookapi[0]["species"], inline=True)
                        data.add_field(name="Personality", value=nookapi[0]["personality"], inline=True)
                        data.add_field(name="Gender", value=nookapi[0]["gender"], inline=True)
                        if bool(nookapi[0]["birthday_month"]) == True:
                                data.add_field(name="Birthday", value=nookapi[0]["birthday_month"] + ' ' + str(nookapi[0]["birthday_day"]), inline=True)
                        else:
                                data.add_field(name="Birthday", value="Unknown", inline=True)
                        data.add_field(name="Sign", value=nookapi[0]["sign"], inline=True)
                        data.add_field(name="Catchphrase", value=nookapi[0]["phrase"], inline=True)
                        if bool(nookapi[0]["nh_details"]) == True:
                                if bool(nookapi[0]["nh_details"]["clothing_variation"]) == True:
                                        data.add_field(name="Clothing", value="[" + nookapi[0]["clothing"] + "](https://nookipedia.com/wiki/Item:" + nookapi[0]["clothing"].replace(" ", "_") + "_(New_Horizons)) (" + nookapi[0]["nh_details"]["clothing_variation"] + ")", inline=True)
                                else:
                                        data.add_field(name="Clothing", value="[" + nookapi[0]["clothing"] + "](https://nookipedia.com/wiki/Item:" + nookapi[0]["clothing"].replace(" ", "_") + "_(New_Horizons))", inline=True)
                        else:
                                data.add_field(name="Clothing", value=nookapi[0]["clothing"], inline=True)
                        data.add_field(name="More Info", value="[Learn more on Nookipedia](" + nookapi[0]["url"] + ")", inline=True)
                        data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
				
        @commands.command(pass_context=True)
        async def fish(self, ctx, fish, *args):
                for arg in args:
                        fish = fish + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/fish/' + fish + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('67ac42', 16)
                data = discord.Embed(title="Fish info", colour=coloring, description=nookapi["catchphrases"][0])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Months (NH)", value=nookapi["north"]["months"], inline=True)
                data.add_field(name="Months (SH)", value=nookapi["south"]["months"], inline=True)
                data.add_field(name="Times", value=nookapi["north"]["availability_array"][0]["time"], inline=True)
                data.add_field(name="Sell", value=nookapi["sell_nook"], inline=True)
                data.add_field(name="Sell (C.J.)", value=nookapi["sell_cj"], inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
				
        @commands.command(pass_context=True)
        async def bug(self, ctx, bug, *args):
                for arg in args:
                        bug = bug + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/bugs/' + bug + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('67ac42', 16)
                data = discord.Embed(title="Bug info", colour=coloring, description=nookapi["catchphrases"][0])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Months (NH)", value=nookapi["north"]["months"], inline=True)
                data.add_field(name="Months (SH)", value=nookapi["south"]["months"], inline=True)
                data.add_field(name="Times", value=nookapi["north"]["availability_array"][0]["time"], inline=True)
                data.add_field(name="Sell", value=nookapi["sell_nook"], inline=True)
                data.add_field(name="Sell (Flick)", value=nookapi["sell_flick"], inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
				
        @commands.command(pass_context=True)
        async def seacrit(self, ctx, seacrit, *args):
                for arg in args:
                        seacrit = seacrit + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/sea/' + seacrit + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('67ac42', 16)
                data = discord.Embed(title="Sea creature info", colour=coloring, description=nookapi["catchphrases"][0])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Months (NH)", value=nookapi["north"]["months"], inline=True)
                data.add_field(name="Months (SH)", value=nookapi["south"]["months"], inline=True)
                data.add_field(name="Times", value=nookapi["north"]["availability_array"][0]["time"], inline=True)
                data.add_field(name="Sell", value=nookapi["sell_nook"], inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
				
        @commands.command(pass_context=True)
        async def art(self, ctx, art, *args):
                for arg in args:
                        art = art + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/art/' + art + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('67ac42', 16)
                data = discord.Embed(title="Art info", colour=coloring, description=nookapi["description"])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Real-world name", value=nookapi["art_name"], inline=True)
                data.add_field(name="Author", value=nookapi["author"], inline=True)
                data.add_field(name="Year", value=nookapi["year"], inline=True)
                data.add_field(name="Art style", value=nookapi["art_style"], inline=True)
                if nookapi["has_fake"] == True:
                        data.add_field(name="Can be fake?", value="Yes", inline=True)
                else:
                        data.add_field(name="Can be fake?", value="No", inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
