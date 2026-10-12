"""Inferencia con un clasificador Keras guardado en formato .keras."""

import argparse
import numpy as np
import keras

CLASS_NAMES = ["diseased", "healthy"]


def predict_image(model_path: str, image_path: str) -> tuple[str, float]:
    """Predice la clase de una imagen y devuelve clase y confianza porcentual."""
    model = keras.models.load_model(model_path)

    image = keras.utils.load_img(image_path, target_size=(224, 224))
    array = keras.utils.img_to_array(image)
    batch = np.expand_dims(array, axis=0)

    probabilities = model.predict(batch, verbose=0)[0]
    index = int(np.argmax(probabilities))
    return CLASS_NAMES[index], float(probabilities[index] * 100)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clasifica una imagen de hoja de limón con un modelo Keras guardado."
    )
    parser.add_argument("--model", required=True, help="Ruta al archivo .keras")
    parser.add_argument("--image", required=True, help="Ruta a la imagen de entrada")
    args = parser.parse_args()

    label, confidence = predict_image(args.model, args.image)
    print(f"Predicción: {label}")
    print(f"Confianza: {confidence:.2f}%")


if __name__ == "__main__":
    main()
