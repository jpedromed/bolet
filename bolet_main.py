import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
from discord_slash import SlashCommand
client = commands.Bot(command_prefix="$", case_insensitive = True)
@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="type $info"))
@client.command()
async def info(ctx):
	await ctx.send(
	 "This is a bot for information about Cards from the game Creatures of Aether, by Tako Boy Studios and Dan Fornace LLC;\nUse $c followed by a card's name to see info about them;\nUse $a followed by an ability's name to see info about it;\nType $decks for a couple of useful links;\nType $skins for info on how what kinds of skins exist in the game, how to obtain them and who has them;\nIf you find any bugs, typos or creatures missing, DM @jpedromed and he'll take care of it;\nFor any names with spaces, the command used will have no spaces or an _ instead of spaces.")
 
@client.command()
async def decks(ctx):
	await ctx.send(
	 "User LunaRay keeps track of tournament top decks in https://tinyurl.com/CoACards go check it out!\nUser CMAvelis has a deckbuilder website, go check it out at https://creatures.cameronavelis.com/ this is also where we create card pools for tournaments.")
 
 #await ctx.send(f'Name: Tinderbit ", description = "Element: Fire\nRarity: Common\nPower Cost: 1\nAbility: none \nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4\n :arrow_right: = 0 | 1 | 2 | 3\n :arrow_down: = 0 | 1 | 2 | 3\n :arrow_left: = 3 | 4 | 5 | 6') code I used before using embeds
