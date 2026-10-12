# Clasificación de hojas de limón con visión artificial

Proyecto experimental para clasificar imágenes de hojas de limón en dos categorías: `healthy` (sana) y `diseased` (enferma). Se comparan tres modelos preentrenados disponibles en Hugging Face Hub: ResNet50, EfficientNetB0 y MobileNetV3 Small.

## Objetivo

Evaluar el desempeño de tres modelos mediante transferencia de aprendizaje y comparar sus métricas de clasificación, latencia de inferencia y tamaño descargado.

## Dataset

Se utilizó la carpeta `Lemon (P10)` del conjunto público [Healthy vs Diseased Leaf Image Dataset](https://www.kaggle.com/datasets/amandam1/healthy-vs-diseased-leaf-image-dataset).

- Total de imágenes: 236
- Hojas enfermas: 77
- Hojas sanas: 159
- Entrenamiento: 189 imágenes
- Validación: 47 imágenes
- Resolución: 224 × 224 píxeles
- Batch size: 16
- Semilla de división: 42

El dataset no se incluye en este repositorio. Descárgalo desde Kaggle y respeta las condiciones de uso de la fuente original.

## Modelos comparados

| Modelo | Repositorio de Hugging Face |
|---|---|
| ResNet50 | [keras/resnet_50_imagenet](https://huggingface.co/keras/resnet_50_imagenet) |
| EfficientNetB0 | [keras/efficientnet_b0_ra_imagenet](https://huggingface.co/keras/efficientnet_b0_ra_imagenet) |
| MobileNetV3 Small | [keras/mobilenet_v3_small_100_imagenet](https://huggingface.co/keras/mobilenet_v3_small_100_imagenet) |

## Entorno de ejecución

- Google Colab
- Python
- TensorFlow / Keras / KerasHub
- Hugging Face Hub para acceder a los modelos
- KaggleHub para descargar el dataset
- Experimentos ejecutados en CPU; no se registraron las especificaciones exactas del procesador ni la memoria RAM.

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

En Colab, configura las credenciales de Kaggle si son necesarias para descargar el dataset. La autenticación de Hugging Face se realiza dentro del notebook si el flujo utilizado la requiere. **No guardes tokens, contraseñas ni archivos de credenciales en GitHub.**

## Pasos de ejecución

1. Abre `notebooks/clasificacion_hojas_limon.ipynb` en Google Colab.
2. Selecciona un entorno de ejecución con Python y ejecuta las celdas en orden.
3. Instala las dependencias y descarga el dataset desde Kaggle.
4. Descarga los modelos preentrenados desde Hugging Face Hub.
5. Carga las imágenes, divide los datos en entrenamiento y validación y entrena la cabeza de clasificación durante cinco épocas.
6. Evalúa accuracy, precision, recall y F1-score; revisa las matrices de confusión.
7. Mide la latencia y genera las tablas de resultados.
8. Guarda los CSV de salida en la carpeta `results/`.

Si el notebook exportado desde Colab tiene otro nombre, actualiza la ruta indicada en este README.

## Resultados principales

| Modelo | Accuracy | Precision diseased | Recall diseased | F1 diseased | Latencia (ms/imagen) | Tamaño descargado |
|---|---:|---:|---:|---:|---:|---:|
| ResNet50 | 82.98% | 100.00% | 38.46% | 55.56% | 227.20 | 188.44 MB |
| EfficientNetB0 | 85.11% | 80.00% | 61.54% | 69.57% | 88.62 | 36.91 MB |
| MobileNetV3 Small | 82.98% | 72.73% | 61.54% | 66.67% | 116.46 | 14.13 MB |

Los tiempos corresponden al entorno experimental utilizado y pueden variar según el hardware y la configuración.

## Conclusiones

EfficientNetB0 fue el mejor candidato general en este experimento: obtuvo el mayor accuracy (85.11%), el mejor F1-score para hojas enfermas (69.57%) y la menor latencia promedio (88.62 ms/imagen). MobileNetV3 Small fue el modelo más ligero (14.13 MB). ResNet50 tuvo el menor recall para la clase enferma.

Los resultados son preliminares. La validación incluyó solo 47 imágenes, de las cuales 13 eran enfermas. EfficientNetB0 no detectó 5 de esas 13 hojas enfermas. Por ello, el modelo no debe utilizarse como diagnóstico agrícola autónomo sin ampliar los datos y evaluar un conjunto de prueba independiente.

## Estructura del repositorio

```text
.
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── notebooks/
│   ├── README.md
│   └── clasificacion_hojas_limon.ipynb
├── results/
│   ├── comparativa_modelos.csv
│   ├── metricas_clasificacion.csv
│   └── README.md
└── src/
    ├── predict.py
    └── README.md
```

## Licencias de los modelos

En los metadatos consultados, ResNet50 y EfficientNetB0 reportaron Apache-2.0. La licencia de MobileNetV3 Small no apareció especificada en la consulta realizada; debe verificarse en su ficha antes de cualquier uso comercial. La licencia del dataset también debe consultarse en Kaggle.

## Reproducibilidad y limitaciones

Se usó una semilla de 42 para la partición del dataset, imágenes de 224 × 224, lotes de 16 y cinco épocas de entrenamiento. La partición usada fue de 189 imágenes para entrenamiento y 47 para validación. No se utilizó un conjunto de prueba independiente. Las métricas no demuestran por sí solas que el sistema generalice a fotografías tomadas en condiciones agrícolas reales.
