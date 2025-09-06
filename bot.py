import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# Botの設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容を取得するために必要
intents.messages = True  # メッセージを読むために必要
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました！')

@bot.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return
    
    # どんなメッセージにも「こんにちは。はろー！よろしくね！」と返す
    await message.channel.send('こんにちは。はろー！よろしくね！')
    
    # コマンドも処理できるようにする
    await bot.process_commands(message)

# Botを起動
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print("エラー: DISCORD_TOKENが設定されていません。.envファイルを確認してください。")