@client.command()
async def c(ctx, creature=None):
  variable = creature
  if creature is None :
    await ctx.send("Use $c followed by a card's name to see info about them.")
  elif creature == "tinderbit" or creature == "Tinderbit" or creature == "tinder" or creature == "Tinder":
    embed=discord.Embed(color=0xd33c30, title = 'Tinderbit", description = "Element: Fire\nRarity: Common\nPower Cost: 1\nAbility: none \nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4\n :arrow_right: = 0 | 1 | 2 | 3\n :arrow_down: = 0 | 1 | 2 | 3\n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A cute creature that also happens to be a naturally skilled thief.')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238484738420866/card-FireRaccoon-level-1.png")
        
    await ctx.send (embed = embed)
 
  elif creature == "scorhawk" or creature == "Scorhawk":
    embed=discord.Embed(color=0xd33c30, title = "Scorhawk ", description = "Element: Fire \nRarity: Common \nPower Cost: 1 \nAbility: none \nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation:It soars effortlessly through the air, painting the sky with streaks of flame.")
    embed.set_thumbnail (url="https://cdn.discordapp.com/attachments/872236731397734431/872238675235307531/card-Scorhawk-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "firanha" or creature == "Firanha":
    embed=discord.Embed(color=0xd33c30, title = "Firanha ", description = "Element: Fire\nRarity: Common\nPower Cost: 1\nAbility: none \nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: It swims through pools of lava, consuming volcanic rock with its powerful jaws.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238434184474624/card-Firanha-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "charclaw" or creature == "Charclaw":
    embed=discord.Embed(color=0xd33c30, title = "Charclaw ", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: Home Field \nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A hard-shelled crustacean that emits a thick, poisonous smog from its head.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238439477674105/card-FireCrab-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "chowl" or creature == "Chowl":
    embed=discord.Embed(color=0xd33c30, title = "Chowl", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: Defender \nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6\n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: The flames erupting from its feathers can be temporarily extinguished to keep itself hidden amongst trees.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238337287671944/card-Chowl-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "flareater" or creature == "Flareater" or creature == "Flareeater" or creature == "flareeater":
    embed=discord.Embed(color=0xd33c30, title = "Flareater", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 0 | 1 | 2 | 3 \nInformation: Its fiery mane keeps enemies away while it searches for food in hard to reach places.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238521044316210/card-Flareater-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == 'flitch' or creature == 'Flitch':
    embed=discord.Embed(color=0xd33c30, title = "Flitch", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: Knight\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 3 | 4 | 5 | 6\n :arrow_left: = 0 | 1 | 2 | 3\nInformation: A career soldier that lives for the rush of combat. Has a bad reputation for breaking ranks.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238527885230080/card-Flitch-level-1.png")
 
    await ctx.send (embed = embed)
 
  elif creature == "porcuber" or creature == "Porcuber":
    embed=discord.Embed(color=0xd33c30, title = "Porcuber", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4\n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: Its quills are made for concentrated bursts of flame. As dangerous as it is cute!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238648656035850/card-Porcuber-level-1.png")
    
    
    await ctx.send (embed = embed)
 
  elif creature == "pyrewing" or creature == "Pyrewing":
    embed=discord.Embed(color=0xd33c30, title = "Pyrewing", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4\n :arrow_left: = 5 | 6 | 7 | 8\nInformation: Its two sets of wings move at great speed, generating colorful fire sparks that light up the night")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238485283676240/card-FireSemiWeakAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "sidgar" or creature == "Sidgar":
    embed=discord.Embed(color=0xd33c30, title = "Sidgar ", description = "Element: Fire\nRarity: Common\nPower Cost: 3\nAbility: War Drums\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A promising young warrior equal parts loyal, brave and humorless. A stickler for the rules of the army.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238774959083520/card-WarDrumCougar-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "slithersinge" or creature == "Slithersinge":
    embed=discord.Embed(color=0xd33c30, title = "Slithersinge", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 3 | 4 | 5 | 6\nAbility: none\nInformation: A dangerous snake with a volcanic rock body.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238710635261992/card-Slithersinge-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "smogeleon" or creature == "Smogeleon":
    embed=discord.Embed(color=0xd33c30, title = "Smogeleon ", description = "Element: Fire\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: Loves incredibly hot enviroments. It can blend into is surroundings to hide from predators.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238436592013313/card-FireChameleon-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "flarekat" or creature == "Flarekat" or creature == "flarecat" or creature == "Flarecat":
    embed=discord.Embed(color=0xd33c30, title = "Flarekat", description = "Element: Fire\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 |2 | 3 | 4  \n :arrow_left: = 8 | 9 | 10 | 11\nInformation: It lives with its pack, burrowing in volcanic rock. They are small, but brave!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238473581592586/card-FireNormalAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "magmotter" or creature == "Magmotter":
    embed=discord.Embed(color=0xd33c30, title = "Magmotter", description = "Element: Fire\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 7 | 8 | 9 | 10 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: It fluidly moves through rivers of lava in search of obsidian it can use to build its den.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238479843663922/card-FireOtter-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "scoraffe" or creature == "Scoraffe":
    embed=discord.Embed(color=0xd33c30, title = "Scoraffe", description = "Element: Fire\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 1 | 2 | 3 | 4\n :arrow_left: = 5 | 6 | 7 | 8 \nInformation: Residing in desert regions, these tall creatures are rather peacefull despite their big size.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238475766796328/card-FireNormalAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "serilia" or creature == "Serilia":
    embed=discord.Embed(color=0xd33c30, title = "Serilia", description = "Element: Fire\nRarity: Epic\nPower Cost: 3\nAbility: Push\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A martial arts master. She can channel intense heat through her body, firing off explosive hits to her opponent.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238690796179547/card-Serilia-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "skoal" or creature == "Skoal":
    embed=discord.Embed(color=0xd33c30, title = "Skoal", description = "Element: Fire\nRarity: Common\nPower Cost: 3\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4  \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: An easily agitated creature with a deadly tail of flame. Can spew poisonous gas from behind when threatened.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238699251900416/card-Skoal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Ursun" or creature == "ursun":
    embed=discord.Embed(color=0xd33c30, title = "Ursun", description = "Element: Fire\nRarity: Common\nPower Cost: 3\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A cute creature that's said to bring about good fortune. Its child-like nature is quite apparent.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238724426121276/card-Sunbear-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "ashe" or creature == "Ashe": 
    embed=discord.Embed(color=0xd33c30, title = "Ashe", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: upperhand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: A skilled warrior. She specializes in rapid, hard-hitting punches that wear down her opponents.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238462542151681/card-FireEpicOffensiveAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "blazadactyl" or creature == "Blazadactyl": 
    embed=discord.Embed(color=0xd33c30, title = "Blazadactyl", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A prehistoric creature that takes to the skies with aggressive ferocity. Be wary of its sharp fangs.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238487519232100/card-FireStrongAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Doki" or creature == "doki":
    embed=discord.Embed(color=0xd33c30, title = "Doki", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: Shifter\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A mischievous trickster who has the ability to change its elements depending on its surroundings.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238346968113212/card-Doki-level-1.png")
    
    await ctx.send (embed = embed)
  
  elif creature == "embertusk" or creature == "Embertusk":
    embed=discord.Embed(color=0xd33c30, title = "Embertusk", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 2 | 3 | 4 | 5\n :arrow_down: = 3 | 4 | 5 | 6\n :arrow_left: = 9 | 10 | 11 | 12\nInformation: An immensively heavy creature sporting two flaming tusk. Easy to anger. Difficult to calm down")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238489947766784/card-FireStrongAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
  
  elif creature == "firefang" or creature == "Firefang" or creature == "charyote" or creature == "Charyote":
    embed=discord.Embed(color=0xd33c30, title = "Firefang", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 2 | 3 | 4 | 5\n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: Fearsome predators that roam in small packs. They swarm their prey in organized, relentless assaults.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238517776973834/card-FireWolf-level-1.png")
    
    await ctx.send (embed = embed)
  
  elif creature == "infernacal" or creature == "Infernacal":
    embed=discord.Embed(color=0xd33c30, title = "Infernacal", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 8 | 9 | 10 | 11 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: Rare, elegant, agile. Its twin tails help it mantain balance when performing acrobatic feats.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238501771509791/card-FireStrongAnimal3-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "renburn" or creature == "Renburn":
    embed=discord.Embed(color=0xd33c30, title = "Renburn", description = "Element: Fire\nRarity: Epic\nPower Cost: 4\nAbility: Raze\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: The powerful ruler of the Fire Kingdom - and the father of Zetterburn and Forsburn.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238656037986304/card-Renburn-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "scorchel" or creature == "Scorchel":
    embed=discord.Embed(color=0xd33c30, title = "Scorchel", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 8 | 9 | 10 | 11 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: Small, mischievous, and very rare. They hide in hollows of scorched trees.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238664724385842/card-Scorchel-level-1.png")
    
    await ctx.send (embed = embed)
  
  elif creature == "smeltsmash" or creature == "Smeltsmash":
    embed=discord.Embed(color=0xd33c30, title = "Smeltsmash", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 5 | 6 | 7 | 8 \nInformation: A dangerous predator that patrols the many magma channels beneath active volcanoes. Loves to crush foes with its head.")
    embed.set_thumbnail(url="hhttps://cdn.discordapp.com/attachments/872236731397734431/872238718214344725/card-Smeltsmash-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Sunny" or creature == "sunny":
    embed=discord.Embed(color=0xd33c30, title = "Sunny", description = "Element: Fire\nRarity: Rare\nPower Cost: 4\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 7 | 8 | 9 | 10 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: An adorable canine with a fiery coat of fur. Said to harness power of the sun!")
    embed.set_thumbnail(url="hhttps://cdn.discordapp.com/attachments/872236731397734431/872238727576031263/card-Sunny-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Blazeen" or creature == "blazeen":
    embed=discord.Embed(color=0xd33c30, title = "Blazeen", description = "Element: Fire\nRarity: Epic\nPower Cost: 5\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 8 | 9 | 10 | 11 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 8 | 9 | 10 | 11\nInformation: Gigantic in size, this creature wields unfathomable strength.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238458553401384/card-FireEpicAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "emberu" or creature == "Emberu":
    embed=discord.Embed(color=0xd33c30, title = "Emberu", description = "Element: Fire\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 10 | 11 | 12 | 13 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: One of the 4 elemental watchers. He holds great wisdom, but is often slow to act.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238512211120158/card-FireStrongerAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Searscale" or creature == "searscale":
    embed=discord.Embed(color=0xd33c30, title = "Searscale", description = "Element: Fire\nRarity: Epic\nPower Cost: 5\nAbility: Avatar\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 2 | 3 | 4 | 5\n :arrow_down: = 4 | 5 | 6 | 7 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: A gargantuan, armored reptile. Its scales of abyss obsidian are unbreakable.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238686765461594/card-Searscale-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Slaggo" or creature == "slaggo":
    embed=discord.Embed(color=0xd33c30, title = "Slaggo", description = "Element: Fire\nRarity: Epic\nPower Cost: 5\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 7 | 8 | 9 | 10 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: An enormous creature with thick, volcanic rock armor. It can generate lava from its innards.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238514538950706/card-FireStrongerAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
  
  elif creature == "torcharus" or creature == "Torcharus":
    embed=discord.Embed(color=0xd33c30, title = "", description = "Element: Fire\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 12 | 13 | 14 | 15\nInformation: A mystical fire dragon. It sits upon volcanoes, honing its power against the fierce forces of nature.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655085690306570/card-FireDragon-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "florpian" or creature == "Florpian":
    embed=discord.Embed(color=0x63bf3c, title = "", description = "Element: Earth\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: It burrows itself in the sand, waiting to strike unsuspecting cratures with its stone stinger.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238531173548112/card-Florpian-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "folet" or creature == "Folet":
    embed=discord.Embed(color=0x63bf3c, title = "Folet", description = "Element: Earth\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: A whimsical creature with a joyful demeanor. It often uses its own tail as a pillow")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238587389804575/card-Leffet-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "weedwing" or creature == "Weedwing":
    embed=discord.Embed(color=0x63bf3c, title = "Weedwing", description = "Element: Earth\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: Its fangs are used to exract the juices from fruits. No blood-sucking here!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238391016697866/card-EarthSemiWeakAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "liztrot" or creature == "Liztrot":
    embed=discord.Embed(color=0x63bf3c, title = "Liztrot", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: It speeds across shallow swamps and ponds, running across the water's surface. Always up for a race!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238586844569660/card-Liztrot-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Meadant" or creature == "meadant":
    embed=discord.Embed(color=0x63bf3c, title = "Meadant", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A sturdy creature that lives with others of its own kind in large , underground colonies. Hard working!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238349652492298/card-EarthAnt-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "muddel" or creature == "Muddel":
    embed=discord.Embed(color=0x63bf3c, title = "Muddel", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: It spends most of its time in small, mud-holes of its own making")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238423484813332/card-EarthWeakAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Palmel" or creature == "palmel":
    embed=discord.Embed(color=0x63bf3c, title = "Palmel", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: Big, leafy and reliable. These plant-covered herbivores store water in their backs.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238393227112529/card-EarthSemiWeakAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Pelisprout" or creature == "pelisprout" :
    embed=discord.Embed(color=0x63bf3c, title = "Pelisprout", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A strange bird-like creature. Its beak is coated in a dense bushel of leaves")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238643429924934/card-Pelisprout-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Scarabie" or creature == "scarabie":
    embed=discord.Embed(color=0x63bf3c, title = "Scarabie", description = "Element: Earth\nRarity: Rare\nPower Cost: 2\nAbility: Shifter\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: This creature will shed its skin and absourb surrounding elements to lay eggs. For these reasons, many believe this sacred beetle represents the cycle of rebirth & resurrection.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238660718829588/card-Scarabie-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Slorp" or creature == "slorp":
    embed=discord.Embed(color=0x63bf3c, title = "Slorp", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: Small creatures that live under rocks and old logs. Considered gross by most.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238714867318794/card-Slorp-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "swamplotl" or creature == "Swamplotl":
    embed=discord.Embed(color=0x63bf3c, title = "Swamplotl", description = "Element: Earth\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: Often lounging in muddy swamps, this relaxed creature oozes a unique type of cuteness.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238352001302598/card-EarthAxolotl-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Buzzridge" or creature == "buzzridge":
    embed=discord.Embed(color=0x63bf3c, title = "Buzzridge", description = "Element: Earth\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5\n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 8 | 9 | 10 | 11 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A vicious creature that is quick to anger. If irritated, it will continuously attack its target.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238389095714856/card-EarthNormalAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Cobbleclaw" or creature == "cobbleclaw":
    embed=discord.Embed(color=0x63bf3c, title = "Cobbleclaw", description = "Element: Earth\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A cluster of winged rocks that descends upon its prey from the sky.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655022637338665/card-EarthBird-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "mudmub" or creature == "Mudmub" or creature == "mudmud" or creature == "Mudmud" :
    embed=discord.Embed(color=0x63bf3c, title = "Mudmub", description = "Element: Earth\nRarity: Common\nPower Cost: 3\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A small, beetle-like creature. They live in swamplands, and use the mud pools as camouflage to evade predators")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238632310833183/card-Mudmub-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "oremol" or creature == "Oremol":
    embed=discord.Embed(color=0x63bf3c, title = "Oremol", description = "Element: Earth\nRarity: Common\nPower Cost: 3\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: An adorable creature that lives underground. Its skillful digging abilities are one of a kind.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238385975148554/card-EarthMole-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "stagara" or creature == "Stagara":
    embed=discord.Embed(color=0x63bf3c, title = "Stagara", description = "Element: Earth\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 7 | 8 | 9 | 10\nInformation: A peaceful creature that spends most of its days among its herd. It sports beautiful antlers.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238721708224512/card-Stagara-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Torong" or creature == "torong" or creature == "towong" or creature == "Towong":
    embed=discord.Embed(color=0x63bf3c, title = "Torong", description = "Element: Earth\nRarity: Epic\nPower Cost: 3\nAbility: Push\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 4 | 5 | 6 | 7\n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A martial arts master. Specialing in grapples and throws, his fierce grip is nearly impossible to escape from.")
    embed.set_thumbnail(url="hhttps://cdn.discordapp.com/attachments/872236731397734431/872238739840172053/card-Torong-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Babidon" or creature == "babidon":
    embed=discord.Embed(color=0x63bf3c, title = "Babidon", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: War Drums\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 4 | 5 | 6 | 7 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: His thundering dreambeat summons warriors from throughout the Aetherian forest. Frequently challenges Torong to contests of strength.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238770982912030/card-WarDrumBoar-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "birchpaw" or creature == "Birchpaw":
    embed=discord.Embed(color=0x63bf3c, title = "Birchpaw", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A rare canine creature with an affinity for maple trees.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872654454950883369/birchpaw.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Boulderoar" or creature == "boulderoar":
    embed=discord.Embed(color=0x63bf3c, title = "Boulderoar", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 8 | 9 | 10 | 11 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A bulky predator, often heralded as king of the mountains.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238418204196956/card-EarthStrongerAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Gravelgrin" or creature == "gravelgrin":
    embed=discord.Embed(color=0x63bf3c, title = "Gravelgrin", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 9 | 10 | 11 | 12 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: This scavenging creature can chew through almost anything with its stout, stone jaws.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238383332741131/card-EarthHyena-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Minto" or creature == "minto":
    embed=discord.Embed(color=0x63bf3c, title = "Minto", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: Knight\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 7 | 8 | 9 | 10  \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: An experienced swordsman from a distant land. Blitzes across the battlefield with his insect-like mount.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238594943778837/card-Minto-level-1.pngg")
    
    await ctx.send (embed = embed)
 
  elif creature == "Mudmo" or creature == "mudmo":
    embed=discord.Embed(color=0x63bf3c, title = "Mudmo", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A rare creature that makes its home in siolated swamplands.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238597640699925/card-Mudmo-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Pinepurr" or creature == "pinepurr":
    embed=discord.Embed(color=0x63bf3c, title = "Pinepurr", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 7 | 8 | 9 | 10 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A rare feline creature with a sharp pine needle fur coat. More agile than it looks!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238395307483206/card-EarthStrongAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "ridgehorn" or creature == "Ridgehorn":
    embed=discord.Embed(color=0x63bf3c, title = "Ridgehorn", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: Incredibly strong. Its horns can fracture solid tock. Be wary of its temper!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238399304650792/card-EarthStrongDefensiveAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "treeceratops" or creature == "Treeceratops" or creature == "treeceritops" or creature == "Treeceritops":
    embed=discord.Embed(color=0x63bf3c, title = "Treeceratops", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 8 | 9 | 10 | 11\nInformation: A powerful, prehistoric creature. A rare type of tree sprouts from its head.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238744831422515/card-Treeceratops-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Zebrock" or creature == "zebrock":
    embed=discord.Embed(color=0x63bf3c, title = "Zebrock", description = "Element: Earth\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: A creature with powerful hind legs made of solid rock. Don’t get kicked!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238227044597811/card-Zebrock-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Zolt" or creature == "zolt":
    embed=discord.Embed(color=0x63bf3c, title = "Zolt", description = "Element: Earth\nRarity: Epic\nPower Cost: 4\nAbility: Metal Armor\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A famed wallrunner with a armored coat of conductive metal. Electrifyingly tough.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238232136466452/card-Zolt-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Cliffroach" or creature == "cliffroach":
    embed=discord.Embed(color=0x63bf3c, title = "Cliffroach", description = "Element: Earth\nRarity: Epic\nPower Cost: 5\nAbility: Avatar\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A colossal insect occasionally mistaken as a moving mountain")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238342383747102/card-Cliffroach-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "crunchodile" or creature == "Crunchodile" or creature == "Crunch" or creature == "crunch" :
    embed=discord.Embed(color=0x63bf3c, title = "Crunchodile", description = "Element: Earth\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 10 | 11 | 12 | 13 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A merciless creature. His deadly bite can crush even the hardest rocks into mere dust.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238378517667911/card-EarthEpicAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "leffox" or creature == "Leffox":
    embed=discord.Embed(color=0x63bf3c, title = "Leffox", description = "Element: Earth\nRarity: Epic\nPower Cost: 5\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 8 | 9 | 10 | 11 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: One of the 4 elemental watchers. Her sly nature gives her an untrustworthy aura")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238414576119869/card-EarthStrongerAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Lumbergard" or creature == "lumbergard":
    embed=discord.Embed(color=0x63bf3c, title = "Lumbergard", description = "Element: Earth\nRarity: Epic\nPower Cost: 5\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: Equipped with reinforced bark armor, his skill wielding his trusty twin shields is unmatched.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238381097156628/card-EarthEpicDefensiveAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Stonedra" or creature == "stonedra":
    embed=discord.Embed(color=0x63bf3c, title = "Stonedra", description = "Element: Earth\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 12 | 13 | 14 | 15 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A mystical earth dragon. It watches over the ancient forests of the world witha  quiet mindfulness.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238371370578051/card-EarthDragon-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "nimbouse" or creature == "Nimbouse":
    embed=discord.Embed(color=0xbf96df, title = "Nimbouse", description = "Element: Air\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A teeny creature that makes cloud burrows among the vast skyscapes. Loves cheese.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238635439759421/card-Nimbouse-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "voltick" or creature == "Voltick":
    embed=discord.Embed(color=0xbf96df, title = "Voltick", description = "Element: Air\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: A bite from this electrified bug creat")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238235269595166/card-AirBeetle-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "wooluff" or creature == "Wooluff":
    embed=discord.Embed(color=0xbf96df, title = "Wooluff", description = "Element: Air\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: It spends its time grazing, resulting in its magnificent cloud wool coat. Warm and fluffy!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238854952869928/card-Wooluff-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Cloala" or creature == "cloala":
    embed=discord.Embed(color=0xbf96df, title = "Cloala", description = "Element: Air\nRarity: Common\nPower Cost: 2\nAbility: Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: Small, bear-like creatures that sit idle upon the highest tree tops.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238344711581718/card-Cloala-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Driftmunk" or creature == "driftmunk":
    embed=discord.Embed(color=0xbf96df, title = "Driftmunk", description = "Element: Air\nRarity: common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: A creature that can be found soaring through the air, as light as a feather. It’s super quick, too!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238304689537024/card-AirSugarglider-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "fluttersnout" or creature == "Fluttersnout" or creature == "f.snout" or creature == "F.snout":
    embed=discord.Embed(color=0xbf96df, title = "Fluttersnout", description = "Element: Air\nRarity: Rare\nPower Cost: 2\nAbility: Shifter\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: Using its snout, this creature is able to absorb elemental properties to adapt to any environment.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238534814212216/card-Fluttersnout-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Platygust" or creature == "platygust":
    embed=discord.Embed(color=0xbf96df, title = "Platygust", description = "Element: Air\nRarity: Common\nPower Cost: 2\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: It paddles through the cloud seas at impressive speeds, thanks to its sturdy tail.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238645250252870/card-Platygust-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Pluffel" or creature == "pluffel" or creature == "Puffel" or creature == "puffel" :
    embed=discord.Embed(color=0xbf96df, title = "Pluffel", description = "Element: Air\nRarity: Common\nPower Cost: 2\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: An adorable creature that hides among the clouds, swelling up its body when danger approaches.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238238398562344/card-AirBlowfish-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Skyfoal" or creature == "skyfoal":
    embed=discord.Embed(color=0xbf96df, title = "Skyfoal", description = "Element: Air\nRarity: Common\nPower Cost: 2\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: Due to its small sinze, it’s difficult to spot amongst the clouds.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238703639142431/card-Skyfoal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "turlad" or creature == "Turlad" or creature == "Turtlad" or creature == "turtlad" :
    embed=discord.Embed(color=0xbf96df, title = "Turlad", description = "Element: Air\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A peaceful creature that lives in the cloud seas. It hides in its shell to defend itself.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238767585513482/card-Turlad-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Zoltfin" or creature == "zoltfin":
    embed=discord.Embed(color=0xbf96df, title = "Zoltfin", description = "Element: Air\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A fish creature with electrically charged whiskers. High voltage: do not touch.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238231096270888/card-Zoltfin-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "breegull" or creature == "Breegull":
    embed=discord.Embed(color=0xbf96df, title = "Breegull", description = "Element: Air\nRarity: Common\nPower Cost: 3\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A scavenger bird with an insatiable appetite. Loud and irritating.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238310658039899/card-Breegull-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Flython" or creature == "flython":
    embed=discord.Embed(color=0xbf96df, title = "Flython", description = "Element: Air\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 8 | 9 | 10 | 11 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A venomous snake creature that can strike its prey from mid-air. SOme say its feathers are lucky.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238278840045638/card-AirSnake-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Herra" or creature == "herra":
    embed=discord.Embed(color=0xbf96df, title = "Herra", description = "Element: Air\nRarity: Epic\nPower Cost: 3\nAbility: Push\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A martial arts master. She can channel electricity through her precise, lightning-quick strikes.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238557266317352/card-Herra-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Jellikid" or creature == "jellikid":
    embed=discord.Embed(color=0xbf96df, title = "Jellikid", description = "Element: Air\nRarity: Common\nPower Cost: 3\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: Don’t let its cute appearance fool you-its tentacles pack an electric punch.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655263725944862/card-AirSemiWeakAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Ruffpuff" or creature == "ruffpuff":
    embed=discord.Embed(color=0xbf96df, title = "Ruffpuff", description = "Element: Air\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: An upbeat creature that remains loyal to its friends. Extremely puffy.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655336283209758/card-AirNormalAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "tentacopter" or creature == "Tentacopter":
    embed=discord.Embed(color=0xbf96df, title = "Tentacopter", description = "Element: Air\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A strange creature that can sometimes be spotted flying through dangerous storms.")
    embed.set_thumbnail(url="hhttps://cdn.discordapp.com/attachments/872236731397734431/872238736606363668/card-Tentacopter-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Cirriphant" or creature == "cirriphant":
    embed=discord.Embed(color=0xbf96df, title = "Cirriphant", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 7 | 8 | 9 | 10 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A huge creature sporting tought armor. It travels in packs, and protects family at all costs.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238291225825290/card-AirStrongDefensiveAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Fairaby" or creature == "fairaby":
    embed=discord.Embed(color=0xbf96df, title = "Fairaby", description = "Element: Air\nRarity: Common\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 8 | 9 | 10 | 11 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A whimsical creature with a set of beautiful wings. Wields mystical powers!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238429226823701/card-Fairaby-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "joltbeak" or creature == "Joltbeak":
    embed=discord.Embed(color=0xbf96df, title = "Joltbeak", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A jolly bird creature with a shockingly trendy feather crown.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238243364614224/card-AirNormalAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Misune" or creature == "misune":
    embed=discord.Embed(color=0xbf96df, title = "Misune", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: A fox-like creature that hides itself among the mists it can emit from its multiple tails.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238595967184956/card-Misune-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "shockjaw" or creature == "Shockjaw":
    embed=discord.Embed(color=0xbf96df, title = "Shockjaw", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A vicious sky predator. It stalks its prey tierlessly, waiting for the perfect chance to strike.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238298880413706/card-AirStrongerAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "sparkfang" or creature == "Sparkfang":
    embed=discord.Embed(color=0xbf96df, title = "Sparkfang", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: Ferocious, intimidating, and quick to anger. Its fangs produce a powerful electric current")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238301371858994/card-AirStrongOffensiveAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Swiftfin" or creature == "swiftfin":
    embed=discord.Embed(color=0xbf96df, title = "Swiftfin", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 8 | 9 | 10 | 11\nInformation: A speedy air creature known for its tremendous tricks, flips and spins.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238287706808361/card-AirStrongAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "vanbard" or creature == "Vanbard":
    embed=discord.Embed(color=0xbf96df, title = "Vanbard", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: War Horns\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 7 | 8 | 9 | 10 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A strict disciplinarian at the head of a local militia. Cunning, resourceful, and deeply bitter.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238780172599336/card-WarHornBaboon-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Whiffalow" or creature == "whiffalow" or creature == "wiffalow" or creature == "Whifalow":
    embed=discord.Embed(color=0xbf96df, title = "Whiffalow", description = "Element: Air\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 9 | 10 | 11 | 12 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A rare herd with magnificent horns and a beautiful, puffy coat of clouds.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238284145844304/card-AirStrongAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Freyden" or creature == "freyden":
    embed=discord.Embed(color=0xbf96df, title = "Freyden", description = "Element: Air\nRarity: Epic\nPower Cost: 5\nAbility: Knight\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 8 | 9 | 10 | 11 \n :arrow_left: = 7 | 8 | 9 | 10\nInformation: A daring shield-maiden. Her mount can leap great distances by discharging stored energy.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238543743889428/card-Freyden-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Swiftwing" or creature == "swiftwing":
    embed=discord.Embed(color=0xbf96df, title = "Swiftwing", description = "Element: Air\nRarity: Epic\nPower Cost: 4\nAbility: Swoop\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 7 | 8 | 9 | 10 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 7 | 8 | 9 | 10\nInformation: A decorated commander of great reknown. His stern, disciplined nature commands respect.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238730461741126/card-Swiftwing-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "galespur" or creature == "Galespur" or creature == "galespurr" or creature == "Galespurr":
    embed=discord.Embed(color=0xbf96df, title = "Galespur", description = "Element: Air\nRarity: Epic\nPower Cost: 5\nAbility: Avatar\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: An enormous, corrupted bird that harnesses immense power.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238549053870140/card-Galespur-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Gorillanado" or creature == "gorillanado":
    embed=discord.Embed(color=0xbf96df, title = "Gorillanado", description = "Element: Air\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 10 | 11 | 12 | 13 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: Self-proclaimed king of the skies, this hulking brute can generate powerful winds in an instant.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238554187726848/card-Gorillanado-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Grizzulus" or creature == "grizzulus" or creature == "Grizzilus" or creature == "grizzilus":
    embed=discord.Embed(color=0xbf96df, title = "Grizzulus", description = "Element: Air\nRarity: Epic\nPower Cost: 5\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 4 | 5 | 6 | 7 \n :arrow_left: = 8 | 9 | 10 | 11\nInformation: One of the 4 elemental watchers. Although he looks fierce, he’s actually quite the gentle soul.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238294891634738/card-AirStrongerAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Zango" or creature == "zango":
    embed=discord.Embed(color=0xbf96df, title = "Zango", description = "Element: Air\nRarity: Epic\nPower Cost: 5\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: Her scale armor can store electricity, which is then unleashed through her swift claw strikes.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238239585554513/card-AirDefensiveEpicAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Zephyrus" or creature == "zephyrus":
    embed=discord.Embed(color=0xbf96df, title = "Zephyrus", description = "Element: Air\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 12 | 13 | 14 | 15 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A mystical dragon that roams the forgotten skies. It’s rumored it can conjure storms at will.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238241397481472/card-AirDragon-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "dripfly" or creature == "Dripfly" or creature == "Drip" or creature == "drip" :
    embed=discord.Embed(color=0x6ab0ff, title = "Dripfly", description = "Element: Water\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: Its small body can absorb and filter water, removing dangerous toxins.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238787739136031/card-WaterDragonfly-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Hailhog" or creature == "hailhog":
    embed=discord.Embed(color=0x6ab0ff, title = "Hailhog", description = "Element: Water\nRarity: Common\nPower Cost: 1\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: An adorable creature that lives in small, self-made dens of snow. Be wary of their ice tusks!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238569132027904/card-IceBoar-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "hopslop" or creature == "Hopslop":
    embed=discord.Embed(color=0x6ab0ff, title = "Hopslop", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A toad-like creature that sspends its days lounging away in shallow ponds.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238560986665060/card-Hopslop-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Blizzape" or creature == "blizzape":
    embed=discord.Embed(color=0x6ab0ff, title = "Blizzape", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: This agile creature travels in small groups. Their fur is highly cold resistant")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238814163238962/card-WaterMonkey-level-1.png")
      
    await ctx.send (embed = embed)
  
  elif creature == "Gloomtrap" or creature == "gloomtrap":
    embed=discord.Embed(color=0x6ab0ff, title = "Gloomtrap", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: Using its beautiful ice gem, it lures unsuspecting creatures into its fearsome jaws.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238828461650010/card-WaterNormalAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Hummrush" or creature == "hummrush":
    embed=discord.Embed(color=0x6ab0ff, title = "Hummrush", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A cute, winged creature that generates beautiful showers of rain drops.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238567185842257/card-Hummice-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "icitar" or creature == "Icitar":
    embed=discord.Embed(color=0x6ab0ff, title = "Icitar", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: Dwelling in frozen seas, its icy spear-like nose can pierce almost any material.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238570088312932/card-Icitar-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Lennington" or creature == "lennington" or creature == "Lenny" or creature == "lenny" :
    embed=discord.Embed(color=0x6ab0ff, title = "Lennington", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: War Horns\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A naive naval officer for the WTC. Has difficulty commanding the respect of his crew, but makes up for it with enthusiasm.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238783997812797/card-WarHornSeaLion-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Sneetle" or creature == "sneetle":
    embed=discord.Embed(color=0x6ab0ff, title = "Sneetle", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 1 | 2 | 3 | 4 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: Lives in snowy environments. It creates a snowball in which it refridgerates its food.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238851714850857/card-WaterWeakAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "swellwhal" or creature == "Swellwhal" or creature == "Swellwal" or creature == "swellwal":
    embed=discord.Embed(color=0x6ab0ff, title = "Swellwhal", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A whimsical sea creature with a razor-sharp horn. An incredibly agile swimmer.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238824498016286/card-WaterNarwhal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Toxigil" or creature == "toxigil":
    embed=discord.Embed(color=0x6ab0ff, title = "Toxigil", description = "Element: Water\nRarity: Common\nPower Cost: 2\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 0 | 1 | 2 | 3 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: A dangerous fish creature that leaves behind a trail of toxic goop as it swims.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238741790556160/card-Toxigil-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Billsworth" or creature == "billsworth":
    embed=discord.Embed(color=0x6ab0ff, title = "Billsworth", description = "Element: Water\nRarity: Common\nPower Cost: 3\nAbility: Knight\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 0 | 1 | 2 | 3 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A gallant knight that has very little sense of danger. Adept at combat in both the sea and air.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238308200177754/card-Billsworth-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Capychilla" or creature == "capychilla" or creature == "capy" or creature == "Capy":
    embed=discord.Embed(color=0x6ab0ff, title = "", description = "Element: Water\nRarity: Common\nPower Cost: 3\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 1 | 2 | 3 | 4\nInformation: A frozen rodent that’s perpetually chilly, despite its seemingly warm coat of fur.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238334481694780/card-Capychilla-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Chillamari" or creature == "chillamari":
    embed=discord.Embed(color=0x6ab0ff, title = "Chillamari", description = "Element: Water\nRarity: Common\nPower Cost: 3\nAbility: Home Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: The crowned jewel beset in its head can blind creatures with its benevolent beauty.")
    embed.set_thumbnail(url="hhttps://cdn.discordapp.com/attachments/872236731397734431/872238806672216094/card-WaterGroundAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Floodmingo" or creature == "floodmingo" or creature == "friday" or creature == "Friday":
    embed=discord.Embed(color=0x6ab0ff, title = "Floodmingo", description = "Element: Water\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 8 | 9 | 10 | 11 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: Its beautiful feathers reflect brilliant colors into the shallow pools of its surroundings.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238796995964948/card-WaterFlamingo-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "latsu" or creature == "Latsu":
    embed=discord.Embed(color=0x6ab0ff, title = "Latsu", description = "Element: Water\nRarity: Epic\nPower Cost: 3\nAbility: Push\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 4 | 5 | 6 | 7 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A martial arts master. His smooth dance-like fighting style makes him difficult to combat.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238586269925386/card-Latsu-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Shiverscale" or creature == "shiverscale" or creature == "shiver" or creature == "Shiver":
    embed=discord.Embed(color=0x6ab0ff, title = "Shiverscale", description = "Element: Water\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 0 | 1 | 2 | 3 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: This reptilian creature that makes its home among glacier walls. It can scale icy structures with ease.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238841073901629/card-WaterStrongAnimal3-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "stingstream" or creature == "Stingstream":
    embed=discord.Embed(color=0x6ab0ff, title = "Stingstream", description = "Element: Water\nRarity: Common\nPower Cost: 3\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 7 | 8 | 9 | 10 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: It can generate its water-tail at will, using it to quickly strike its prey at breackneck speeds.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238832022597692/card-WaterStingray-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Suttlebub" or creature == "suttlebub" or creature == "Scuttlebub" or creature == "scuttlebub":
    embed=discord.Embed(color=0x6ab0ff, title = "Suttlebub", description = "Element: Water\nRarity: Rare\nPower Cost: 3\nAbility: Shifter\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: Even with tiny legs, this creature is extremely fast. It’s able to blend into the environment to hide from predators.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238682550181888/card-Scuttlebub-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Briskis" or creature == "briskis":
    embed=discord.Embed(color=0x6ab0ff, title = "Briskis", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: One of the few bug-like creatures that prefers cold climates. Avoid its razor sharp blades.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238325812047942/card-Briskis-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Bunnal" or creature == "bunnal":
    embed=discord.Embed(color=0x6ab0ff, title = "Bunnal", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 8 | 9 | 10 | 11 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: An exceedingly rare creature that makes its home among the coral reefs of the sea.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238331713450085/card-Bunnal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Frostbite" or creature == "forstbite":
    embed=discord.Embed(color=0x6ab0ff, title = "Forstbite", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 8 | 9 | 10 | 11 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A ferocious tiger with razor-sharp icicle fangs. Its tail is equally as dangerous.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238846182567986/card-WaterStrongerAnimal2-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Gallosplash" or creature == "gallosplash" or creature == "Gallo" or creature == "gallo" :
    embed=discord.Embed(color=0x6ab0ff, title = "Gallosplash", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility:Upper Hand\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 2 | 3 | 4 | 5 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: Has the ability to gallop straight across the sea. Powerful, fierce, and determined.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238836011393105/card-WaterStrongAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "MasterCai" or creature == "mastercai" or creature == "Master_Cai" or creature == "Master_cai" or creature == "master_cai" or creature == "Cai" or creature ==  "cai" or creature == "master" or creature == "Master" or creature == "master" or creature == "Master":
    embed=discord.Embed(color=0x6ab0ff, title = "Master Cai", description = "Element: Water\nRarity: Epic\nPower Cost: 4\nAbility: Poison\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A master martial artist and Ranno’s mentor. A role model of both balance and strength.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655452834525294/card-MasterCai-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Plippaw" or creature == "plippaw":
    embed=discord.Embed(color=0x6ab0ff, title = "Plippaw", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 1 | 2 | 3 | 4 \n :arrow_left: =  1 | 2 | 3 | 4\nInformation: A rare, exceedingly shy creature that can produce water from its tail. Tremendously cute.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238431223300106/card-FennecFox-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Torremur" or creature == "torremur":
    embed=discord.Embed(color=0x6ab0ff, title = "Torremur", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 9 | 10 | 11 | 12 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: One of the 4 elemental watchers. Her curiosity gets her into more trouble than she’d like to admit.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238843783442492/card-WaterStrongerAnimal1-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Tsculami" or creature == "tsuclami":
    embed=discord.Embed(color=0x6ab0ff, title = "Tsuclami", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: Ally\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 2 | 3 | 4 | 5 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: Its soft, vulnerable body is protected by its strong outer shell.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238760832692285/card-Tsuclami-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Yakcicle" or creature == "yakcicle":
    embed=discord.Embed(color=0x6ab0ff, title = "Yakcicle", description = "Element: Water\nRarity: Rare\nPower Cost: 4\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 7 | 8 | 9 | 10 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A big, bulky creature found only in the coldest regions of the world.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238838418915358/card-WaterStrongAnimal2-level-1.png")
    
    await ctx.send (embed = embed)  
 
  elif creature == "Brutice" or creature == "brutice":
    embed=discord.Embed(color=0x6ab0ff, title = "Brutice", description = "Element: Water\nRarity: Epic\nPower Cost: 5\nAbility: Defender\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 9 | 10 | 11 | 12 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: Big, burly, and mean. His shell is unbreakable and freezes anything it comes in contact with.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238792466116658/card-WaterEpicOffensiveAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Chillchomp" or creature == "chillchomp" or creature == "Chomp" or creature == "chomp" :
    embed=discord.Embed(color=0x6ab0ff, title = "Chillchomp", description = "Element: Water\nRarity: Epic\nPower Cost: 5\nAbility: Power Up\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A powerful creature hailing from prehistoric times. Its icy jaw can crush bone.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238849101803520/card-WaterSuperStrongAnimal-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Hornfrost" or creature == "hornfrost":
    embed=discord.Embed(color=0x6ab0ff, title = "Hornforst", description = "Element: Water\nRarity: Epic\nPower Cost: 5\nAbility: Avatar\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 2 | 3 | 4 | 5\nInformation: A gigantic beast tainted by corruption. Its black ice antlers are as splendid as they are deadly.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238564350504970/card-Hornfrost-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Kinguin" or creature == "kinguin":
    embed=discord.Embed(color=0x6ab0ff, title = "Kinguin ", description = "Element: Water\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 4 | 5 | 6 | 7 \n :arrow_left: = 10 | 11 | 12 | 13\nInformation: A self-proclaimed king, this muscular hunk of feathered royalty is not to be tossled with.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238571724091402/card-Kinguin-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Serpensaur" or creature == "serpensaur":
    embed=discord.Embed(color=0x6ab0ff, title = "Serpensaur", description = "Element: Water\nRarity: Epic\nPower Cost: 5\nAbility: none\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 12 | 13 | 14 | 15 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 0 | 1 | 2 | 3\nInformation: A mystical sea dragon that resides within deepest recesses of the ocean.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238694961135706/card-Serpensaur-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Absa" or creature == "absa":
    embed=discord.Embed(color=0xbf96df, title = "Absa", description = "Element: Air\nRarity: Legendary\nAbility: Voltmatch\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A famed engineer and martial artist, her skill with lightning is a force to be reckoned with.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238233688363088/card-Absa-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Clairen" or creature == "clairen":
    embed=discord.Embed(color=0xd33c30, title = "Clairen", description = "Element: Fire\nRarity: Legendary\n Ability: Plasma Field\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 5 | 6 | 7 | 8\nInformation: A seasoned warrior from the future. She’s come to the past on a noble mission to save her kingdom.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238339925897216/card-Clairen-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Elliana" or creature == "elliana" or creature == "Elli" or creature == "elli":
    embed=discord.Embed(color=0xbf96df, title = "Elliana", description = "Element: Air\nRarity: Legendary\nAbilities: Missile Barrage and Overheat\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 1 | 2 | 3 | 4 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: An ambitious pilot equipped with a deadly, weaponized flying machine.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238425837826138/card-Elliana-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Etalus" or creature == "etalus" or creature == "eta" or creature == "Eta":
    embed=discord.Embed(color=0x6ab0ff, title = "Etalus", description = "Element: Water\nRarity: Legendary\nAbility: Ice Armor\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: A legendary warrior from the Ice Barrens. One of the last surviving members of the ‘Harbor Guard’.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238427523923983/card-Etalus-level-1.png")
 
    await ctx.send (embed = embed)
 
  elif creature == "Fleet" or creature == "fleet":
    embed=discord.Embed(color=0xbf96df, title = "Fleet", description = "Element: Air\nRarity: Legendary\nAbility: Stamina\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: Julesvale’s very own Robin Hood. She protects the downtrodden and stands up to Badger Co.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238524550754375/card-Fleet-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Forsburn" or creature == "forsburn" or creature == "fors" or creature == "Fors":
    embed=discord.Embed(color=0xd33c30, title = "Forsburn", description = "Element: Fire\nRarity: Legendary\nAbility: Smokescreen\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 7 | 8 | 9 | 10 \n :arrow_right: = 8 | 9 | 10 | 11 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: Leader of the ‘Smoke Clan’, this disgraced exile plots to reclaim the corrupted Fire Capital.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238537888628767/card-Forsburn-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Kragg" or creature == "kragg":
    embed=discord.Embed(color=0x63bf3c, title = "Kragg", description = "Element: Earth\nRarity: Legendary\nAbility: Rock <a:kraggrock:867927454164058123>\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 7 | 8 | 9 | 10 \n :arrow_right: = 4 | 5 | 6 | 7 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: A fierce defender of the forest, he patrols the border atop the massive Rock Wall.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238585842135080/card-Kragg-level-1.png")
 
    await ctx.send (embed = embed)
 
  elif creature == "Maypul" or creature == "maypul":
    embed=discord.Embed(color=0x63bf3c, title = "Maypul", description = "Element: Earth\nRarity: Legendary\nAbility: Spreading Roots\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 6 | 7 | 8 | 9 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 7 | 8 | 9 | 10 \nInformation: Self-appointed guardian of the Aetherian Forest. She possesses incredible agility.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655641183920198/card-Maypul-level-1.png")
 
    await ctx.send (embed = embed)
 
  elif creature == "Orcane" or creature == "orcane" or creature == "orca"  or creature == "Orca":
    embed=discord.Embed(color=0x6ab0ff, title = "Orcane", description = "Element: Water\nRarity: Legendary\nAbility: Puddleport\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 7 | 8 | 9 | 10 \n :arrow_right: = 7 | 8 | 9 | 10 \n :arrow_down: = 4 | 5 | 6 | 7 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: The puddle jumping trickster is as slippery as he is playful.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238628435283988/card-Orcane-level-1.png")
        
    await ctx.send (embed = embed)
 
  elif creature == "Ranno" or creature == "ranno":
    embed=discord.Embed(color=0x6ab0ff, title = "Ranno", description = "Element: Water\nRarity: Legendary\nAbility: Bubble Flip\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 6 | 7 | 8 | 9 \n :arrow_left: = 7 | 8 | 9 | 10\nInformation: A martial arts master with a peaceful disposition.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238651986292796/card-Ranno-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Sylvanos" or creature == "sylvanos" or creature == "sylv"  or creature == "Sylv":
    embed=discord.Embed(color=0x63bf3c, title = "Sylvanos", description = "Element: Earth\nRarity: Legendary\nAbility: Untamed Growth\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 3 | 4 | 5 | 6 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 3 | 4 | 5 | 6 \n :arrow_left: = 3 | 4 | 5 | 6\nInformation: A powerful creature heralded as ‘the heart of the forest’.")
    embed.set_thumbnail(url="hhttps://cdn.discordapp.com/attachments/872236731397734431/872238733502595153/card-Sylvanos-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Wrastor" or creature == "wrastor":
    embed=discord.Embed(color=0xbf96df, title = "Wrastor", description = "Element: Air\nRarity: Legendary\nAbility: Tornado\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 3 | 4 | 5 | 6 \n :arrow_down: = 2 | 3 | 4 | 5 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: The infamous Aerial Ace of the ‘Air Armada’. His arrogance knows no bounds.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238857691734026/card-Wrastor-level-1.png")
    
    await ctx.send (embed = embed)
  elif creature == "Zetterburn" or creature == "zetterburn" or creature == "zetter" or creature == "Zetter":
    embed=discord.Embed(color=0xd33c30, title = "Zetterburn", description = "Element: Fire\nRarity: Legendary\nAbility: Scorch\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 5 | 6 | 7 | 8 \n :arrow_right: = 8 | 9 | 10 | 11 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 6 | 7 | 8 | 9\nInformation: Known as the “Fire Roar”, he is an immensely powerful warrior of the Firelands.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238230186115102/card-Zetterburn-level-1.png")
    
    await ctx.send (embed = embed)
 
  elif creature == "Slade" or creature == "slade": 
    embed = discord.Embed(color=0x6ab0ff, title="Slade", description = "Element: Water\nRarity: Legendary\nAbility: Thief's Gambit\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 6 | 7 | 8 | 9 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: = 5 | 6 | 7 | 8 \n :arrow_left: = 7 | 8 | 9 | 10\nInformation: Slade’s penchant for stealing led him from the Poleki Islands to a swashbuckling pirate life")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872238707112017970/card-Slade-level-1.png")

    await ctx.send (embed = embed)
  elif creature == "Guadua" or creature == "guadua":
    embed=discord.Embed(color=0x63bf3c, title = "Guadua", description = "Element: Earth\nRarity: Legendary\nAbility: Bamboo Bayonet\nStats(lvl 1 | 2 | 3 | 4): \n :arrow_up: = 4 | 5 | 6 | 7 \n :arrow_right: = 5 | 6 | 7 | 8 \n :arrow_down: =6 | 7 | 8 | 9 \n :arrow_left: = 4 | 5 | 6 | 7\nInformation: The biggest, baddest panda that the world of Rivals has ever seen.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872654382645280830/card-Guadua-level-1.png")
    await ctx.send (embed = embed)
  elif creature == "Rivals" or creature == "rivals":
    embed = discord.Embed(title="Rivals", description="From left to right, top to bottom:\nAbsa (Ability: Voltmatch)\nMaypul (Ability: Spreading Roots)\nOrcane (Ability: Puddleport)\nZetterburn (Ability: Scorch)\nClairen (Ability: Plasma Field)\nEtalus(Ability: Ice Armor)\nWrastor (Ability: Tornado)\nSylvanos (Ability: Untamed Growth)\nForsburn (Ability: Smokescreen)\nKragg (Ability: Rock)\nFleet (Ability: Stamina Dice)\nRanno (Ability: Bubble Flip)\nElliana (Abilities: Missile Barrage and Overheat)\nSlade (Ability: Thief's Gambit)\nGuadua (Ability: Bamboo Bayonet)", color=0xefdb77)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/872236731397734431/872240621644042371/Design_sem_nome_1.png")
    await ctx.send (embed = embed)

  else: 
    await ctx.send (f"I'm sorry, I don't know this creature, make sure you spelled it correctly or check with @jpedromed")
@client.command()
async def skins(ctx):
  embed=discord.Embed(title="Champion Skins", description = "Champions Skins are obtainable through participation in tournaments. For more information, react to this message: (https://discord.com/channels/695434412451561542/695442626878504970/725182318381236274) and then head over to the #tournament-faq channel\n Obtainable for: Zetterburn, Absa, Orcane, Maypul, Clairen, Etalus, Wrastor, Sylvanos, Forsburn, Kragg, Fleet, Ranno and Elliana so far.", color=0x1e212a)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655752689512548/card-Fleetchampion-level-1.png")
  await ctx.send (embed = embed)
  embed=discord.Embed(title="Master Skins", description = "Master Skins are given to the top 100 on the in-game leaderboard at the end of a season. The Master Skin given is the one for the Rival from the Rival Pass from when the player got Top 100.\nObtainable for: Sylvanos, Forsburn, Kragg, Fleet, Ranno and Elliana so far.", color=0x72d1a0)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655767277277234/card-Fleetmaster-level-1.png")
  await ctx.send (embed = embed)
  embed=discord.Embed(title="Gameboy Skins", description = "For the four starter Rivals, Gameboy skins were given to the people who played the game's Beta at least once from July 31st, 2020, to September 28th, 2020; For new Rivals, starting with Forsburn,Gameboy skins were awarded for people who bought the Rival Pass and got to at least tier 5 of it.\nObtainable for: Absa, Zetterburn, Maypul, Orcane, Forsburn, Kragg, Fleet, Ranno, Elliana and Slade so far.", color=0xa6b95c)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655755436769310/card-Fleetgameboy-level-1.png")
  await ctx.send (embed = embed)
  embed=discord.Embed(title="Golden Skins", description = "Golden skins are given to you when you reach 500 affection with a creature (the ribbons when you click on a card's info).\nObtainable for: Every creature.", color=0xffeb85)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655763217190973/card-Fleetgolden-level-1.png")
  await ctx.send (embed = embed)
  embed=discord.Embed(title="Premium Skins", description = "Premium skins or Seasonal skins are skins that have to be bought through bundles on the shop. Each bundle usually contains the skin, a copy of the card that skins is for (or multiple, if it's not a legendary), 30 thousand coins and 250 orbs and usually cost 10 USD. They are only available during certain periods, but most likely will appear again when time comes.\nObtainable for: Absa, Maypul, Zetterburn, Etalus, Folet, Joltbeak, Wrastor, Forsburn, Orcane, Fleet, Kragg, Master Cai, Ranno, Elliana, Swiftwing and Slade so far.", color=0x765d79)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872236731397734431/872655759559757824/card-Fleetlovers-level-1.png")
  await ctx.send (embed = embed)
#this is the command for abilities. I have to send the gif as a separate message because gifs on embeds have a very bad frame rate
@client.command()
async def a(ctx, ability=None):
  variavel = ability
  if ability is None :
     await ctx.send ("Use $a followed by an ability's name to see info about it.")
  elif ability == "Homefield" or ability == "HomeField" or ability == "homefield" or ability == "HF" or ability == "hf" or ability == "home_field" or ability == "Home_field" or ability == "Home_Field" or ability == "Home" or ability == "home" :
    embed=discord.Embed(color= 0xd3d5e4, title = "Home Field", description = "Stat Cost: 4\nDescription: Applies +1 to all open neighboring tiles of the creature's element and non-element tiles and -1 to open tiles of other elements\nUnlocks at: Arena 3 (Fire Capital)\nCreature(s) with this ability: Muddel <:el_earth:863078639779971102>, Sneetle <:el_water:863078639541420043>, Charclaw <:el_fire:863078639709323295>, Pluffel <:el_air:863078639575105626>, Chillamari <:el_water:863078639541420043>, Jellikid <:el_air:863078639575105626>, Ursun <:el_fire:863078639709323295> and Oremol <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send('https://imgur.com/LollBwE')

  elif ability == "defender" or ability == "Defender" or ability == "DF" or ability == "df" or ability == "Df":
    embed=discord.Embed(color= 0xda73e3, title = "Defender", description = "Stat Cost: 2\nDescription: Give +1 to every creature on the board you control.\nUnlocks at: Arena 2 (Training 2)\nCreature(s) with this ability: Icitar <:el_water:863078639541420043>, Chowl <:el_fire:863078639709323295>, Skyfoal <:el_air:863078639575105626>, Liztrot <:el_earth:863078639779971102>, Firefang <:el_fire:863078639709323295>, Yakcicle <:el_water:863078639541420043>, Ridgehorn <:el_earth:863078639779971102>, Cirriphant <:el_air:863078639575105626>, Lumbergard <:el_earth:863078639779971102>, Blazeen <:el_fire:863078639709323295>, Grizzulus <:el_air:863078639575105626> and Brutice <:el_water:863078639541420043>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/qxoVAbD")
  
  elif ability == "Shifter" or ability == "shifter" or ability == "S" or ability == "s" or ability == "Sh" or ability == "sh" or ability == "SH" :
    embed=discord.Embed(color= 0x5387ff, title = "Shifter", description = "Stat Cost: 3\nDescription: When this card is played on an elemental slot, it shifts its element to that slot's element and gains its benefits.\nUnlocks at: Arena 4 (Air Armada)\nCreature(s) with this ability: Fluttersnout <:el_air:863078639575105626>, Scarabie <:el_earth:863078639779971102>, Scuttlebub <:el_water:863078639541420043> and Doki <:el_fire:863078639709323295>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/eImC0Xz")

  elif ability == "Powerup" or ability == "PowerUp" or ability == "powerup" or ability == "powerUp" or ability == "power_up" or ability == "Power_Up" or ability == "Power_up" or ability == "power_Up" or ability == "PU" or ability == "pu" or ability == "Pu" or ability == "Power" or ability == "power":
    embed=discord.Embed(color= 0xda73e3, title = "Power Up", description = "Stat Cost: 6\nDescription: This card gets +1 for each creature and tile of the same element as this creature in a 3x3 area around it\nUnlocks at: Arena 5 (The Rock Wall)\nCreature(s) with this ability: Skoal <:el_fire:863078639709323295>, Breegul <:el_air:863078639575105626>, Mudmub <:el_earth:863078639779971102>, Capychilla <:el_water:863078639541420043>, Blazadactyl <:el_fire:863078639709323295>, Plippaw <:el_water:863078639541420043>, Shockjaw <:el_air:863078639575105626>, Birchpaw <:el_earth:863078639779971102>, Chillchomp <:el_water:863078639541420043>, Leffox <:el_earth:863078639779971102>, Slaggo <:el_fire:863078639709323295> and Zango <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/1G9oNXR")

  elif ability == "warhorn" or ability == "WarHorn" or ability == "Warhorn" or ability == "warHorn" or ability == "War_Horn" or ability == "war_horn" or ability == "War_horn" or ability == "war_Horn" or ability == "Horn" or ability == "horn" or ability == "horns" or ability == "Horns" or ability == "WH" or ability == "wh" or ability == "Wh" :
    embed=discord.Embed(color= 0x5387ff, title = "War Horn", description = "Stat Cost: 4\nDescription: When you play this card, pick a non-ability creature from your hand and play it on an open tile then return it to your hand. \nUnlocks at: Arena 6(Merchant Port)\nCreature(s) with this ability: Lennington <:el_water:863078639541420043> and Vanbard <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/cHZ0MJ2")

  elif ability == "wardrums" or ability == "WarDrums" or ability == "Wardrums" or ability == "warDrums" or ability == "War_Drums" or ability == "war_drums" or ability == "War_drums" or ability == "war_Drums" or ability == "Drums" or ability == "drums" or ability == "WD" or ability == "wd" or ability == "Wd" :
    embed=discord.Embed(color= 0x5387ff, title = "War Drums", description = "Stat Cost: 0\nDescription: Grants up to 2 non-ability creatures, when summoned, +3 (does not stack with other drums) \nUnlocks at: Arena 6(Merchant Port)\nCreature(s) with this ability: Sidgar <:el_fire:863078639709323295> and Babidon <:el_earth:863078639779971102>\nNote: If a card is summoned by War Horn while War Drums is active, that card will keep the +3 when it returns to the player's hand.")
    await ctx.send (embed=embed)
    await ctx.send ("https://imgur.com/G8WJsE8")
  elif ability == "Upperhand" or ability == "UpperHand" or ability == "upperHand" or ability == "upperhand" or ability == "Upper_hand" or ability == "Upper_Hand" or ability == "upperh_Hand" or ability == "upper_hand" or ability == "UH" or ability == "uh" or ability == "Uh" or ability == "Upper" or ability == "upper":
    embed=discord.Embed(color= 0x5387ff, title = "Upper Hand", description = "Stat Cost: 4\nDescription: Gains +1 for each creature of the same element as this one in your hand for one turn only\nUnlocks at: Arena 7 (Blazing Hideout)\nCreature(s) with this ability: Pelisprout <:el_earth:863078639779971102>, Cloala <:el_air:863078639575105626>, Flareater <:el_fire:863078639709323295>, Gloomtrap <:el_water:863078639541420043>, Ashe <:el_fire:863078639709323295>, Gallosplash <:el_water:863078639541420043>, Pinepurr <:el_earth:863078639779971102> and Joltbeak <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/jLVJnJ9")

  elif ability == "Ally" or ability == "ally" or ability == "AL" or ability == "al" or ability == "Al" :
    embed=discord.Embed(color= 0x5387ff, title = "Ally", description = "Stat Cost: 4\nDescription: If played next to a creature you control of the same element as this one, that creature will try and recapture any creatures next to it.\nUnlocks at: Arena 8 (Tempest Peak)\nCreature(s) with this ability: Meadant <:el_earth:863078639779971102>, Hummrush <:el_water:863078639541420043>, Platygust <:el_air:863078639575105626>, Porcuber <:el_fire:863078639709323295>, Sunny <:el_fire:863078639709323295>, Sparkfang <:el_air:863078639575105626>, Tsuclami <:el_water:863078639541420043> and Mudmo <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/EFFtZ32")
  elif ability == "knight" or ability == "knights" or ability == "Knight" or ability == "Knights" or ability == "K" or ability == "k":
    embed=discord.Embed(color=0xda73e3, title = "Knight", description = "Stat Cost: 1\nDescription: When capturing a creature, jump to any adjacent space of the captured creature. When landing, this card regains its flip potential.\nUnlocks at: Arena 9 (Treetop Lodge)\nCreature(s) with this ability: Flitch <:el_fire:863078639709323295>, Billsowrth <:el_water:863078639541420043>, Minto <:el_earth:863078639779971102> and Freyden <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/I2ixL0P")
  elif ability == "Push" or ability == "push" or ability == "P" or ability == "p" :
    embed=discord.Embed(color=0xda73e3, title = "Push", description = "Stat Cost: 0\nDescription: Pulls the nearest creatures in each cardinal direction towards it. After resolving flips, pushes each creature in the same direction it came.\nUnlocks at: Arena 10 (Frozen Fortress)\nCreature(s) with this ability: Serilia <:el_fire:863078639709323295>, Latsu <:el_water:863078639541420043>, Torong <:el_earth:863078639779971102> and Herra <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/RVeu4GV")
  elif ability == "Avatar" or ability == "avatar" or ability == "AV" or ability == "av" or ability == "Av" or ability == "aV" :
    embed=discord.Embed(color=0xda73e3, title = "Avatar", description = "Stat Cost: 7\nDescription: Gets +4 if you currently control all four elements when played, inculding itself.\nUnlocks at: Arena 11 (Neo Fire Capital)\nCreature(s) with this ability: Hornfrost <:el_water:863078639541420043>, Searscale <:el_fire:863078639709323295>, Galespur <:el_air:863078639575105626> and Cliffroach <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/O2zLWEk")
  elif ability == "Raze" or ability == "raze" or ability == "r" or ability == "R" or ability == "Renburn" or ability == "renburn" :
    embed=discord.Embed(color=0xda73e3, title = "Raze", description = "Stat Cost: 0\nDescription: After this card captures another creature, give all creatures on the board -3 (excluding this creature)\nUnlocks at: Arena 12 (Julesvale)\nCreature(s) with this ability: Renburn <:el_fire:863078639709323295> ")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/SsK8EZI")

  elif ability == "Poison" or ability == "poison" or ability == "Po" or ability == "po" or ability == "MasterCai" or ability == "mastercai" or ability == "Mastercai" or ability == "masterCai" or ability == "Cai" or ability == "cai" or ability == "Master_Cai" or ability == "master_cai" or ability == "Master_cai" or ability == "master_Cai" or ability == "PO" or ability == "po" or ability == "Master" or ability == "master":
    embed=discord.Embed(color= 0xda73e3, title = "Poison", description = "Stat Cost: 4\nDescription: At the start of your turn, give all your opponent's creatures -1. Loses this ability when flipped.\nUnlocks at: Arena 12 (Julesvale)\nCreature(s) with this ability: Master Cai <:el_water:863078639541420043> ")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/4Gt4TCz")
  elif ability == "Swoop" or ability == "swoop" or ability == "Swiftwing" or ability == "swiftwing" or ability == "Sw" or ability == "sw" or ability =="SW" or ability =="sW" :
    embed=discord.Embed(color=0xda73e3, title = "Swoop", description = "Stat Cost: 2\nDescription: When played, the creature flies in the longest direction with empty spaces (select direction if tied). This creature will try to flip any creatures it passes.\nUnlocks at: Arena 12 (Julesvale)\nCreature(s) with this ability: Swiftwing <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/tnGZ2qh")
  elif ability == "Metal_Armor" or ability == "metal_armor" or ability == "Metal_armor" or ability == "" or ability == "metal_Armor" or ability == "MatalArmor" or ability == "metalarmor" or ability == "Metalarmor" or ability == "metalArmor" or ability == "Zolt" or ability == "zolt" or ability == "MA" or ability == "ma" or ability == "metal" or ability == "Metal":
    embed=discord.Embed(color=0xda73e3, title = "Metal Armor", description = "Stat Cost: 4\nDescription: Metal armor prevents this creature from being captured, once.\nUnlocks at: Arena 12 (Julesvale)\nCreature(s) with this ability: Zolt <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/N3kxuMZ")
  elif ability == "Rivals" or ability == "rivals":
    await ctx.send("You can check a rival's ability by typing $a and that rival's name; that works for any card with a unique ability.\nYou can see all rivals currently in the game by typing $c rivals")
  elif ability == "Scorch" or ability == "scorch" or ability == "Zetterburn" or ability == "zetterburn" or ability == "Zetter" or ability == "zetter" or ability == "zett" or ability == "zett":
    embed=discord.Embed(color=0xefdb77, title = "Scorch", description = "Description: Removes open elemental tiles from the board. It also removes all debuff from your cards and buffs from opponent's cards including the elemental tiles underneath them.\nRival with this ability: Zetterburn <:el_fire:863078639709323295> ")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/e0MSkvU")
  elif ability == "Smokescreen" or ability == "smokescreen" or ability == "Forsburn" or ability == "forsburn" or ability == "Fors" or ability == "fors":
    embed=discord.Embed(color=0xefdb77, title = "Smokescreen", description = "Description: When played, this creature creates 3x3 smoke tiles. AT the end of your turn, move this creature to another smoke, regaining flip potential. Non-ability cards can remain hidden in smoke.\nRival with this ability: Forsburn <:el_fire:863078639709323295>\nNote: Forsburn can swap places with any card that's hidden in smoke, unless that card is controlled by another player; Forsburn will regain flip potential when doing that, but the other card won't.")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/qKzEvxW")
  elif ability == "Puddleport" or ability == "puddleport" or ability == "Orcane" or ability == "orcane" or ability == "orca" or ability == "Orca":
    embed=discord.Embed(color=0xefdb77, title = "Puddleport", description = "Description: Captrues creatures from a distance using water spouts. Spouts can wrap the board to hit from the opposing side.\nRival with this ability: Orcane <:el_water:863078639541420043>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/K5mOsAo")
  elif ability == "StaminaDice" or ability == "staminadice" or ability == "Staminadice" or ability == "staminaDice" or ability == "Stamina_Dice" or ability == "stamina_dice" or ability == "Stamina_dice" or ability == "stamina_Dice" or ability == "Dice" or ability == "dice" or ability == "Fleet" or ability == "fleet" or ability == "stamina" or ability == "Stamina":
    embed=discord.Embed(color=0xefdb77, title = "Stamina Dice", description = "Description: Starts the game with 6 Stamina. Each turn, you can spend Stamina to add a modifier to the next creature you play. Spends all remaining Stamina when this card is played.\nRival with this ability: Fleet <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/zMsPNAz")
  elif ability == "Tornado" or ability == "tornado" or ability == "Wrastor" or ability == "wrastor" or ability == "Wras" or ability == "wras":
    embed=discord.Embed(color=0xefdb77, title = "Tornado", description = "Description: Summon a Tornado that can move a creature through open slots. The moved creature regains is flip potential.\nRival with this ability: Wrastor <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/F7IBZj4")
  elif ability == "Voltmatch" or ability == "voltmatch" or ability == "Match" or ability == "match" or ability == "Absa" or ability == "absa":
    embed=discord.Embed(color=0xefdb77, title = "Voltmatch", description = "Description: Shock any neighboring card with a matching power with Absa. Shocked cards will try to shock any card with numbers smaller than or equal to themselves. Attempt to capture all shocked cards.\nRival with this ability: Absa <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/Ly4b77h")
  elif ability == "Rock" or ability == "rock" or ability == "Kragg" or ability == "kragg":
    embed=discord.Embed(color=0xefdb77, title = "Rock", description = "Description: When played, select an empty tile to place a rock in that space. Your opponent can't play on that tile.\nRival with this ability: Kragg <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/msDGQpg")
  elif ability == "MissileBarrage" or ability == "missilebarrage" or ability == "Missilebarrage" or ability == "missileBarrage" or ability == "Missile" or ability == "missile" or ability == "Missile_Barrage" or ability == "missile_barrage" or ability == "Missile_barrage" or ability == "missile_Barrage" or ability == "missile" or ability == "Missile":
    embed=discord.Embed(color=0xefdb77, title = "Missile Barrage", description = "Description: Creates a missile for every exposed side with power equal to that side. This missile fires and flips the furthest creature with any power lower than that missile.\nRival with this ability: Elliana <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/mNt6BYw")
  elif ability == "Overheat" or ability == "overheat":
    embed=discord.Embed(color=0xefdb77, title = "Overheat", description = "Description: Has +5 power while overheated. When played, select a tile to jump to. When landing, lose your overheat and regain your flip potential.\nRival with this ability: Elliana <:el_air:863078639575105626>\nNote: Missile Barrage becomes Overheat when the Elliana player has only 3 cards remaining on their hand.")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/YrUzyQD")
  elif ability == "elliana" or ability == "Elliana" or ability == "Elli" or ability == "elli":
    embed=discord.Embed(color=0xefdb77, title = "Missile Barrage", description = "Description: Creates a missile for every exposed side with power equal to that side. This missile fires and flips the furthest creature with any power lower than that missile.\nRival with this ability: Elliana <:el_air:863078639575105626>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/mNt6BYw")
    embed=discord.Embed(color=0xefdb77, title = "Overheat", description = "Description: Has +5 power while overheated. When played, select a tile to jump to. When landing, lose your overheat and regain your flip potential.\nRival with this ability: Elliana <:el_air:863078639575105626>\nNote: Missile Barrage becomes Overheat when the Elliana player has only 3 cards remaining on their hand.")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/YrUzyQD")
  elif ability == "BubbleFlip" or ability == "bubbleflip" or ability == "Bubbleflip" or ability == "bubbleFlip" or ability == "Bubble_Flip" or ability == "bubble_flip" or ability == "bubble_Flip" or ability == "Bubble_flip" or ability == "Ranno" or ability == "ranno" or ability == "bubble" or ability == "Bubble":
    embed=discord.Embed(color=0xefdb77, title = "Bubble Flip", description = "Description: Pulls all opponent creatures from a distance. If they are captured, places them into a bubble that prevents capture once. At the start of your turn, bubbles pop, creatures inside regain their flip potential.\nRival with this ability: Ranno <:el_water:863078639541420043>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/JGPBYzz")
  elif ability == "Thief'sGambit" or ability == "thief'sgambit" or ability == "Thief'sgambit" or ability == "thief'sGambit" or ability == "ThiefsGambit" or ability == "thiefsgambit" or ability == "Thiefsgambit" or ability == "thiefsGambit" or ability == "ThiefGambit" or ability == "thiefgambit" or ability == "Thiefgambit" or ability == "thiefGambit" or ability == "Slade" or ability == "slade" or ability == "Thief's_Gambit" or ability == "thief's_gambit" or ability == "Thief's_gambit" or ability == "thief's_Gambit" or ability == "Thiefs_Gambit" or ability == "thiefs_gambit" or ability == "Thiefs_gambit" or ability == "thiefs_Gambit" or ability == "Thief_Gambit" or ability == "thief_gambit" or ability == "Thief_gambit" or ability == "thief_Gambit" or ability == "Thief's" or ability == "thief's" or ability == "Thiefs" or ability == "thiefs" or ability == "Thief" or ability == "thief":
    embed=discord.Embed(color=0xefdb77, title = "Thief's Gambit", description = "Description: When played, take a creature owned by you and replace it with one in your had\nRival with this ability: Slade <:el_water:863078639541420043>\nNote: The card taken keeps any stat modifiers that aren't from tiles and the card used to replace it does not activate its ability and doesn't have flip potential.")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/G8sUBP3")
  elif ability == "PlasmaField" or ability == "plasmafield" or ability == "Plasmafield" or ability == "plasmaField" or ability == "Clairen" or ability == "clairen" or ability == "Plasma_Field" or ability == "plasma_field" or ability == "Plasma_field" or ability == "plasma_Field"  or ability == "plasma" or ability == "Plasma":
    embed=discord.Embed(color=0xefdb77, title = "Plasma Field", description = "Description: When flipped, a Plasma Field spawns, preventing opponent card abilities. If not flipped by the end of the match, attempts to flip all surrounding cards\nRival with this ability: Clairen <:el_fire:863078639709323295>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/t4hEweN")
    await ctx.send("https://imgur.com/t4ORRud")
  elif ability == "SpreadingRooots" or ability == "spreadingroots" or ability == "Spreadingroots" or ability == "spreadingRoots" or ability == "Maypul" or ability == "maypul" or ability == "Spreading_Rooots" or ability == "spreading_roots" or ability == "Spreading_roots" or ability == "spreading_Roots" or ability == "spreading" or ability == "Spreading":
    embed=discord.Embed(color=0xefdb77, title = "Spreading Roots", description = "Description: Spreads roots onto a single neighboring opponent creature with a smaller power than her. The rooted creature then attempts the same on its neighbors, resulting in a chain. At the end of the chain, attempts to capture all rooted cards.\nRival with this ability: Maypul <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/SbSMl5i")
  elif ability == "UntamedGrowth" or ability == "untamedgrowth" or ability == "Untamedgrowth" or ability == "untamedGrowth" or ability == "Sylvanos" or ability == "sylvanos" or ability == "Untamed_Growth" or ability == "untamed_growth" or ability == "Untamed_growth" or ability == "untamed_Growth" or ability == "Sylv" or ability == "sylv" or ability == "untamed" or ability == "Untamed":
    embed=discord.Embed(color=0xefdb77, title = "Untamed Growth", description = "Description: When played on an elemental slot, Sylvanos consumes it, leaving the tile empty. He then spreads the consumed element across the board adding +1 on open slots and flipping all cards of that element with at least one side lower than its power values.\nRival with this ability: Sylvanos <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/l5VFuic")
  elif ability == "IceArmor" or ability == "icearmor" or ability == "Icearmor" or ability == "iceArmor" or ability == "Etalus" or ability == "etalus" or ability == "Ice_Armor" or ability == "icea_rmor" or ability == "Ice_armor" or ability == "ice_Armor" or ability == "Eta" or ability == "eta" or ability == "ice" or ability == "Ice":
    embed=discord.Embed(color=0xefdb77, title = "Ice Armor", description = "Description: Any creature this creature flips is frozen - making them immune to capture\nRival with this ability: Etalus <:el_water:863078639541420043>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/PzpQwf9")
  elif ability == "BambooBayonet" or ability == "bamboobayonet" or ability == "Bamboobayonet" or ability == "bambooBayonet" or ability == "Guadua" or ability == "guadua" or ability == "Bamboo_Bayonet" or ability == "bamboo_bayonet" or ability == "Bamboo_bayonet" or ability == "bamboo_Bayonet" or ability == "bamboo" or ability == "Bamboo" :
    embed=discord.Embed(color=0xefdb77, title = "Bamboo Bayonet", description = "Description: When your other creatures are played, they'll sprout bamboos on diagonally adjacent tiles. For each bamboo this creature is played on, gain +2 and increase your flip range by 1.\nRival with this ability: Guadua <:el_earth:863078639779971102>")
    await ctx.send (embed = embed)
    await ctx.send("https://imgur.com/81d6sUg")
  else:
    await ctx.send(f"I'm sorry, I don't know this ability, make sure you spelled it correctly or check with @jpedromed.")
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)