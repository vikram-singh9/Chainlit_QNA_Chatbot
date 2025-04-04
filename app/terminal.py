import google.generativeai as genai  # for google genai api
from dotenv import load_dotenv  # for loading environment variables
import os  # for environment variables

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API with the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Main chat loop
while True:
    # Get user input from terminal
    user_input = input("\nEnter your question (or 'quit' to exit): ")

    # Check if user wants to quit
    if user_input.lower() == "quit":
        print("Thanks for chatting! Goodbye!")
        break

    # Generate response using user's input
    response = model.generate_content(user_input)

    # Print the response
    print("\nResponse:", response.text)