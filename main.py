from os import name
import discord
from discord.channel import GroupChannel
from discord.ext import commands, tasks
from random import choice
from discord.message import Message
import requests
from bs4 import BeautifulSoup
import re
import time

from requests.models import parse_url

def poem():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    ur= 'http://kavitakosh.org/kk/index.php'
    r = requests.get(ur, headers)
    soup1 = BeautifulSoup(r.content, 'html.parser')
    title1 = soup1.findAll(name= 'a', attrs={'href': re.compile("^/kk/%")})
    author = choice(title1)
    author0 = author.text
    ran = str(author)
    pattern = re.compile('"(.*?)\"')
    # print(ran+"\n")
    url = 'http://kavitakosh.org'+re.search(pattern, ran).group(1)
    # print(url)

    r1 = requests.get(url, headers)
    soup2 = BeautifulSoup(r1.content, 'html.parser')
    title2_0 = soup2.find('div', attrs={'class': "mw-content-ltr"})
    title2_1 = soup2.find('div', attrs={'id': 'kkparichay-box'})
    title2_1.clear()
    title2 = title2_0.findAll(name= 'a',attrs={'href': re.compile("^/kk/%")})
    ran2 = str(choice(title2))
    
    URL1 = 'http://kavitakosh.org'+re.search(pattern, ran2).group(1)


    page = requests.get(URL1, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(class_="poem").text
    return(title, author0)

# print(title)



bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('ready')

@bot.event
async def on_message(message):
    if '>kavita' in message.content:
        (title , author) = poem()
        await message.channel.send(title + "\n-" + author)

bot.run('ODQ3MDU3NjE1NzAzNzY5MTQ4.YK4h4Q.AHvcKV0JKg7dgdE4r-KHbwMfeow')
time.sleep(5)
