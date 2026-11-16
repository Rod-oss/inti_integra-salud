import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

VERDE, TERRA, GRIS, CLARO = "#2E5E4E", "#C0703F", "#5B5B5B", "#EEF3F0"
fig, ax = plt.subplots(figsize=(14, 7.6))
ax.set_xlim(0, 152); ax.set_ylim(0, 79); ax.axis("off")

def caja(x, y, w, h, titulo, sub="", color=VERDE, fondo=CLARO, nuevo=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=fondo, ec=TERRA if nuevo else color, lw=2.2 if nuevo else 1.5))
    ax.text(x + w / 2, y + h - 2.6, titulo, ha="center", va="top", fontsize=10.5, fontweight="bold", color=color)
    if sub:
        ax.text(x + w / 2, y + h - 6.4, sub, ha="center", va="top", fontsize=8.3, color=GRIS, linespacing=1.35)

def flecha(a, b, punteada=False, color=VERDE, texto=None, dx=0, dy=1.2):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=14, lw=1.4, color=color,
                                 linestyle=(0, (4, 3)) if punteada else "-"))
    if texto:
        ax.text((a[0] + b[0]) / 2 + dx, (a[1] + b[1]) / 2 + dy, texto, ha="center", fontsize=8, color=color, style="italic")


caja(2, 50, 15, 20, "Usuario", "paciente o\nfamiliar escribe\no adjunta foto", fondo="white")
caja(21, 50, 17, 20, "Interfaz", "cuaderno de\nColab: texto y\ncarga de imagen")
caja(42, 50, 20, 20, "Filtros de\nseguridad", "\nemergencia,\nencuadre clínico\ny contención")
caja(66, 50, 20, 20, "Preprocesamiento\nde texto", "\nNLTK: normalizar,\ntokenizar, stopwords,\nstemming")
caja(90, 58, 20, 12, "Reglas de\ncontexto", "")
caja(90, 33, 20, 19, "Clasificador de\nintenciones", "\nTF-IDF palabras y\ncaracteres + SVM\ncon umbral", nuevo=True)
caja(66, 15, 20, 17, "Preprocesamiento\nde imagen", "\nredimensionar 224,\nnormalizar ImageNet", nuevo=True)
caja(90, 15, 20, 17, "Clasificador\nvisual", "\nEfficientNet-B0,\ntransferencia", nuevo=True)
caja(115, 15, 35, 55, "Gestor de diálogo\ny acciones", "\ninformación del consultorio\norientación sobre homeopatía\nagendar y consultar citas\nderivar a una persona\nregistrar tipo de documento\npedir otra foto\n\ngenerador de respuestas\ncon plantillas")
caja(66, 0.5, 34, 10.5, "Base de conocimiento", "servicios, costos, plantillas, agenda", fondo="white")
caja(110, 0.5, 40, 10.5, "Estado de sesión", "pendiente, contadores, documentos, historial", fondo="white")

flecha((17, 60), (21, 60)); flecha((38, 60), (42, 60))
flecha((62, 62), (66, 62))
flecha((86, 64), (90, 64))
flecha((110, 64), (115, 64))
flecha((100, 58), (100, 52.5), texto="no aplica", dx=5.5, dy=-0.5)
flecha((110, 42), (115, 42))
ax.plot([52, 52], [50, 23.5], color=TERRA, lw=1.4)
flecha((52, 23.5), (66, 23.5), color=TERRA, texto="imagen", dy=1.3)
ax.text(53, 37, "si no hubo\nalerta", fontsize=8, color=TERRA, style="italic")
flecha((86, 23.5), (90, 23.5), color=TERRA)
flecha((110, 23.5), (115, 23.5), color=TERRA)
ax.annotate("", xy=(118, 70.6), xytext=(52, 70.6), arrowprops=dict(arrowstyle="-|>", color=TERRA, lw=1.4, connectionstyle="arc3,rad=-0.1"))
ax.text(85, 71.5, "alerta: respuesta de seguridad inmediata", ha="center", fontsize=8.3, color=TERRA, style="italic")
ax.annotate("", xy=(9.5, 70.6), xytext=(140, 70.6), arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=1.4, connectionstyle="arc3,rad=0.1"))
ax.text(30, 75.6, "respuesta conversacional", ha="center", fontsize=8.5, color=VERDE, style="italic")
flecha((125, 15), (90, 11.2), punteada=True, color=GRIS)
flecha((135, 15), (135, 11.2), punteada=True, color=GRIS)
ax.text(2, 44, "Contorno terracota: componente\nnuevo del Avance 2.\n\nFlechas terracota: recorrido de\nuna imagen y de las alertas.\n\nFlechas punteadas: consultas a la\nbase de conocimiento y al estado.", fontsize=8.3, color=GRIS, va="top")
plt.savefig("figuras/arquitectura_multimodal.png", dpi=220, bbox_inches="tight", facecolor="white")
