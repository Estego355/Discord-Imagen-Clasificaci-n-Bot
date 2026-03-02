# Discord-Imagen-Clasificaci-n-Bot
este es un bot de Discord creado en Teachable Machine cuyo objetivo es diferenciar entre tres personajes del universo de Dragon Ball 🐉: Goku 💪, Bardock 🔴 y Goku Black 🌸⚡.

Este proyecto consiste en un clasificador de imágenes entrenado con inteligencia artificial 🤖. Lo que hace el modelo es analizar una imagen, ya sea tomada desde la cámara 📷 o cargada desde un archivo 🖼️, y determinar a cuál de estos tres personajes pertenece. El resultado no es simplemente un nombre, sino un porcentaje de probabilidad 📊 que indica qué tan seguro está el modelo de su decisión.

El modelo fue desarrollado utilizando la herramienta Teachable Machine de Google 💻, que permite entrenar redes neuronales convolucionales sin necesidad de programar desde cero. Internamente, el sistema analiza patrones visuales como colores 🎨, formas, proporciones del rostro, peinados y detalles característicos del vestuario 👕.

Para entrenarlo, se crearon tres clases principales.

La primera clase corresponde a Goku 💪. En esta categoría se incluyeron imágenes del personaje en distintas posiciones, ángulos y expresiones 😃😠. Se usaron versiones en estado base y transformaciones como Super Saiyajin ✨, procurando que el modelo aprendiera rasgos constantes del personaje, como su cabello puntiagudo, el gi naranja 🟠 y la forma de su rostro.

La segunda clase es Bardock. En este caso, se utilizaron imágenes donde se destacaran elementos distintivos como la cicatriz en la mejilla 🩹, la banda roja en la cabeza y la armadura saiyajin 🛡️. El objetivo era que el modelo aprendiera a diferenciarlo de Goku, a pesar de que ambos comparten rasgos físicos similares por ser padre e hijo 👨‍👦.

La tercera clase corresponde a Goku Black 🌸⚡. Aquí se incluyeron imágenes en estado base y en su transformación con cabello rosado. El modelo debía identificar diferencias sutiles, como el vestuario oscuro, los pendientes Potara 💎 y una expresión más seria o agresiva. Aunque visualmente se parece mucho a Goku, el conjunto de detalles en ropa, colores y actitud visual permite que el modelo establezca una distinción.

Durante el entrenamiento, el sistema analizó cientos de ejemplos por clase 📚 y ajustó automáticamente sus parámetros internos para reconocer patrones comunes dentro de cada grupo 🔎. El proceso incluyó pruebas en tiempo real ⏱️ para verificar la precisión y evitar que el modelo confundiera a Goku con Goku Black, que es uno de los desafíos principales debido a su gran parecido.

Al finalizar, el modelo es capaz de observar una imagen nueva y asignarle una probabilidad a cada clase 📊. Por ejemplo, podría indicar un 85% de probabilidad de que sea Goku, un 10% de Bardock y un 5% de Goku Black, tomando como resultado final la categoría con mayor porcentaje.

En conclusión, este modelo demuestra cómo una herramienta accesible puede entrenar un sistema de visión artificial capaz de distinguir personajes con características similares, basándose en patrones visuales aprendidos durante el entrenamiento 📖. Además, evidencia cómo la inteligencia artificial puede aplicarse al reconocimiento de imágenes de manera práctica y comprensible incluso sin conocimientos avanzados de programación 💡.
