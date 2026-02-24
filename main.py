from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Configura tu TOKEN y tu TELEGRAM ID aquí
TOKEN = 8376353383:AAGeRugcPXgC1LpA3g6DN227-gRp3Ae4YkM
AUTHORIZED_USER_ID =  7984230912 ejemplo: 123456789

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    await update.message.reply_text("Hola! Bot de apuestas activo ⚽🔥")

# Comando /analisis (ejemplo)
async def analisis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    partido = " ".join(context.args)
    if not partido:
        await update.message.reply_text("Escribe /analisis equipo1 vs equipo2")
        return
    # Aquí más adelante pondremos análisis real
    await update.message.reply_text(f"Analizando partido: {partido}\nPróximamente: Probabilidades y picks de value.")

# Inicializar bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analisis", analisis))

print("Bot iniciado...")
app.run_polling()
