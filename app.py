#%%

#Aplicacion para digitalizar texto manuscrito usando gradio y el modelo Florence-2 de Hugging Face

#Fecha: 2024-07-04
#Autor: @rdurango92

#%% Importaciones

import requests
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM, pipeline
import torch

#%% Cargar modelo y procesador

ocr_model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
ocr_processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)

# Cargar modelo para corrección de texto
device = 0 if torch.cuda.is_available() else -1 # -1 para CPU, 0 para GPU
#correction_model = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction", device=device)

#%% Carga de Imagen

image_path = "data/page3.jpg"
image = Image.open(image_path)

#%% Funcion para correr el ejemplo

def run_ocr(task_prompt, image):
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

#%% Ejecucion de la tarea
prompt = "<OCR>"
ocr_text = run_ocr(prompt, image)
print("Texto OCR:", ocr_text)

#%%
