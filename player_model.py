import numpy as np

# Ejemplo de jugadores con estadísticas simples
# Esto se puede reemplazar luego con datos reales de API
jugadores = {
    "Barcelona": [
        {"nombre": "Lewandowski", "tiros": 4, "goles": 1, "asistencias": 0.5},
        {"nombre": "Pedri", "tiros": 2, "goles": 0.3, "asistencias": 0.8},
    ],
    "Real Madrid": [
        {"nombre": "Benzema", "tiros": 5, "goles": 1.2, "asistencias": 0.6},
        {"nombre": "Modric", "tiros": 1, "goles": 0.2, "asistencias": 1},
    ],
}

def calcular_probabilidades(equipo):
    """
    Retorna probabilidades de tiro, gol y asistencia para cada jugador
    """
    if equipo not in jugadores:
        return []

    resultados = []
    for j in jugadores[equipo]:
        tiros_prob = min(100, j["tiros"] * 20)  # ejemplo: más tiros = más probabilidad
        gol_prob = min(100, j["goles"] * 30)    # más goles = más probabilidad
        asist_prob = min(100, j["asistencias"] * 25)  # más asistencias = más probabilidad

        resultados.append({
            "nombre": j["nombre"],
            "prob_tiro": round(tiros_prob,1),
            "prob_gol": round(gol_prob,1),
            "prob_asistencia": round(asist_prob,1)
        })
    return resultados

from player_model import calcular_probabilidades

equipo = "Barcelona"  # ejemplo, se puede obtener del argumento del usuario
res = calcular_probabilidades(equipo)

mensaje = f"🎯 Probabilidades de jugadores de {equipo}:\n"
for r in res:
    mensaje += f"{r['nombre']}: tiro {r['prob_tiro']}%, gol {r['prob_gol']}%, asistencia {r['prob_asistencia']}%\n"

await update.message.reply_text(mensaje)
