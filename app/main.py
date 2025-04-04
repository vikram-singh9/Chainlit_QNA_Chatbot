import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

user_input = ("Enter your message: ")

response  = model.generate_content(user_input)

print(response.text)

