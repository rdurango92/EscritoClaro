## App: Escrito-Claro
## Por: Ruben Durango

# Importaciones
import gradio as gr
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM
import torch
import numpy as np

# Cargar modelo y procesador
ocr_model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
ocr_processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)

# Función para ejecutar el OCR
def run_ocr(task_prompt, image):
    # Asegurarse de que la imagen es un objeto PIL
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    
    prompt = task_prompt
    inputs = ocr_processor(text=prompt, images=image, return_tensors="pt")
    generated_ids = ocr_model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        num_beams=3
    )
    generated_text = ocr_processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
    parsed_answer = ocr_processor.post_process_generation(generated_text, task=task_prompt, image_size=(image.width, image.height))
    return parsed_answer['<OCR>']

# Función para ser llamada en Gradio
def process_image(image):
    ocr_text = run_ocr("<OCR>", image)
    return ocr_text

# Interfaz princital
with gr.Blocks(theme='bethecloud/storj_theme') as demo:
    gr.Markdown("<center><h1>🤓 Escrito-Claro</h1><br><h3>OCR con Florence-2</h3></center>")
    gr.Markdown("Con **EscritoClaro**, convierte tus notas manuscritas en texto digital de forma rápida y precisa, utilizando el modelo Florence-2 de Microsoft.Esta aplicación extrae el texto de tus documentos con buena precisión. Simplemente sube una imagen y deja que EscritoClaro haga el resto.")
    
    # Botón de Procesado
    submit_btn = gr.Button(value="Procesar ⚙️")
    
    with gr.Row():
        # Entradas 
        with gr.Column():
            image = gr.Image(label="Imagen de entrada")
        
        # Salidas
        with gr.Column():
            ocr_text = gr.Textbox(label="Texto OCR", placeholder="Texto extraído")
    
    submit_btn.click(fn=process_image, inputs=image, outputs=ocr_text)  
demo.launch()