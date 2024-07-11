## App: Escrito-Claro
## Por: Ruben Durango

# Importaciones
import gradio as gr


# Interfaz princital
with gr.Blocks() as demo:
    gr.Markdown("<center><h1>🤓 Escrito-Claro</h1><br><h3>OCR con Florence-2</h3></center>")
    gr.Markdown("Con **EscritoClaro**, convierte tus notas manuscritas en texto digital de forma rápida y precisa, utilizando el modelo Florence-2 de Microsoft.Esta aplicación extrae el texto de tus documentos con buena precisión. Simplemente sube una imagen y deja que EscritoClaro haga el resto.")
    
    # Entradas 
    with gr.Column():
        image = gr.Image(label="Imagen de entrada")
        submit_btn = gr.Button(value="Procesar ⚙️")
    
    # Salidas
    with gr.Column():
        ocr_text = gr.Textbox(label="Texto OCR", placeholder="Texto extraído")
demo.launch()