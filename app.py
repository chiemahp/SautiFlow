import gradio as gr
from modules.pdf_parser import extract_text_from_pdf
from modules.voice_input import transcribe_audio
from modules.voice_output import generate_speech
from modules.chat_engine import get_response

def handle_text_input(text):
    response = get_response(text)
    audio_path = generate_speech(response)
    return response, audio_path

def handle_voice_input(audio):
    text = transcribe_audio(audio)
    return handle_text_input(text)

def handle_pdf_input(pdf):
    pdf_text = extract_text_from_pdf(pdf.name)
    return handle_text_input(pdf_text)

##with gr.Blocks() as demo:
    ##gr.Markdown("# 🗣️ SautiFlow\n#### Made by xhumwe")

with gr.Blocks() as demo:
    gr.Image(value="assets/sautiflow1.png", width=96, show_label=False)
    gr.Markdown("#### Developed by xhumwe")

    with gr.Tab("Text"):
        text_input = gr.Textbox(label="Type your question")
        text_output = gr.Textbox(label="Response")
        audio_output = gr.Audio(label="Voice", autoplay=True)
        text_btn = gr.Button("Submit")
        text_btn.click(fn=handle_text_input, inputs=[text_input], outputs=[text_output, audio_output])  # ✅ inside Blocks

    with gr.Tab("Voice"):
        voice_input = gr.Audio(label="Record your voice", type="filepath", interactive=True)
        voice_output = gr.Textbox(label="Response")
        voice_audio = gr.Audio(label="Voice", autoplay=True)
        voice_btn = gr.Button("Transcribe & Respond")
        voice_btn.click(fn=handle_voice_input, inputs=[voice_input], outputs=[voice_output, voice_audio])  # ✅ inside Blocks

    with gr.Tab("PDF"):
        pdf_input = gr.File(label="Upload PDF")
        pdf_output = gr.Textbox(label="Response")
        pdf_audio = gr.Audio(label="Voice", autoplay=True)
        pdf_btn = gr.Button("Analyze PDF")
        pdf_btn.click(fn=handle_pdf_input, inputs=[pdf_input], outputs=[pdf_output, pdf_audio])  # ✅ inside Blocks

demo.launch('share=True')
