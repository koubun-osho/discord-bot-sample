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
intents.reactions = True  # リアクションを受け取るために必要
bot = commands.Bot(command_prefix='!', intents=intents)

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
        value="1. 送信されたメッセージをそのまま返信します（エコーボット）\n2. 👍リアクションが付けられたときにお知らせします",
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
    
    # 受け取ったメッセージをそのまま返信する
    await message.channel.send(message.content)
    
    # コマンドも処理できるようにする
    await bot.process_commands(message)

# リアクションが追加されたときのイベント（キャッシュされているメッセージのみ）
@bot.event
async def on_reaction_add(reaction, user):
    # Bot自身のリアクションは無視
    if user == bot.user:
        return
    
    # 👍（サムズアップ）リアクションが追加された場合
    if str(reaction.emoji) == '👍':
        # メッセージ内容を取得（長すぎる場合は省略）
        message_content = reaction.message.content
        if len(message_content) > 50:
            message_content = message_content[:50] + '...'
        
        # リアクションが付けられたことを通知
        response = f'👍グッドマークが押されたよ！\n「{message_content}」のメッセージにグッドマークが押されたよ！'
        await reaction.message.channel.send(response)

# 古いメッセージへのリアクションも検知するイベント
@bot.event
async def on_raw_reaction_add(payload):
    # Bot自身のリアクションは無視
    if bot.user and payload.user_id == bot.user.id:
        return
    
    # 👍（サムズアップ）リアクションが追加された場合
    if str(payload.emoji) == '👍':
        # チャンネルを取得
        channel = bot.get_channel(payload.channel_id)
        if channel is None:
            return
        
        # テキストチャンネルかどうか確認
        if not isinstance(channel, discord.TextChannel):
            return
        
        try:
            # メッセージを取得
            message = await channel.fetch_message(payload.message_id)
            
            # メッセージ内容を取得（長すぎる場合は省略）
            message_content = message.content
            if len(message_content) > 50:
                message_content = message_content[:50] + '...'
            
            # リアクションが付けられたことを通知
            response = f'👍グッドマークが押されたよ！\n「{message_content}」のメッセージにグッドマークが押されたよ！'
            await channel.send(response)
        except discord.NotFound:
            pass
        except discord.HTTPException:
            pass

# Botを起動
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print("エラー: DISCORD_TOKENが設定されていません。.envファイルを確認してください。")