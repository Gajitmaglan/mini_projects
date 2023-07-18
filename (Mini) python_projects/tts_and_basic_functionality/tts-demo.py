from gtts import gTTS

language_codes = {
    "pt": "pt-br",  # Portuguese (Brazil)
    "fr": "fr",     # French
    "es": "es",     # Spanish
    "ro": "ro",     # Romanian
    "it": "it",     # Italian
}

selected_lang = input("select language (pt, fr, es, ro, it): ")
input_text = input("text to save as mp3 (but not too long): ")

tts = gTTS(input_text, lang=language_codes[selected_lang])
    
filename = f"({selected_lang}) {input_text}.mp3"
tts.save(filename)
