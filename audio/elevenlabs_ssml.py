# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 17:51:57 2025

@author: TechTailor
"""


import requests

def format_text_with_ssml(text):
    paragraphs = text.strip().split("\n")
    ssml = "<speak>\n"
    for para in paragraphs:
        clean_para = para.strip()
        if clean_para:
            ssml += f"  <p>{clean_para}</p>\n"
            ssml += "  <break time=\"500ms\"/>\n"
    ssml += "</speak>"
    return ssml

# 🟡 Your input text (from LLM, file, etc.)
raw_text = """
The United Nations was founded in 1945 after World War II.
Its goal is to maintain international peace and promote cooperation among nations.

Today, nearly every country on Earth is a member.
The UN works on issues like climate change, human rights, and global health.
"""

ssml_text = format_text_with_ssml(raw_text)

api_key = ""  # <-- Replace this with your real key
voice_id = "21m00Tcm4TlvDq8ikWAM"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

data = {
    "text": ssml_text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    },
    "text_type": "ssml"
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open("output_ssml_snippet.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Audio saved as 'output_ssml_snippet.mp3'")
else:
    print("❌ Error:", response.status_code)
    print(response.text)