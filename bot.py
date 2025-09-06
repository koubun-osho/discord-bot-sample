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

# 特定のサーバー（ギルド）IDを設定
TARGET_GUILD_ID = 1386313046590492724

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました！')
    try:
        # スラッシュコマンドを同期
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期しました")
    except Exception as e:
        print(f"コマンドの同期に失敗しました: {e}")

# /helpスラッシュコマンド
@bot.tree.command(name="help", description="このボットの使い方を表示します")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🤖 Discord Bot ヘルプ",
        description="このボットの使い方を説明します",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="📝 基本機能",
        value="このボットは、送信されたすべてのメッセージに「こんにちは。はろー！よろしくね！」と返信します。",
        inline=False
    )
    
    embed.add_field(
        name="🎯 スラッシュコマンド",
        value="`/help` - このヘルプメッセージを表示します",
        inline=False
    )
    
    embed.add_field(
        name="💡 使い方",
        value="1. チャンネルでメッセージを送信すると、ボットが自動的に返信します\n2. `/help`コマンドでいつでもこのヘルプを確認できます",
        inline=False
    )
    
    embed.set_footer(text="楽しくチャットしましょう！")
    
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return
    
    # 特定のサーバーでのみ返信する
    if message.guild and message.guild.id == TARGET_GUILD_ID:
        await message.channel.send('こんにちは。はろー！よろしくね！')
    
    # コマンドも処理できるようにする
    await bot.process_commands(message)

# Botを起動
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print("エラー: DISCORD_TOKENが設定されていません。.envファイルを確認してください。")