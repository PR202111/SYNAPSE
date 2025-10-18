from langdetect import detect
from deep_translator import GoogleTranslator
from speech import speak_text, get_input_text
from config import SUPPORTED_LANGS, TTS_LANG_MAP

def run_agent(agent_llm, retriever, yolo_output="", ocr_output=""):
    chat_history = []

    # Language selection
    print("Choose preferred language:")
    for code, name in SUPPORTED_LANGS.items():
        print(f"{code}: {name}")
    preferred_lang = input("Enter language code (default: en): ").lower()
    if preferred_lang not in SUPPORTED_LANGS:
        preferred_lang = 'en'
    print(f"Language: {SUPPORTED_LANGS[preferred_lang]}")

    while True:
        print("\n--- Conversation ---")
        user_input = get_input_text()
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            speak_text("Goodbye!", TTS_LANG_MAP[preferred_lang])
            break

        # Detect language
        try:
            detected_lang = detect(user_input)
        except:
            detected_lang = 'auto'

        # Translate to English
        english_text = GoogleTranslator(source='auto', target='en').translate(user_input)
        print(f"User query (EN): {english_text}")

        # Retrieve info
        docs = retriever.invoke(english_text)
        info_text = "\n".join([doc.page_content for doc in docs])

        # Only include YOLO/OCR if available
        combined_info = info_text
        if yolo_output:
            combined_info += f"\nYOLO detected: {yolo_output}"
        if ocr_output:
            combined_info += f"\nOCR text: {ocr_output}"

        # Prompt
        prompt_text = f"""
        You are a Doctor's assistant and you are autorized to give information on what is asked with 2-3 line
        statements. and if you dont have any idea about the question then deny it gracefully,
        Use the following info:
        {combined_info}

        User question: {english_text}
        """
        agent_response = agent_llm.invoke(prompt_text)

        # Translate
        translated_response = GoogleTranslator(source='en', target=preferred_lang).translate(agent_response)
        print(f"Response ({SUPPORTED_LANGS[preferred_lang]}): {translated_response}")

        # Speak
        speak_text(translated_response, TTS_LANG_MAP[preferred_lang])
