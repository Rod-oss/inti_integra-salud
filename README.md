# Inti, asistente del Consultorio Integra Salud

Proyecto académico de la Maestría en Inteligencia Artificial, asignatura Desarrollo de aplicaciones con inteligencia artificial. Inti es un asistente conversacional para un consultorio privado ficticio de medicina general y homeopatía en México. Responde preguntas frecuentes, orienta sobre la consulta de homeopatía, registra y consulta citas de prueba, deriva a una persona y, desde el segundo avance, clasifica intenciones con un modelo entrenado y reconoce el tipo de documento que el paciente envía en una foto.

> Todos los datos del consultorio, las frases de entrenamiento y los documentos de las imágenes son ficticios y se usan solo con fines académicos. Inti identifica el tipo de documento, pero no lee ni interpreta su contenido, no diagnostica y no recomienda tratamientos.

## Avances

| Avance | Qué incluye | Cuaderno ||
|---|---|---|---|
| 1 | Chatbot basado en reglas con Python y NLTK: siete intenciones, filtros de emergencia, encuadre clínico y contención, agenda simulada y 36 casos de prueba | `avance1/avance1_chatbot_inti.ipynb` | 
| 2 | Primera versión multimodal: clasificador de intenciones (TF-IDF y SVM lineal), clasificador visual de documentos (EfficientNet-B0 con transferencia de aprendizaje) e integración en la conversación | `avance2/avance2_inti_multimodal.ipynb` | 


## Resultados del Avance 2

| Componente | Métrica | Resultado |
|---|---|---|
| Clasificador de intenciones | F1 macro en validación cruzada (5 particiones) | 0.890 |
| Clasificador de intenciones | Accuracy y F1 macro en prueba (120 mensajes) | 0.967 y 0.966 |
| Flujo completo | Precisión de intención en la matriz del Avance 1 (36 casos) | 100 % (reglas: 97.2 %) |
| Clasificador visual | Accuracy, precision, recall y F1 macro en prueba (200 imágenes) | 1.000 |
| Clasificador visual | Accuracy en la prueba de estrés (120 imágenes degradadas) | 0.875 |

El 100 % del clasificador visual es una cota optimista: las imágenes de prueba provienen del mismo generador sintético. El análisis completo, con limitaciones, está al final del cuaderno y en el documento de `docs/`.

## Cómo ejecutarlo

1. Abra el cuaderno con el enlace de Colab de la tabla.
2. Opcional: elija Entorno de ejecución, Cambiar tipo de entorno, GPU T4.
3. Ejecute Entorno de ejecución, Ejecutar todas. El cuaderno instala las dependencias que Colab no trae, descarga las imágenes públicas y los pesos preentrenados desde GitHub y genera el conjunto de imágenes sintéticas. Con CPU tarda alrededor de 15 minutos.
4. La última sección abre una conversación con Inti: escriba sus mensajes, escriba `foto` para adjuntar una imagen y `salir` para terminar.

## Estructura del repositorio

```
inti-integra-salud/
├── README.md
├── requirements.txt
├── avance1/
│   └── avance1_chatbot_inti.ipynb        chatbot de reglas
├── avance2/
│   ├── avance2_inti_multimodal.ipynb     cuaderno ejecutado con salidas
│   ├── datos/                            conjunto textual y manifiesto de imágenes
│   ├── figuras/                          gráficas y diagrama de arquitectura
│   ├── pruebas/                          métricas, matriz de pruebas y conversaciones
│   └── herramientas/                     script del diagrama de arquitectura
└── 
```

Las imágenes generadas, las imágenes públicas descargadas y los pesos del modelo entrenado no se suben al repositorio: el cuaderno los reconstruye en cada ejecución (ver `.gitignore`).

## Datos y licencias

1. **Conjunto textual:** 643 frases sintéticas en español, generadas con apoyo de un modelo de lenguaje y revisadas por el autor (`avance2/datos/intenciones.csv`).
2. **Documentos sintéticos:** generados en el cuaderno con datos ficticios, diseño genérico y la marca "DATOS FICTICIOS". No imitan documentos de ninguna institución real.
3. **Recibos:** 100 imágenes del conjunto ICDAR 2019 SROIE (Huang et al., 2019), obtenidas del repositorio público `zzzDavid/ICDAR-2019-SROIE`, con fines de investigación.
4. **Fotografías de escenas:** imágenes de ejemplo de OpenCV (`opencv/opencv`, carpeta `samples/data`).
5. **Pesos preentrenados:** EfficientNet-B0 en ImageNet del paquete `efficientnet_pytorch`.

## Tecnologías

Python 3.10 o superior, NLTK, spaCy, scikit-learn, PyTorch, torchvision, efficientnet_pytorch, pandas y matplotlib, en Google Colab.
