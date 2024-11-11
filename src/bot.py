import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

CARGOS_PERMITIDOS = ["Cargo Teste"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

def tem_cargo_permitido(member):
    return any(cargo.name in CARGOS_PERMITIDOS for cargo in member.roles)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')
    print(f'Servidor: {bot.guilds[0].name}')

@bot.command(name='adicionar')
async def adicionar(ctx, member: discord.Member):
    try:
        # Verifica permissão do autor
        if not tem_cargo_permitido(ctx.author):
            await ctx.send("❌ Você não tem permissão para usar este comando!")
            return

        channel = ctx.channel

        # Verifica menções especiais
        if member.mention in ['@everyone', '@here']:
            await ctx.send("❌ Não é possível adicionar everyone ou here!")
            return

        # Verifica se o membro já tem acesso
        if channel.permissions_for(member).read_messages:
            await ctx.send("❌ Este usuário já tem acesso ao canal!")
            return

        # Adiciona o membro ao canal
        await channel.set_permissions(member, read_messages=True, send_messages=True)
        await ctx.send(f"✅ Usuário adicionado com sucesso!")

    except Exception as e:
        await ctx.send("❌ Ocorreu um erro ao adicionar o usuário.")
        print(f"Erro detalhado: {e}")

@bot.command(name='remover')
async def remover(ctx, member: discord.Member):
    try:
        # Verifica permissão do autor
        if not tem_cargo_permitido(ctx.author):
            await ctx.send("❌ Você não tem permissão para usar este comando!")
            return

        channel = ctx.channel

        # Verifica menções especiais
        if member.mention in ['@everyone', '@here']:
            await ctx.send("❌ Não é possível remover everyone ou here!")
            return

        # Verifica se o membro já está sem acesso
        if not channel.permissions_for(member).read_messages:
            await ctx.send("❌ Este usuário já não tem acesso ao canal!")
            return

        # Remove o membro do canal
        await channel.set_permissions(member, read_messages=False, send_messages=False)
        await ctx.send(f"✅ Usuário removido com sucesso!")

    except Exception as e:
        await ctx.send("❌ Ocorreu um erro ao remover o usuário.")
        print(f"Erro detalhado: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Mencione o usuário! Exemplo: !adicionar @usuário")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("❌ Usuário não encontrado!")
    else:
        await ctx.send("❌ Ocorreu um erro ao executar o comando.")
        print(f"Erro não tratado: {error}")

bot.run(os.getenv('DISCORD_TOKEN'))