# main.py
from config import DB_LOCATION
from db import setup_vector_db
from agent import run_agent
from ocr_yolo import capture_image, process_image
from langchain_ollama.llms import OllamaLLM

if __name__ == "__main__":
    agent_llm = OllamaLLM(model="llama3.2")
    retriever = setup_vector_db()

    medicine_name = ""
    extracted_text = ""

    image_present = input("Do you have the medicine with you? (yes/no): ").lower()
    if image_present == "yes":
        image_file = capture_image()
        if image_file:
            medicine_name, extracted_text = process_image(image_file)

    run_agent(agent_llm, retriever, yolo_output=medicine_name, ocr_output=extracted_text)
