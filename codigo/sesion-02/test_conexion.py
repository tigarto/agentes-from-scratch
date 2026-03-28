# codigo/sesion-02/test_conexion.py
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Di 'conexión exitosa' y nada más."
)

print(response.text)
