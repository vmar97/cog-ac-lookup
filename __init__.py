from .ac-lookup import ACLookup

def setup(bot):
    cog = ACLookup(bot)
    bot.add_cog(cog)
