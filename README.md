# 🗣️ Multimodal AI Voice Assistant(SautiFlow) — combining speech recognition, text-to-speech, document parsing, and LLM-powered reasoning for interactive human-AI communication.

## 🚀 Features
- 🎙️ Voice input (Whisper)
- 🔊 Voice output (gTTS)
- 📄 PDF parsing (pyMuPDF)
- 💬 LLM-powered responses (Groq)
- 🖥️ Gradio UI with text, voice, and PDF modes

## 🛠️ Setup
```bash
pip install -r requirements.txt


🧠 Core Capabilities Recap
Feature:Text Input/Output		
Tech Used:Python + Gradio UI
Role: in the Assistant:Chat interface for typing and reading responses.

Features:Voice Input
Tech used:Whisper (speech-to-text)	
Role: Converts spoken queries to text

Features:Voice Output	
Tech Used:gTTS (text-to-speech)	
Role:Speaks responses aloud.

Features:PDF Parsing	
Tech Used:pyMuPDF	
Role:Extracts and analyzes text from uploaded PDFs

Features:LLM Backend	
Tech Used:Groq + model (e.g. LLaMA, Mistral)
Role:Powers the assistant’s reasoning and responses.


🚀 Enhancement Ideas


-📄 Smart PDF Q&A: Let users ask questions like “Summarize this contract” or “What’s the due date in this invoice?” and extract answers from the PDF using semantic search or chunked context feeding.

-🎙️ Real-Time Voice Loop: Add a loop that continuously listens and responds like a true voice assistant (e.g., using sounddevice or pyaudio for real-time mic input).

-🌍 Language Switching: Add a dropdown in Gradio to switch between languages for both input and output (Whisper + gTTS support many).

-🧩 Modular UI: Use Gradio’s Blocks to create a clean layout with tabs for Text, Voice, and PDF modes.

-📦 Deployment: Package it into a Hugging Face Space or Docker container for easy sharing and testing.

# Run app

python app.py

## Icon Concepts
SautiFlow
Icon: A stylized soundwave forming a brain or spiral.

Colors: Warm earth tones + digital blue.

Style: Minimalist, fluid, motion-inspired.

demo:https://drive.google.com/file/d/1XrPWvA2IeP023rH6_wOimW5zmvpvTHrh/view?usp=sharing
