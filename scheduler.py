from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
from main import analisis, USUARIO_AUTORIZADO, app
from datetime import datetime
import pytz

# Zona horaria Colombia
zona = pytz.timezone("America/Bogota")

# Scheduler
scheduler = AsyncIOScheduler(timezone=zona)

# Función que manda picks de prueba
async def picks_automaticos():
    ahora = datetime.now(zona)
    dia_semana = ahora.weekday()  # 0=lunes ... 6=domingo

    if dia_semana >=5:  # sábado y domingo
        mensaje = "📊 Picks fines de semana:\n1️⃣ Partido de ejemplo\n2️⃣ Otro partido"
    else:  # lunes a viernes
        mensaje = "📊 Picks entre semana (ligas top y Colombia/Argentina)\n1️⃣ Partido ejemplo"

    # Mandar mensaje al usuario autorizado
    chat = await app.bot.get_chat(USUARIO_AUTORIZADO)
    await chat.send_message(mensaje)

# Programar scheduler
# Todos los días a las 6:00 AM
scheduler.add_job(picks_automaticos, CronTrigger(hour=6, minute=0))

# Iniciar scheduler
scheduler.start()
