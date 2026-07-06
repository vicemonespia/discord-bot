import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f" Bot conectado como: {bot.user}")


@bot.command()
async def miri(ctx, tipo: str):
    try:
        tipo = tipo.lower().strip()
        
        # Carpeta donde guardarás tus imágenes
        carpeta = "miris"
        
        posibles_extensiones = ['.png', '.jpg', '.jpeg', '.gif']
        ruta_imagen = None
        
        for ext in posibles_extensiones:
            ruta = f"{carpeta}/{tipo}{ext}"
            if os.path.exists(ruta):
                ruta_imagen = ruta
                break
        
        if not ruta_imagen:
            await ctx.send(f" No tengo la miri de **{tipo}** guardada.")
            await ctx.send(" Prueba con: `basket_truco`, `baile_cuyeya`, `asombrao`, etc.")
            return
        
        # Enviamos la imagen
        await ctx.send(f"**Miri {tipo.capitalize()}** aquí tienes:")
        await ctx.send(file=discord.File(ruta_imagen))
        
    except Exception as e:
        print("Error:", e)
        await ctx.send(" Ocurrió un error al enviar la miri.")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(" Debes escribir el tipo de miri.\nEjemplo: `$miri carrusel`")
    elif isinstance(error, commands.errors.CommandNotFound):
        pass
    else:
        print(f"Error: {error}")

if __name__ == "__main__":
    try:
        import clave
        print("✅ Bot iniciado correctamente")
        bot.run(clave.TOKEN)
    except Exception as e:
        print(" Error:", e)