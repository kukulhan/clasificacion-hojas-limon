# Código fuente

`predict.py` contiene una función genérica para ejecutar inferencia con un modelo Keras previamente guardado en formato `.keras`.

El notebook de Colab crea los clasificadores entrenados en memoria. Para usar `predict.py`, primero guarda el modelo entrenado desde Colab, por ejemplo:

```python
clasificadores["EfficientNetB0"].save("efficientnetb0_hojas.keras")
```

Después, copia el archivo `.keras` a una ruta local y úsala como argumento para el script. No se incluye un modelo entrenado en este repositorio.
