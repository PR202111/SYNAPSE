# 🧠 AI Medicine Assistant

An intelligent assistant that helps identify and understand medicines using **computer vision**, **OCR**, and **AI-powered dialogue** — available in **English** and **Telugu**, with **voice interaction** support.

Built using **Ollama Llama 3.2**, **YOLO**, and **LangChain**, it allows users to simply upload a photo of a pill or package, talk to the agent, and get instant results.

---

## ✨ Features

### 🩺 **Medicine Recognition**

* Fine-tuned **YOLO model** trained on **500+ medicine images**.
* Detects medicines based on **shape, color, size, and markings**.
* Supports **image input** from camera.

### 🔍 **OCR + Text Understanding**

* Uses **OCR** to extract text from packaging and prescriptions.
* Queries a **ChromaDB** knowledge base using **RAG (Retrieval-Augmented Generation)** to give contextual information.

### 🗣️ **Voice & Text Interaction**

* Talk naturally or type — supports both **speech** and **text** modes.
* Converts responses to **speech** using text-to-speech engine.
* Available in **English** and **Telugu**.

### 🧩 **LangChain-Powered Agent Pipeline**

* Combines **OCR**, **YOLO**, **LLM (Llama 3.2)**, and **ChromaDB** through **LangChain agents**.
* Each component communicates seamlessly for an end-to-end experience.

---

## ⚙️ Tech Stack

| Component             | Tool / Library              |
| --------------------- | --------------------------- |
| **LLM**               | Ollama Llama 3.2            |
| **Computer Vision**   | YOLO (fine-tuned)           |
| **OCR**               | EasyOCR / Tesseract         |
| **Pipeline**          | LangChain                   |
| **Database (RAG)**    | ChromaDB                    |
| **Speech Processing** | pyttsx3 / SpeechRecognition |
| **Interface**         | Streamlit                   |
| **Runtime**           | Local Machine               |

---
🧠 Current Capabilities

At this stage, the AI can accurately recognize and provide information about the following medicines:

Aspirin

Crocin

Meftal

Paracetamol

Saridon

(More medicines will be added as the dataset expands.)
---

## 🧰 Installation Guide

### 🪶 Prerequisites

Make sure you have the following installed:

* Python **3.10+**
* **Ollama** (for Llama 3.2) → [Install Guide](https://ollama.ai/download)
* **pip** package manager
* GPU support (optional but recommended for YOLO inference)

---

### 🧩 1. Clone the Repository

```bash
git clone https://github.com/PR202111/SYNAPSE.git
cd SYNAPSE
```

---

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```
---

### 🧠 3. Run Ollama & Pull the Model

```bash
ollama pull llama3.2
```

*(Ensure Ollama service is running in the background.)*

---

### 💡 4. Run the Application

```bash
streamlit run app.py
```

or if using CLI mode:

```bash
python main.py
```

---

## 🔁 How It Works

1. User uploads an image or talks to the assistant.
2. YOLO model identifies the medicine from the image.
3. OCR extracts text (like name, dosage).
4. Data is passed to **LangChain Agent** → queries **ChromaDB (RAG)**.
5. **Llama 3.2 (Ollama)** generates a natural, contextual explanation.
6. Text-to-Speech converts the output to audio response (English/Telugu).

---

## 🧪 Example Use Case

> 👩‍🏫 **Professor Karthik:** *[Uploads a pill image]*
>
> 🤖 **Agent:** “This appears to be **Amoxicillin 500mg** — an antibiotic used to treat bacterial infections.”
>
> *(Voice output: response spoken aloud in the selected language)*

---
