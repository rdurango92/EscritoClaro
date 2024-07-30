# EscritoClaro

EscritoClaro es una aplicación diseñada para transformar texto manuscrito en texto digital de manera rápida y precisa. Utilizando el modelo Florence-2 de Microsoft y la interfaz de usuario proporcionada por Gradio, esta herramienta está diseñada para ser accesible y gratuita a traves de HuggingFace.

## Descripción

En el mundo digital actual, la digitalización de textos manuscritos sigue siendo un desafío. Inspirado por una amiga que disfruta escribir a mano pero encuentra difícil digitalizar sus escritos, EscritoClaro nace para solucionar este problema. Con EscritoClaro, cualquier persona puede subir una imagen de un texto manuscrito y convertirlo fácilmente en texto digital.

## Características

- **OCR Preciso**: Utiliza el modelo Florence-2 de Microsoft para reconocimiento óptico de caracteres.
- **Interfaz Simple**: Gradio proporciona una interfaz amigable y fácil de usar.
- **Accesible y Gratuito**: Diseñado para ser utilizado por cualquier persona sin costo.

## Cómo Usar

1. **Sube una Imagen**: Toma una foto de tu texto manuscrito.
2. **Procesa la Imagen**: La aplicación transformará la imagen en texto digital.
3. **Descarga el Texto**: Obtén el texto digitalizado listo para editar y usar.

## Instalación

Para ejecutar EscritoClaro localmente, sigue estos pasos:

1. Clona este repositorio:
    ```bash
    git clone https://github.com/rdurango92/EscritoClaro.git
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta la aplicación:
    ```bash
    gradio app.py
    ```
## Futuras Funcionalidades

Estoy trabajando en una segunda etapa de procesamiento que no solo digitalice el texto, sino que también corrija la ortografía y ayude con la dicción en español. Esta funcionalidad adicional será muy útil para aquellos que quieran perfeccionar sus escritos.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar EscritoClaro, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Espero que disfrutes usando EscritoClaro tanto como yo disfruté creándolo!

# [Prueba EscritoClaro aquí](https://huggingface.co/spaces/Rdurango92/EscritoClaro)  